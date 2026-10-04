import numpy as np, math, sys, os
from PIL import Image, ImageDraw, ImageFilter
W,H,FPS=1080,1920,30
def ease(t): return 1-(1-t)**3
def eio(t): return t*t*(3-2*t)
def dotwave(i,N,out):
    S=2
    im=Image.new("RGBA",(W*S//2,H*S//2),(0,0,0,0)); d=ImageDraw.Draw(im)
    cols,rows=27,48; gx=W/cols; gy=H/rows
    ph=2*math.pi*i/N
    cx,cy=W*0.5,H*0.42
    for r in range(rows):
        for c in range(cols):
            x=(c+.5)*gx; y=(r+.5)*gy
            dist=math.hypot(x-cx,y-cy)/W
            w=math.sin(dist*9*math.pi-ph*2)  # radial ripple, loops (integer cycles)
            w2=math.sin(x/W*2*math.pi*1+ph+y/H*3)
            v=(w*0.65+w2*0.35)*0.5+0.5
            rad=gx*(0.07+0.17*v)
            a=int(55+150*v)
            col=(int(110+40*v),int(150+50*v),255,a)
            X,Y=x*S/2,y*S/2;R=rad*S/2
            d.ellipse([X-R,Y-R,X+R,Y+R],fill=col)
    im=im.resize((W,H),Image.LANCZOS); im.save(out)
def card(i,N,out,cw=820,ch=520,rad=64):
    t=i/(N-1)
    # in 0-.3 slide from right w/ ease, hold, out .8-1 slide left
    if t<.3: off=(1-ease(t/.3))*900; al=eio(t/.3)
    elif t<.8: off=0; al=1
    else: off=-eio((t-.8)/.2)*900; al=1-eio((t-.8)/.2)
    S=2
    cardim=Image.new("RGBA",(cw*S,ch*S),(0,0,0,0))
    m=Image.new("L",cardim.size,0); ImageDraw.Draw(m).rounded_rectangle([0,0,cw*S-1,ch*S-1],rad*S,fill=255)
    # frosted fill: vertical gradient white
    g=np.zeros((ch*S,cw*S,4),np.uint8)
    yy=np.linspace(0,1,ch*S)[:,None]
    xx=np.linspace(0,1,cw*S)[None,:]
    g[...,0]=255;g[...,1]=255;g[...,2]=255
    sheenpos=(t*1.6-0.3)
    sheen=np.exp(-(((xx+yy*0.4)-sheenpos)**2)/0.012)*60
    g[...,3]=np.clip(70+60*(1-yy)+sheen,0,255).astype(np.uint8)
    gi=Image.fromarray(g,"RGBA")
    cardim=Image.composite(gi,cardim,m)
    # border highlight
    bd=Image.new("RGBA",cardim.size,(0,0,0,0));dd=ImageDraw.Draw(bd)
    dd.rounded_rectangle([0,0,cw*S-1,ch*S-1],rad*S,outline=(255,255,255,200),width=3*S)
    cardim=Image.alpha_composite(cardim,bd)
    # inner top gloss line
    cardim=cardim.resize((cw,ch),Image.LANCZOS)
    # content placeholder: soft bars
    cd=ImageDraw.Draw(cardim)
    for k,wd in enumerate([0.55,0.8,0.65]):
        cd.rounded_rectangle([60,70+k*70,60+int((cw-120)*wd),70+k*70+28],14,fill=(255,255,255,150))
    canvas=Image.new("RGBA",(W,H),(0,0,0,0))
    x=int((W-cw)/2+off); y=int((H-ch)/2)
    # shadow
    sh=Image.new("RGBA",(W,H),(0,0,0,0)); sm=Image.new("L",(cw,ch),0)
    ImageDraw.Draw(sm).rounded_rectangle([0,0,cw-1,ch-1],rad,fill=255)
    shl=Image.new("RGBA",(cw,ch),(40,60,120,90)); sh.paste(shl,(x,y+36),sm)
    sh=sh.filter(ImageFilter.GaussianBlur(34))
    canvas=Image.alpha_composite(canvas,sh)
    canvas.alpha_composite(cardim,(max(0,x) if x>=0 else 0,y)) if False else None
    tmp=Image.new("RGBA",(W,H),(0,0,0,0)); tmp.paste(cardim,(x,y)); canvas=Image.alpha_composite(canvas,tmp)
    if al<1:
        a=np.array(canvas); a[...,3]=(a[...,3]*al).astype(np.uint8); canvas=Image.fromarray(a,"RGBA")
    canvas.save(out)
kind=sys.argv[1]; N=int(sys.argv[2]); os.makedirs(kind,exist_ok=True)
for i in range(N):
    (dotwave if kind=="dotwave" else card)(i,N,f"{kind}/f{i:04d}.png")
