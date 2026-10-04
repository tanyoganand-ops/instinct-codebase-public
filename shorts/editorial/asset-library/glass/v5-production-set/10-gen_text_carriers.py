import numpy as np, sys, os
from PIL import Image, ImageDraw, ImageFilter
W,H=1080,1920
ease=lambda t:1-(1-min(max(t,0),1))**3
eio=lambda t:(lambda u:u*u*(3-2*u))(min(max(t,0),1))
def back(t):  # ease-out with slight overshoot settle
    t=min(max(t,0),1);c1=1.2;c3=c1+1
    return 1+c3*(t-1)**3+c1*(t-1)**2
def panel(w,h,rad,sheen=-1,bars=None,label=None):
    S=2
    m=Image.new("L",(w*S,h*S),0);ImageDraw.Draw(m).rounded_rectangle([0,0,w*S-1,h*S-1],rad*S,fill=255)
    yy=np.linspace(0,1,h*S)[:,None];xx=np.linspace(0,1,w*S)[None,:]
    g=np.full((h*S,w*S,4),255,np.uint8)
    sh=np.exp(-(((xx+yy*0.4)-sheen)**2)/0.012)*60 if sheen>-1 else 0
    g[...,3]=np.clip(70+60*(1-yy)+sh,0,255).astype(np.uint8)
    base=Image.composite(Image.fromarray(g,"RGBA"),Image.new("RGBA",m.size,(0,0,0,0)),m)
    bd=Image.new("RGBA",m.size,(0,0,0,0));ImageDraw.Draw(bd).rounded_rectangle([0,0,w*S-1,h*S-1],rad*S,outline=(255,255,255,200),width=3*S)
    p=Image.alpha_composite(base,bd).resize((w,h),Image.LANCZOS)
    d=ImageDraw.Draw(p)
    if bars:
        for k,wd in enumerate(bars):
            y=h//2-12-(len(bars)-1)*18+k*36
            d.rounded_rectangle([int(h*.3),y,int(h*.3)+int((w-h*.5)*wd),y+16],8,fill=(255,255,255,170))
        d.ellipse([int(h*.08),h//2-int(h*.09),int(h*.08)+int(h*.18),h//2+int(h*.09)],fill=(150,185,255,200))
    if label:
        d.rounded_rectangle([w//2-int(w*.2),h//2-12,w//2+int(w*.2),h//2+12],12,fill=(255,255,255,200))
    return p
def put(canvas,p,x,y,al=1,scale=1,shadow=True):
    w,h=p.size
    if scale!=1:
        p=p.resize((max(1,int(w*scale)),max(1,int(h*scale))),Image.LANCZOS);x+= (w-p.size[0])//2;y+=(h-p.size[1])//2;w,h=p.size
    lay=Image.new("RGBA",(W,H),(0,0,0,0))
    if shadow:
        sh=Image.new("RGBA",(W,H),(0,0,0,0));a=p.split()[3].point(lambda v:255 if v>0 else 0)
        sh.paste(Image.new("RGBA",(w,h),(40,60,120,80)),(x,y+int(h*.07)),a);lay=Image.alpha_composite(lay,sh.filter(ImageFilter.GaussianBlur(max(10,h*.07))))
    t=Image.new("RGBA",(W,H),(0,0,0,0));t.paste(p,(x,y));lay=Image.alpha_composite(lay,t)
    if al<1:
        a=np.array(lay);a[...,3]=(a[...,3]*al).astype(np.uint8);lay=Image.fromarray(a,"RGBA")
    return Image.alpha_composite(canvas,lay)
def frame(kind,i,N):
    t=i/(N-1);c=Image.new("RGBA",(W,H),(0,0,0,0))
    if kind=="pill_dropdown":
        p=panel(700,150,75,sheen=t*1.6-.3,bars=[.7,.45])
        if t<.25: y=-200+(260+200)*back(t/.25);al=1
        elif t<.8: y=260;al=1
        else: u=eio((t-.8)/.2);y=260-u*500;al=1-u
        return put(c,p,(W-700)//2,int(y),al)
    if kind=="button_press":
        u=min(t/.2,1);al=eio(u)
        pr=0
        if .45<t<.7: pr=np.sin((t-.45)/.25*np.pi)
        sc=(0.9+0.1*ease(u))*(1-0.06*pr)
        if t>.85: al=1-eio((t-.85)/.15)
        p=panel(560,160,80,sheen=(t-.2)*2.2-.3 if t>.2 else -1,label=True)
        return put(c,p,(W-560)//2,H//2-80,al,sc)
    if kind=="notif_stack":
        for k in range(3):
            s=.08+k*.14;u=back((t-s)/.2)
            ex=eio((t-.82-k*.03)/.15)
            y0=300+k*230;y=int(-260+(y0+260)*u-ex*700)
            al=min(1,(t-s)/.08)*(1-ex) if t>s else 0
            if al>0: c=put(c,panel(900,200,50,sheen=t*1.6-.3,bars=[.8,.5]),(W-900)//2,y,al)
        return c
    if kind=="card_dropdown":
        p=panel(820,520,64,sheen=t*1.6-.3,bars=[.55,.8,.65])
        if t<.3: y=-600+(700+600)*back(t/.3);al=1
        elif t<.8: y=700;al=1
        else: u=eio((t-.8)/.2);y=700+u*800;al=1-u
        return put(c,p,(W-820)//2,int(y),al)

def tint(p,col):
    a=p.split()[3];ov=Image.new("RGBA",p.size,col+(0,));ov.putalpha(a.point(lambda v:int(v*0.55)));return Image.alpha_composite(p,ov)
def badge(w=520,h=130):
    p=tint(panel(w,h,65,sheen=-1),(120,160,255))
    d=ImageDraw.Draw(p);d.ellipse([34,h//2-24,82,h//2+24],fill=(255,255,255,230))  # icon slot
    return p
def frame2(kind,i,N):
    t=i/(N-1);c=Image.new("RGBA",(W,H),(0,0,0,0))
    if kind=="badge_pop":
        p=badge()
        if t<.2: sc=0.2+0.8*back(t/.2)*1.0;al=min(1,t/.08)
        elif t<.8: sc=1+0.04*np.sin((t-.2)/.6*np.pi*2);al=1
        else: u=eio((t-.8)/.2);sc=1-0.25*u;al=1-u
        return put(c,p,(W-520)//2,700,al,max(sc,.05))
    if kind=="source_rail":
        w,h=1000,150;p=panel(w,h,40,sheen=-1)
        d=ImageDraw.Draw(p);d.rounded_rectangle([28,h//2-40,36,h//2+40],4,fill=(120,160,255,230))
        y1=H-420
        if t<.25: y=H+40+(y1-H-40)*ease(t/.25)
        else: y=y1
        al=min(1,t/.1)
        return put(c,p,(W-w)//2,int(y),al)
    if kind=="cta_press":
        w,h=640,170;p=tint(panel(w,h,85,sheen=(t-.25)*2.2-.3 if t>.25 else -1),(120,160,255))
        d=ImageDraw.Draw(p);d.ellipse([46,h//2-34,114,h//2+34],fill=(255,255,255,235));d.polygon([(70,h//2-16),(70,h//2+16),(96,h//2)],fill=(110,150,245,255))
        u=min(t/.18,1);al=eio(u);pr=np.sin((t-.5)/.2*np.pi) if .5<t<.7 else 0
        pulse=1+0.03*np.sin(t*np.pi*6) if .2<t<.5 else 1
        sc=(0.85+0.15*back(u))*(1-0.07*pr)*pulse
        if t>.88: al=1-eio((t-.88)/.12)
        return put(c,p,(W-w)//2,H-520,al,sc)

def aa(draw_fn,size,S=3):
    im=Image.new("RGBA",(size[0]*S,size[1]*S),(0,0,0,0));draw_fn(ImageDraw.Draw(im),S);return im.resize(size,Image.LANCZOS)
def underline(t):
    x0,x1,y=140,940,1000
    L=back(t/.6)  # overshoot then settle
    L=min(L,1.04);xe=x0+(x1-x0)*L
    n=80;pts=[(x0+(xe-x0)*k/n, y+7*np.sin(k/n*np.pi*2.2)+ (k/n)*-6) for k in range(n+1)]
    def f(d,S):
        d.line([(a*S,b*S) for a,b in pts],fill=(110,150,245,235),width=16*S,joint="curve")
        for a,b in (pts[0],pts[-1]):d.ellipse([(a-8)*S,(b-8)*S,(a+8)*S,(b+8)*S],fill=(110,150,245,235))
    return aa(f,(W,H))
def highlight(t):
    x0,x1,y,h=120,960,930,130
    u=ease(t/.55);xe=x0+(x1-x0)*u
    m=Image.new("L",(W*2,H*2),0);ImageDraw.Draw(m).rounded_rectangle([x0*2,y*2,x1*2,(y+h)*2],40,fill=255)
    m=m.resize((W,H),Image.LANCZOS)
    wipe=Image.new("L",(W,H),0);ImageDraw.Draw(wipe).rectangle([0,0,int(xe),H],fill=255)
    a=np.minimum(np.array(m),np.array(wipe)).astype(np.float32)*(120/255)
    arr=np.zeros((H,W,4),np.uint8);arr[...,0]=255;arr[...,1]=214;arr[...,2]=90;arr[...,3]=a.astype(np.uint8)
    return Image.fromarray(arr,"RGBA")
def counter(i,N):
    t=i/(N-1);c=Image.new("RGBA",(W,H),(0,0,0,0))
    u=min(i/12,1);al=eio(u);sc=0.8+0.2*back(u)
    ph=(i%15)/15;tick=0
    if i>=15: tick=0.07*np.exp(-ph*7)*(1 if ph<.6 else 0)  # decaying scale pulse each beat
    return put(c,panel(380,240,70,sheen=-1),(W-380)//2,H//2-120,al,(sc+tick))
def endcard(i,N):
    t=i/(N-1);c=Image.new("RGBA",(W,H),(0,0,0,0))
    u=min(t/.3,1);sc=0.88+0.12*back(u);al=eio(min(t/.2,1))
    w,h=940,1500
    p=panel(w,h,90,sheen=-1)
    d=ImageDraw.Draw(p)
    def replay(dd,S):
        cx,cy,r=470,500,110
        dd.ellipse([(cx-r-26)*S,(cy-r-26)*S,(cx+r+26)*S,(cy+r+26)*S],fill=(255,255,255,120),outline=(255,255,255,210),width=3*S)
        dd.arc([(cx-r+30)*S,(cy-r+30)*S,(cx+r-30)*S,(cy+r-30)*S],40,330,fill=(110,150,245,255),width=16*S)
        dd.polygon([((cx+r-24)*S,(cy-34)*S),((cx+r+22)*S,(cy-6)*S),((cx+r-48)*S,(cy+12)*S)],fill=(110,150,245,255))
    def sub(dd,S):
        x0,y0,x1,y1=130,860,810,1060
        dd.rounded_rectangle([x0*S,y0*S,x1*S,y1*S],100*S,fill=(120,160,255,170),outline=(255,255,255,220),width=3*S)
        cx,cy=x0+110,(y0+y1)//2
        dd.ellipse([(cx-52)*S,(cy-52)*S,(cx+52)*S,(cy+52)*S],fill=(255,255,255,235))
        # bell
        dd.pieslice([(cx-24)*S,(cy-28)*S,(cx+24)*S,(cy+20)*S],180,360,fill=(110,150,245,255))
        dd.polygon([((cx-24)*S,(cy-4)*S),((cx+24)*S,(cy-4)*S),((cx+32)*S,(cy+16)*S),((cx-32)*S,(cy+16)*S)],fill=(110,150,245,255))
        dd.ellipse([(cx-7)*S,(cy+16)*S,(cx+7)*S,(cy+28)*S],fill=(110,150,245,255))
    ov=aa(replay,(w,h));p=Image.alpha_composite(p,ov);ov=aa(sub,(w,h));p=Image.alpha_composite(p,ov)
    # blank text slots under replay + inside subscribe handled by compositor
    return put(c,p,(W-w)//2,(H-h)//2,al,sc)
kind=sys.argv[1];N=int(sys.argv[2]);os.makedirs(kind,exist_ok=True)
for i in range(N):
    t=i/(N-1)
    im={"underline":lambda:underline(t),"highlight":lambda:highlight(t),"counter":lambda:counter(i,N),"endcard2":lambda:endcard(i,N)}[kind]()
    im.save(f"{kind}/f{i:04d}.png")
