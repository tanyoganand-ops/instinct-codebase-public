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
kind=sys.argv[1];N=int(sys.argv[2]);os.makedirs(kind,exist_ok=True)
for i in range(N):frame(kind,i,N).save(f"{kind}/f{i:04d}.png")
