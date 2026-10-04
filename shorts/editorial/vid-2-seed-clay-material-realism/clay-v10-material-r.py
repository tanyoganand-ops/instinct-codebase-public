import numpy as np, math, sys, os
from PIL import Image, ImageDraw, ImageFont
from scipy.ndimage import gaussian_filter
A='/tmp/b/src/editorial-short-v9/assets/'
W,H=1920*0+1080,1920
NOSHADOW=os.environ.get('NOSHADOW')=='1'
ANTON=A+'Anton-Regular.ttf'; BOLD=A+'LiberationSans-Bold.ttf'
def clamp(x,a=0,b=1): return max(a,min(b,x))
def ss(x): x=clamp(x); return x*x*(3-2*x)
def eio(x): x=clamp(x); return 0.5-0.5*math.cos(math.pi*x)
def eout(x): x=clamp(x); return 1-(1-x)**3
def seg(t,a,b): return clamp((t-a)/(b-a))
def spring(t,a,dur=0.9):
    s=t-a
    if s<=0: return 0.0
    if s>dur*2.2: return 1.0
    return 1-math.exp(-6.5*s)*math.cos(11*s)
def bell(t,a,b): return math.sin(math.pi*seg(t,a,b))
def lerp(a,b,u): return a+(b-a)*u
def norm(v): v=np.array(v,float); return v/np.linalg.norm(v)
# ---------- assets
def load_logo(f,h):
    im=Image.open(A+f).convert('RGBA'); w=int(im.width*h/im.height); return im.resize((w,h),Image.LANCZOS)
LOGO={'c':load_logo('Claude-logo-Slate-0aff1e24.png',64),'g':load_logo('Gemini-logo-2025-32a9eb8b.png',58)}
_fc={}
def font(p,s):
    k=(p,s)
    if k not in _fc:_fc[k]=ImageFont.truetype(p,s)
    return _fc[k]
# ---------- clay shapes
_sh={}
def rr(w,h,r,bevel,dome=0.0,grain=0.13,seed=1):
    k=(w,h,r,bevel,dome,seed)
    if k in _sh: return _sh[k]
    w=int(w);h=int(h)
    yy,xx=np.mgrid[0:h,0:w].astype(np.float32); xx+=0.5;yy+=0.5
    qx=np.abs(xx-w/2)-(w/2-r); qy=np.abs(yy-h/2)-(h/2-r)
    d=np.hypot(np.maximum(qx,0),np.maximum(qy,0))+np.minimum(np.maximum(qx,qy),0)-r
    al=np.clip(0.5-d,0,1)
    u=np.clip(-d/bevel,0,1)
    hh=bevel*np.sqrt(1-(1-u)**2)
    if dome: hh+=dome*np.clip(-d/(min(w,h)/2),0,1)**0.7
    rng=np.random.RandomState(seed)
    n=gaussian_filter(rng.randn(h,w).astype(np.float32),1.3)*grain*2.2
    hh=hh+n
    _sh[k]=(al,hh.astype(np.float32)); return _sh[k]
_tx={}
def textmask(s,fp,size,spacing=0):
    k=(s,fp,size)
    if k in _tx: return _tx[k]
    f=font(fp,size); pad=14
    bb=f.getbbox(s); w=bb[2]+pad*2; h=int((f.getmetrics()[0]+f.getmetrics()[1]))+pad*2
    im=Image.new('L',(w,h),0); ImageDraw.Draw(im).text((pad,pad),s,font=f,fill=255)
    a=np.asarray(im,np.float32)/255
    hgt=gaussian_filter(a,size*0.045+1.0)*(size*0.11+2)
    _tx[k]=(a,hgt.astype(np.float32),w,h,pad); return _tx[k]
def shade(hh,base,L,gs=1.0,spec=0.06,recess=False,wrap=0.55,warm=0.0):
    if recess: hh=-hh
    gy,gx=np.gradient(hh)
    n=np.stack([-gx*gs,-gy*gs,np.ones_like(hh)],-1); n/=np.linalg.norm(n,axis=-1,keepdims=True)
    nl=n@L
    diff=np.clip((nl+wrap)/(1+wrap),0,1)
    base=np.array(base,np.float32)/255
    # clay: shadows go toward saturated darker tint of base (sss-like)
    sat=np.clip(base*1.0-0.18*(base.mean()-base)*-1,0,1)
    shadow_c=base*np.array([0.66,0.62,0.74])
    lit_c=np.clip(base*1.07+np.array([0.03,0.02,0.0]),0,1)
    d=diff[...,None]**1.15
    col=shadow_c*(1-d)+lit_c*d
    Hh=norm(L+np.array([0,0,1.0]))
    sp=np.clip(n@Hh,0,1)**9*spec   # very broad matte sheen
    rim=(1-n[...,2])**2.5*0.05
    col=col+(sp+rim)[...,None]
    return np.clip(col,0,1)
# ---------- layer compositing (premultiplied float)
class Layer:
    def __init__(s,y0,h):
        s.y0=y0; s.a=np.zeros((h,W,4),np.float32)
    def over(s,rgb,al,x,y,alpha=1.0):
        x=int(round(x)); y=int(round(y))-s.y0
        h,w=al.shape
        X0=max(x,0);Y0=max(y,0);X1=min(x+w,W);Y1=min(y+h,s.a.shape[0])
        if X0>=X1 or Y0>=Y1: return
        sub_a=al[Y0-y:Y1-y,X0-x:X1-x]*alpha
        sub_c=rgb[Y0-y:Y1-y,X0-x:X1-x]
        dst=s.a[Y0:Y1,X0:X1]
        inv=(1-sub_a)[...,None]
        dst[...,:3]=sub_c*sub_a[...,None]+dst[...,:3]*inv
        dst[...,3:]=sub_a[...,None]+dst[...,3:]*inv
    def shadow(s,al,x,y,elev,L,alpha=1.0,color=(70,62,104)):
        if NOSHADOW or alpha<=0.01: return
        ox=-L[0]/L[2]*elev; oy=-L[1]/L[2]*elev
        sig=3+elev*0.5; pad=int(sig*3)+2
        p=np.pad(al,pad)
        c=np.array(color,np.float32)/255
        # cast
        g=gaussian_filter(p,sig)*0.26*alpha
        s.over(np.broadcast_to(c,g.shape+(3,)),g,x-pad+ox,y-pad+oy)
        # contact
        g2=gaussian_filter(p,3.0)*0.34*alpha*(1 if elev<40 else 0.6)
        s.over(np.broadcast_to(c,g2.shape+(3,)),g2,x-pad+ox*0.12,y-pad+oy*0.12+1.5)
    def clay(s,w,h,r,bevel,base,L,x,y,elev=18,alpha=1.0,dome=0,recess=False,seed=1,gs=1.1,shadow=True,spec=0.05):
        al,hh=rr(w,h,r,bevel,dome,seed=seed)
        if shadow and not recess: s.shadow(al,x,y,elev,L,alpha)
        col=shade(hh,base,L,gs=gs,recess=recess,spec=spec)
        s.over(col,al,x,y,alpha)
    def text(s,txt,fp,size,base,L,cx,cy,alpha=1.0,gs=1.4,shadow=True,blur=0,elev=6,spec=0.12):
        a,hh,w,h,pad=textmask(txt,fp,size)
        col=shade(hh,base,L,gs=gs,spec=spec,wrap=0.45)
        al=a
        if blur>0.3:
            al=gaussian_filter(a,blur); col=np.stack([gaussian_filter(col[...,i],blur) for i in range(3)],-1)
        x=cx-w/2; y=cy-h/2
        if shadow and blur<1: s.shadow(al,x,y,elev,L,alpha*0.4)
        s.over(col,al,x,y,alpha)
    def decal(s,im,cx,cy,alpha=1.0):
        a=np.asarray(im,np.float32)/255
        s.over(a[...,:3],a[...,3],cx-im.width/2,cy-im.height/2,alpha)
    def ball(s,cx,cy,r,L,alpha=1.0,elev=0,sx=1.0,sy=1.0,base=(205,188,240)):
        rx=r*sx; ry=r*sy
        w=int(rx*2)+4;h=int(ry*2)+4
        yy,xx=np.mgrid[0:h,0:w].astype(np.float32)
        px=(xx+0.5-w/2)/rx; py=(yy+0.5-h/2)/ry
        rho=np.hypot(px,py); al=np.clip((1-rho)*rx*0.5+0.5,0,1)
        z=np.sqrt(np.clip(1-rho**2,0,1))
        n=np.stack([px,py,z],-1)
        # clay grain
        rng=np.random.RandomState(7); g=gaussian_filter(rng.randn(h,w).astype(np.float32),1.2)*0.035
        n[...,:2]+=g[...,None]; n/=np.linalg.norm(n,axis=-1,keepdims=True)
        diff=np.clip((n@L+0.55)/1.55,0,1)[...,None]**1.15
        b=np.array(base,np.float32)/255
        col=b*np.array([0.66,0.6,0.78])*(1-diff)+np.clip(b*1.07,0,1)*diff
        Hh=norm(L+np.array([0,0,1.0])); col+= (np.clip(n@Hh,0,1)**9*0.06)[...,None]+((1-z)**2.5*0.05)[...,None]
        col=np.clip(col,0,1)
        if elev>=0 and not NOSHADOW:
            s.shadow(al,cx-w/2,cy-h/2,elev,L,alpha)
        s.over(col,al,cx-w/2,cy-h/2,alpha)
# ---------- perspective
def persp_coeffs(yaw,pitch,cx,cy,f=2600.0,W_=W,H_=H):
    ya=math.radians(yaw); pa=math.radians(pitch)
    def proj(x,y):
        X=x-cx;Y=y-cy;Z=0
        X1=X*math.cos(ya)+Z*math.sin(ya); Z1=-X*math.sin(ya)+Z*math.cos(ya)
        Y2=Y*math.cos(pa)-Z1*math.sin(pa); Z2=Y*math.sin(pa)+Z1*math.cos(pa)
        s=f/(f+Z2); return cx+X1*s, cy+Y2*s
    src=[(0,0),(W_,0),(W_,H_),(0,H_)]
    dst=[proj(*p) for p in src]
    A_=[];B_=[]
    for (x,y),(u,v) in zip(src,dst):  # map dst->src for PIL
        A_.append([u,v,1,0,0,0,-x*u,-x*v]);B_.append(x)
        A_.append([0,0,0,u,v,1,-y*u,-y*v]);B_.append(y)
    return np.linalg.solve(np.array(A_,float),np.array(B_,float))
# ---------- background
yy,xx=np.mgrid[0:H,0:W].astype(np.float32)
g=np.random.RandomState(3).randn(H,W).astype(np.float32)*1.0
BG0=np.stack([240+2*yy/H-1.0*xx/W, 241.5+1.5*yy/H, 246-1.5*yy/H],-1)
vig=1-0.035*((xx-540)/540)**2-0.03*((yy-960)/960)**2
BG0=BG0*vig[...,None]+g[...,None]
def bg_frame(L,t):
    # soft moving light pool on the "floor": slow, low contrast, tied to key light, NOT drifting bg detail
    lx=540+L[0]*-380; ly=620+L[1]*-300
    sm=np.exp(-(((xx[::4,::4]-lx)/620)**2+((yy[::4,::4]-ly)/760)**2))
    sm=np.asarray(Image.fromarray((sm*255).astype(np.uint8)).resize((W,H),Image.BICUBIC),np.float32)/255
    return BG0+ (sm*5.0)[...,None]*np.array([1.0,0.9,0.7])
