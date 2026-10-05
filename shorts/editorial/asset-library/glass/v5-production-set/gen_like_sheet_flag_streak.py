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
def lerp_keys(keys,t):
    for (t0,*a),(t1,*b) in zip(keys,keys[1:]):
        if t<=t1:
            u=(t-t0)/(t1-t0) if t1>t0 else 1;u=(1-np.cos(u*np.pi))/2
            return [x+(y-x)*u for x,y in zip(a,b)]
    return keys[-1][1:]
def whip(i,N):
    t=i/(N-1);p=back(t)  # slight overshoot past, comes back; band travels -500 -> W+500
    cx=-500+(W+1000)*min(p,1.0) if p<=1 else W+500-(p-1)*0
    cx=-500+(W+1000)*t**0.9 if False else -500+(W+1000)*eio(t)*1.0
    xs=np.arange(W)[None,:].astype(np.float32);ys=np.arange(H)[:,None].astype(np.float32)
    g=np.exp(-((xs-cx)/230)**2)                       # soft band
    tail=np.exp(-np.clip(cx-xs,0,None)/600)/(1+np.exp(-(cx-xs)/60))      # trailing smear
    streak=0.92+0.08*np.sin(ys/23.0+t*9)
    a=np.clip((g*0.85+tail*0.35)*streak,0,1)*min(1,t*10,(1-t)*10)
    arr=np.zeros((H,W,4),np.uint8);arr[...,0]=235;arr[...,1]=242;arr[...,2]=255;arr[...,3]=(a*200).astype(np.uint8)
    return Image.fromarray(arr,"RGBA")
def iris(i,N):
    t=i/(N-1);R=1250*eio(t) if True else 0
    S=2
    im=Image.new("RGBA",(W,H),(0,0,0,0));
    if R<=1:return im
    def f(d,S):
        cx,cy=W/2*S,H/2*S
        d.ellipse([cx-R*S,cy-R*S,cx+R*S,cy+R*S],fill=(255,255,255,255))
    disc=aa(f,(W,H))
    # glass rim ring just outside edge
    def g(d,S):
        cx,cy=W/2*S,H/2*S
        d.ellipse([cx-(R+34)*S,cy-(R+34)*S,cx+(R+34)*S,cy+(R+34)*S],outline=(255,255,255,170),width=34*S)
        d.ellipse([cx-(R+4)*S,cy-(R+4)*S,cx+(R+4)*S,cy+(R+4)*S],outline=(255,255,255,240),width=4*S)
    ring=aa(g,(W,H))
    return Image.alpha_composite(ring,disc)
def clay(i,N):
    t=i/(N-1);c=Image.new("RGBA",(W,H),(0,0,0,0))
    base=1320  # bottom edge target
    keys=[(0,base+700,0.9,1.18),(.30,base-120,0.9,1.15),(.46,base,1.18,0.80),(.62,base-70,0.95,1.06),(.78,base,1.08,0.92),(1,base,1,1)]
    bot,sx,sy=lerp_keys(keys,t)
    w0=h0=440;w=int(w0*sx);h=int(h0*sy)
    S=2
    m=Image.new("L",(w*S,h*S),0);ImageDraw.Draw(m).rounded_rectangle([0,0,w*S-1,h*S-1],110*S,fill=255)
    yy=np.linspace(0,1,h*S)[:,None];xx=np.linspace(0,1,w*S)[None,:]
    col=np.zeros((h*S,w*S,4),np.uint8)
    shade=1-0.18*yy-0.06*xx
    hl=np.exp(-(((xx-.3)**2+(yy-.22)**2)/0.03))*0.22
    base_c=np.array([236,170,138],np.float32)
    for k in range(3):col[...,k]=np.clip(base_c[k]*shade+255*hl,0,255).astype(np.uint8)
    col[...,3]=255
    p=Image.composite(Image.fromarray(col,"RGBA"),Image.new("RGBA",m.size,(0,0,0,0)),m).resize((w,h),Image.LANCZOS)
    x=(W-w)//2;y=int(bot-h)
    # contact shadow on ground (shrinks with height)
    air=max(0,(base-bot)/300)
    sh=Image.new("RGBA",(W,H),(0,0,0,0));sd=ImageDraw.Draw(sh)
    sw=int(w0*0.9*(1-0.3*min(air,1)));sd.ellipse([W//2-sw//2,base-18,W//2+sw//2,base+30],fill=(90,60,50,int(90*(1-0.6*min(air,1)))))
    c=Image.alpha_composite(c,sh.filter(ImageFilter.GaussianBlur(18)))
    t2=Image.new("RGBA",(W,H),(0,0,0,0));t2.paste(p,(x,y));return Image.alpha_composite(c,t2)
def bellsprite(sz=120):
    S=3
    im=Image.new("RGBA",(sz*S,sz*S),(0,0,0,0));d=ImageDraw.Draw(im);c=sz*S//2;col=(110,150,245,255);u=S*sz/120
    d.pieslice([c-34*u,c-46*u,c+34*u,c+22*u],180,360,fill=col)
    d.polygon([(c-34*u,c-12*u),(c+34*u,c-12*u),(c+46*u,c+22*u),(c-46*u,c+22*u)],fill=col)
    d.ellipse([c-10*u,c+22*u,c+10*u,c+40*u],fill=col)
    d.ellipse([c-7*u,c-56*u,c+7*u,c-42*u],fill=col)
    return im.resize((sz,sz),Image.LANCZOS)
def bell(i,N):
    t=i/(N-1);c=Image.new("RGBA",(W,H),(0,0,0,0))
    w,h=300,110;x=W-w-50;yt=H-260
    if t<.15: y=yt+260*(1-back(t/.15))+0;al=min(1,t/.08)
    elif t<.88: y=yt;al=1
    else: u=eio((t-.88)/.12);y=yt+260*u;al=1-u
    if t<=0.0 or al<=0:return c
    pill=tint(panel(w,h,55,sheen=-1),(120,160,255))
    dd=ImageDraw.Draw(pill);dd.ellipse([22,h//2-34,90,h//2+34],fill=(255,255,255,235))
    # ring: two decaying swings
    ang=0
    for s0 in (.25,.52):
        if s0<=t<s0+.22:
            u=(t-s0)/.22;ang=16*np.exp(-u*2.2)*np.sin(u*np.pi*4)
    sp=bellsprite(70).rotate(ang,resample=Image.BICUBIC,center=(35,8))
    pill.alpha_composite(sp,(56-35+0,h//2-35+2)) if False else pill.alpha_composite(sp,(22+34-35,h//2-35))
    return put(c,pill,x,int(y),al)

def bar(i,N):
    SH=140;t=i/(N-1);f=min(t/(14/15),1);f=f  # linear fill over 14 s, full for last second
    x0,x1,y,h=60,1020,60,18
    def g(d,S):
        d.rounded_rectangle([x0*S,y*S,x1*S,(y+h)*S],h*S//2,fill=(255,255,255,90),outline=(255,255,255,200),width=2*S)
        xe=x0+(x1-x0)*f
        if xe-x0>h:
            d.rounded_rectangle([x0*S,y*S,xe*S,(y+h)*S],h*S//2,fill=(110,150,245,240))
            d.rounded_rectangle([(x0+6)*S,(y+3)*S,(xe-6)*S,(y+7)*S],2*S,fill=(255,255,255,110))
        elif f>0:
            d.ellipse([x0*S,y*S,(x0+max(f*(x1-x0),h*0.6))*S,(y+h)*S],fill=(110,150,245,240))
    im=aa(g,(W,SH))
    sh=Image.new("RGBA",(W,SH),(0,0,0,0));return im
def bubble(i,N):
    t=i/(N-1);c=Image.new("RGBA",(W,H),(0,0,0,0))
    w,h=300,210
    p=Image.new("RGBA",(w,h+50),(0,0,0,0))
    body=panel(w,h,70,sheen=-1);p.alpha_composite(body,(0,0))
    def tail(d,S):
        d.polygon([(60*S,(h-8)*S),(130*S,(h-8)*S),(48*S,(h+46)*S)],fill=(255,255,255,120))
        d.line([(60*S,(h-4)*S),(48*S,(h+46)*S),(130*S,(h-4)*S)],fill=(255,255,255,200),width=3*S)
    p=Image.alpha_composite(p,aa(tail,p.size))
    def q(d,S):
        cx,cy=w//2,h//2-6;col=(110,150,245,255)
        d.arc([(cx-34)*S,(cy-58)*S,(cx+34)*S,(cy+10)*S],180,40,fill=col,width=16*S)
        d.line([(cx+24)*S,(cy-6)*S,(cx)*S,(cy+22)*S,(cx)*S,(cy+34)*S],fill=col,width=16*S,joint="curve")
        d.ellipse([(cx-10)*S,(cy+50)*S,(cx+10)*S,(cy+70)*S],fill=col)
    p=Image.alpha_composite(p,aa(q,p.size))
    u=min(t/.2,1);sc=0.15+0.85*back(u);al=min(1,t/.08)
    ang=0
    if t>.25: ang=5*np.exp(-(t-.25)*5)*np.sin((t-.25)*np.pi*9)
    p=p.rotate(ang,resample=Image.BICUBIC,center=(60,h+20),expand=False)
    return put(c,p,70,1110,al,max(sc,.05))
def hookcard(i,N):
    t=i/(N-1);c=Image.new("RGBA",(W,H),(0,0,0,0))
    w,h=580,780;p=panel(w,h,70,sheen=t*1.6-.3)
    def z(d,S):
        d.rounded_rectangle([60*S,70*S,(w-60)*S,430*S],50*S,fill=(255,255,255,120),outline=(255,255,255,220),width=3*S)
    p=Image.alpha_composite(p,aa(z,p.size))
    d=ImageDraw.Draw(p)
    for k,wd in enumerate([.8,.55]):d.rounded_rectangle([60,500+k*60,60+int((w-120)*wd),500+k*60+22],11,fill=(255,255,255,170))
    ex=ease(t/.3);x=int(W+60-(W+60-(W-w-50))*ex)
    return put(c,p,x,540,min(1,t/.1),1)
def bm(filled):
    w,h=200,280
    def f(d,S):
        pts=[(14,6),(w-14,6),(w-14,h-8),(w//2,h-78),(14,h-8)]
        pts=[(a*S,b*S) for a,b in pts]
        if filled:
            d.polygon(pts,fill=(110,150,245,255));d.polygon([(34*S,24*S),(70*S,24*S),(70*S,150*S),(34*S,150*S)],fill=(255,255,255,70))
        else:
            d.line(pts+[pts[0]],fill=(110,150,245,255),width=16*S,joint="curve")
    return aa(f,(w,h))
def save(i,N):
    t=i/(N-1);c=Image.new("RGBA",(W,H),(0,0,0,0))
    cx,cy=W//2,1250
    o,fl=bm(False),bm(True)
    if t<.15: u=back(t/.15);sc=0.3+0.7*u;sx=1;img=o;al=min(1,t/.06)
    elif t<.42:
        u=(t-.15)/.27;sx=max(abs(np.cos(u*np.pi)),0.04);img=o if u<.5 else fl;sc=1+0.1*np.sin(u*np.pi);al=1
    elif t<.62:
        u=(t-.42)/.2;img=fl;sx=1;al=1;sc=1+0.22*np.exp(-u*4)*np.cos(u*np.pi*3)
    else: img=fl;sx=1;al=1;sc=1
    # glow pulse after fill
    if t>=.42:
        pul=0.5+0.5*np.sin((t-.42)*np.pi*5)
        gl=Image.new("RGBA",(W,H),(0,0,0,0));m=Image.new("L",(W,H),0);m.paste(fl.split()[3],(cx-100,cy-140))
        m=m.filter(ImageFilter.GaussianBlur(40));arr=np.zeros((H,W,4),np.uint8);arr[...,0]=120;arr[...,1]=160;arr[...,2]=255
        arr[...,3]=(np.array(m).astype(np.float32)*(0.35+0.5*pul)).clip(0,255).astype(np.uint8);c=Image.fromarray(arr,"RGBA")
    w,h=img.size;im2=img.resize((max(2,int(w*sx*sc)),int(h*sc)),Image.LANCZOS)
    x=cx-im2.size[0]//2;y=cy-im2.size[1]//2
    return put(c,im2,x,y,al,1,shadow=False)

def spring(t,k=7.0):  # damped overshoot 0->1
    t=min(max(t,0),1);return 1-np.exp(-5*t)*np.cos(k*t)
def quiz(i,N):
    t=i/(N-1);c=Image.new("RGBA",(W,H),(0,0,0,0))
    w,h=900,150
    for k in range(3):
        s0=.05+k*.12;u=min(max((t-s0)/.25,0),1)
        if u<=0:continue
        p=panel(w,h,60,sheen=-1)
        def lz(d,S,h=h):
            d.rounded_rectangle([26*S,(h//2-45)*S,116*S,(h//2+45)*S],30*S,fill=(255,255,255,200),outline=(110,150,245,255),width=4*S)
            d.rounded_rectangle([150*S,(h//2-11)*S,640*S,(h//2+11)*S],11*S,fill=(255,255,255,150))
        p=Image.alpha_composite(p,aa(lz,p.size))
        x=int(-w-40+((W-w)//2+w+40)*back(u));c=put(c,p,x,900+k*170,min(1,u*4))
    return c
def flip(i,N):
    t=i/(N-1);c=Image.new("RGBA",(W,H),(0,0,0,0))
    w,h=620,760
    u=min(max((t-.2)/.55,0),1);ang=np.pi*back(u) if u>0 else 0
    cs=np.cos(ang);face_front=cs>=0
    if face_front:
        p=panel(w,h,70,sheen=0.5)
        def z(d,S):d.rounded_rectangle([70*S,90*S,(w-70)*S,420*S],50*S,fill=(255,255,255,120),outline=(255,255,255,220),width=3*S)
        p=Image.alpha_composite(p,aa(z,p.size))
    else:
        S=2;m=Image.new("L",(w*S,h*S),0);ImageDraw.Draw(m).rounded_rectangle([0,0,w*S-1,h*S-1],70*S,fill=255)
        yy=np.linspace(0,1,h*S)[:,None];xx=np.linspace(0,1,w*S)[None,:]
        col=np.zeros((h*S,w*S,4),np.uint8);sh=1-0.16*yy-0.05*xx;hl=np.exp(-(((xx-.3)**2+(yy-.2)**2)/0.04))*0.2
        for k,b in enumerate((236,170,138)):col[...,k]=np.clip(b*sh+255*hl,0,255).astype(np.uint8)
        col[...,3]=255
        p=Image.composite(Image.fromarray(col,"RGBA"),Image.new("RGBA",m.size,(0,0,0,0)),m).resize((w,h),Image.LANCZOS)
        def z(d,S):d.rounded_rectangle([70*S,90*S,(w-70)*S,420*S],50*S,fill=(255,255,255,70),outline=(255,255,255,200),width=3*S)
        p=Image.alpha_composite(p,aa(z,p.size))
    sx=max(abs(cs),0.03);sy=1+0.05*(1-abs(cs))
    p2=p.resize((max(2,int(w*sx)),int(h*sy)),Image.LANCZOS)
    al=min(1,t/.1);x=(W-p2.size[0])//2;y=900-p2.size[1]//2
    return put(c,p2,x,y,al,1)
def rating(i,N):
    t=i/(N-1);c=Image.new("RGBA",(W,H),(0,0,0,0))
    x0,x1,y,h=140,940,1250,40
    f=0;pulse=0
    for k in range(5):
        s0=.18+k*.14;u=(t-s0)/.12
        if u>=0:
            f=(k)/5+0.2*back(min(u,1))
            if 0<u<1:pulse=np.sin(u*np.pi)
    al=min(1,t/.1)
    def g(d,S):
        d.rounded_rectangle([x0*S,y*S,x1*S,(y+h)*S],h*S//2,fill=(240,205,185,140),outline=(255,255,255,200),width=2*S)
        for k in range(1,5):
            xk=x0+(x1-x0)*k/5;d.line([xk*S,(y+8)*S,xk*S,(y+h-8)*S],fill=(255,255,255,170),width=2*S)
        xe=x0+(x1-x0)*min(max(f,0),1.04)
        if xe-x0>2:
            hh=h+int(8*pulse)
            d.rounded_rectangle([x0*S,(y-(hh-h)//2)*S,xe*S,(y+h+(hh-h)//2)*S],hh*S//2,fill=(230,160,125,255))
            d.rounded_rectangle([(x0+8)*S,(y+6)*S,max(xe-8,x0+9)*S,(y+14)*S],4*S,fill=(255,255,255,90))
    im=aa(g,(W,H))
    if al<1:
        a=np.array(im);a[...,3]=(a[...,3]*al).astype(np.uint8);im=Image.fromarray(a,"RGBA")
    return im
def tab(i,N):
    t=i/(N-1);c=Image.new("RGBA",(W,H),(0,0,0,0))
    w,h=340,60;p=panel(w,h,30,sheen=-1)
    def d_(d,S):d.rounded_rectangle([22*S,(h//2-10)*S,(w-22)*S,(h//2+10)*S],10*S,fill=(255,255,255,170))
    p=Image.alpha_composite(p,aa(d_,p.size))
    u=min(t/.4,1);y=int(-100+(90+100)*spring(u)) if t>0.0 else -200
    return put(c,p,60,y,min(1,t/.06),1)

BL=(110,150,245,255)
def claypanel(w,h,rad):
    S=2;m=Image.new("L",(w*S,h*S),0);ImageDraw.Draw(m).rounded_rectangle([0,0,w*S-1,h*S-1],rad*S,fill=255)
    yy=np.linspace(0,1,h*S)[:,None];xx=np.linspace(0,1,w*S)[None,:]
    col=np.zeros((h*S,w*S,4),np.uint8);sh=1-0.16*yy-0.05*xx;hl=np.exp(-(((xx-.3)**2+(yy-.2)**2)/0.04))*0.2
    for k,b in enumerate((236,170,138)):col[...,k]=np.clip(b*sh+255*hl,0,255).astype(np.uint8)
    col[...,3]=255
    return Image.composite(Image.fromarray(col,"RGBA"),Image.new("RGBA",m.size,(0,0,0,0)),m).resize((w,h),Image.LANCZOS)
def swipe(i,N):
    t=i/(N-1);c=Image.new("RGBA",(W,H),(0,0,0,0))
    cx=975;d0=110
    def chev(d,S):
        d.line([(d0//2-22)*S*0+ (60-22)*S,(66)*S,60*S,(44)*S,(60+22)*S,66*S],fill=BL,width=10*S,joint="curve")
        d.line([60*S,44*S,60*S,80*S],fill=BL,width=10*S)
    base=panel(120,120,60,sheen=-1);base=Image.alpha_composite(base,aa(chev,(120,120)))
    u=min(max((t-.1)/.7,0),1);y=1320-330*ease(u)
    al=min(1,t/.12)*(1-eio((t-.82)/.18))
    for k in range(4,0,-1):  # trail echoes below
        yk=y+k*34;ak=al*(0.22-0.045*k)*min(u*4,1)
        if ak>0:
            ghost=Image.new("RGBA",(120,120),(0,0,0,0));gd=ImageDraw.Draw(ghost);gd.ellipse([20,20,100,100],fill=(120,160,255,255))
            c=put(c,ghost,cx-60,int(yk),ak,1,shadow=False)
    return put(c,base,cx-60,int(y),al)
def mute(i,N):
    t=i/(N-1);c=Image.new("RGBA",(W,H),(0,0,0,0))
    w,h=260,110;p=panel(w,h,55,sheen=-1)
    muted=t>=.45
    def ic(d,S):
        cx,cy=80,h//2
        d.polygon([((cx-26)*S,(cy-10)*S),((cx-10)*S,(cy-10)*S),((cx+10)*S,(cy-28)*S),((cx+10)*S,(cy+28)*S),((cx-10)*S,(cy+10)*S),((cx-26)*S,(cy+10)*S)],fill=BL)
        if not muted:
            d.arc([(cx+2)*S,(cy-18)*S,(cx+34)*S,(cy+18)*S],-50,50,fill=BL,width=7*S)
            d.arc([(cx+8)*S,(cy-30)*S,(cx+52)*S,(cy+30)*S],-50,50,fill=BL,width=7*S)
        else:
            d.line([(cx+22)*S,(cy-14)*S,(cx+50)*S,(cy+14)*S],fill=BL,width=8*S);d.line([(cx+50)*S,(cy-14)*S,(cx+22)*S,(cy+14)*S],fill=BL,width=8*S)
    p=Image.alpha_composite(p,aa(ic,p.size));d=ImageDraw.Draw(p);d.rounded_rectangle([140,h//2-10,w-30,h//2+10],10,fill=(255,255,255,150))
    u=min(t/.25,1);sc=0.3+0.7*back(u);al=min(1,t/.1)
    if .4<t<.7:
        v=(t-.4)/.3;sx=1+0.12*np.sin(v*np.pi*2)*np.exp(-v*1.5);sy=1-0.14*np.sin(v*np.pi*2)*np.exp(-v*1.5)
    else:sx=sy=1
    p2=p.resize((int(w*sx*sc),int(h*sy*sc)),Image.LANCZOS)
    cx0,cy0=760+w//2,170+h//2
    return put(c,p2,cx0-p2.size[0]//2,cy0-p2.size[1]//2,al,1)
def poll(i,N):
    t=i/(N-1);c=Image.new("RGBA",(W,H),(0,0,0,0))
    x0,w,h=140,760,90;rows=[(1010,.62,(110,150,245)),(1130,.38,(236,170,138))]
    for k,(y,pct,col) in enumerate(rows):
        u=(t-.08-k*.08)/.5;g=back(min(max(u,0),1))
        al=min(1,t/.1)
        def f(d,S,y=y,pct=pct,col=col,g=g):
            d.rounded_rectangle([x0*S,y*S,(x0+w)*S,(y+h)*S],45*S,fill=(255,255,255,90),outline=(255,255,255,210),width=3*S)
            ww=max(0,w*pct*g)
            if ww>40:
                d.rounded_rectangle([x0*S,y*S,(x0+ww)*S,(y+h)*S],45*S,fill=col+(235,))
                d.rounded_rectangle([(x0+14)*S,(y+10)*S,(x0+ww-14)*S,(y+22)*S],6*S,fill=(255,255,255,90))
            d.ellipse([(x0+w-84)*S,(y+14)*S,(x0+w-14)*S,(y+h-14)*S],fill=(255,255,255,0))
        c=Image.alpha_composite(c,aa(f,(W,H)))
        # blank pct slot at right end
        sl=Image.new("RGBA",(W,H),(0,0,0,0));ImageDraw.Draw(sl).rounded_rectangle([x0+w-190,y+25,x0+w-30,y+h-25],20,fill=(255,255,255,150));c=Image.alpha_composite(c,sl) if g>0.2 else c
    if t<.1:
        a=np.array(c);a[...,3]=(a[...,3]*min(1,t/.1)).astype(np.uint8);c=Image.fromarray(a,"RGBA")
    return c
def badge2(i,N):
    t=i/(N-1);c=Image.new("RGBA",(W,H),(0,0,0,0))
    w,h=240,110;p=claypanel(w,h,55)
    def sl(d,S):d.ellipse([18*S,(h//2-36)*S,90*S,(h//2+36)*S],fill=(255,255,255,235),outline=(255,255,255,255),width=2*S)
    p=Image.alpha_composite(p,aa(sl,p.size));d=ImageDraw.Draw(p);d.rounded_rectangle([108,h//2-10,w-28,h//2+10],10,fill=(255,255,255,170))
    u=min(t/.3,1);sc=0.2+0.8*back(u);al=min(1,t/.1)
    ang=0
    if t>.3:ang=-6*np.exp(-(t-.3)*6)*np.sin((t-.3)*np.pi*6)
    p=p.rotate(ang,resample=Image.BICUBIC,expand=True)
    p2=p.resize((max(2,int(p.size[0]*sc)),max(2,int(p.size[1]*sc))),Image.LANCZOS)
    cx0,cy0=60+w//2,200+h//2
    return put(c,p2,cx0-p2.size[0]//2,cy0-p2.size[1]//2,al,1)

def heartpts(cx,cy,sz,S):
    ts=np.linspace(0,2*np.pi,120)
    x=16*np.sin(ts)**3;y=-(13*np.cos(ts)-5*np.cos(2*ts)-2*np.cos(3*ts)-np.cos(4*ts))
    k=sz/34.0
    return [((cx+a*k)*S,(cy+b*k)*S) for a,b in zip(x,y)]
def like(i,N):
    t=i/(N-1);c=Image.new("RGBA",(W,H),(0,0,0,0))
    cx,cy=900,400
    # particles
    rng=np.random.RandomState(7)
    if t>.18:
        u=(t-.18)/.8;n=8
        for k in range(n):
            a=2*np.pi*k/n+0.3;dist=40+110*ease(u)*(0.8+0.4*rng.rand());r=int(14-8*u) if k%2==0 else int(10-5*u)
            al=max(0,1-u**1.5)
            col=(236,170,138,255) if k%2==0 else (255,255,255,235)
            pr=Image.new("RGBA",(2*r+2,2*r+2),(0,0,0,0));ImageDraw.Draw(pr).ellipse([1,1,2*r+1,2*r+1],fill=col,outline=(110,150,245,255) if k%2 else None,width=2)
            c=put(c,pr,int(cx+np.cos(a)*dist-r),int(cy+np.sin(a)*dist-r),al,1,shadow=False)
    u=min(t/.25,1);sc=0.2+0.8*back(u)
    if t>.25:sc*=1+0.05*np.exp(-(t-.25)*8)*np.sin((t-.25)*np.pi*10)
    al=min(1,t/.08)
    S=3;hs=150
    def f(d,S):
        pts=heartpts(hs/2+10,hs/2+10,hs,S)
        d.polygon(pts,fill=(255,255,255,150));d.line(pts+[pts[0]],fill=(255,255,255,235),width=4*S,joint="curve")
        d.polygon(heartpts(hs/2+10,hs/2+10,hs*0.62,S),fill=(110,150,245,120))
    hp=aa(f,(hs+20,hs+20))
    hp2=hp.resize((max(2,int((hs+20)*sc)),max(2,int((hs+20)*sc))),Image.LANCZOS)
    return put(c,hp2,cx-hp2.size[0]//2,cy-hp2.size[1]//2,al,1)
def sheet(i,N):
    t=i/(N-1);c=Image.new("RGBA",(W,H),(0,0,0,0))
    w,h=1000,640;p=panel(w,h,70,sheen=t*1.4-.2)
    def f(d,S):
        d.rounded_rectangle([(w//2-50)*S,16*S,(w//2+50)*S,26*S],5*S,fill=(255,255,255,200))
        for k in range(3):
            cx=w//2+(k-1)*300
            d.rounded_rectangle([(cx-75)*S,70*S,(cx+75)*S,220*S],50*S,fill=(255,255,255,170),outline=(255,255,255,235),width=3*S)
            d.rounded_rectangle([(cx-60)*S,246*S,(cx+60)*S,266*S],10*S,fill=(255,255,255,150))
    p=Image.alpha_composite(p,aa(f,p.size))
    u=min(t/.55,1);y=int(1920+40-(1920+40-1380)*spring(u,6.5)) if t>0 else 1960
    return put(c,p,(W-w)//2,y,min(1,t/.06),1)
def flag(i,N):
    t=i/(N-1);c=Image.new("RGBA",(W,H),(0,0,0,0))
    w,h=96,140;cx,cy=140,410
    def mk(filled):
        def f(d,S):
            pts=[(8*S,6*S),((w-8)*S,6*S),((w-8)*S,(h-6)*S),((w//2)*S,(h-38)*S),(8*S,(h-6)*S)]
            if filled:d.polygon(pts,fill=(236,170,138,255));d.polygon([(20*S,18*S),(36*S,18*S),(36*S,80*S),(20*S,80*S)],fill=(255,255,255,80))
            else:d.polygon(pts,fill=(255,255,255,150));d.line(pts+[pts[0]],fill=(255,255,255,240),width=4*S,joint="curve")
        return aa(f,(w,h))
    g,cl=mk(False),mk(True)
    u0=min(t/.2,1);sc=0.3+0.7*back(u0);al=min(1,t/.08)
    if t<.35:img=g;sx=1
    elif t<.55:
        u=(t-.35)/.2;img=g if u<.5 else cl;sx=max(abs(np.cos(u*np.pi)),0.05)
    else:
        img=cl;v=(t-.55)/.45;sx=1;sc*=1+0.18*np.exp(-v*7)*np.cos(v*np.pi*3)  # snap
    i2=img.resize((max(2,int(w*sx*sc)),int(h*sc)),Image.LANCZOS)
    return put(c,i2,cx-i2.size[0]//2,cy-i2.size[1]//2,al,1)
def flame_img(ph):
    w,h=90,120;S=3
    def f(d,S):
        ys=np.linspace(0,1,60)
        sway=6*np.sin(ph)*(1-ys)
        for scale,col,off in ((1,(255,150,60,255),0),(0.6,(255,210,90,255),14)):
            hw=0.5*w*scale*ys**0.9*np.sqrt(np.clip(1-ys**3,0,1))*1.3
            L=[((w/2+sway[k]*scale-hw[k])*S,(off+ (h-off)*ys[k]*(1 if scale==1 else 0.88)*1.0)*S) for k in range(60)]
            R=[((w/2+sway[k]*scale+hw[k])*S,(off+ (h-off)*ys[k]*(1 if scale==1 else 0.88)*1.0)*S) for k in range(60)]
            d.polygon(L+R[::-1],fill=col)
    return aa(f,(w,h))
def streak(i,N):
    t=i/(N-1);c=Image.new("RGBA",(W,H),(0,0,0,0))
    w,h=240,110;p=claypanel(w,h,55)
    d=ImageDraw.Draw(p);d.rounded_rectangle([118,h//2-22,w-26,h//2+22],14,fill=(255,255,255,235))
    u=min(t/.25,1);sc=0.2+0.8*back(u);al=min(1,t/.1)
    ph=t*2*np.pi*4
    fl=flame_img(ph);fs=1+0.06*np.sin(ph*1.7)+0.03*np.sin(ph*3.1)
    fl=fl.resize((int(90*0.8),int(120*0.8*fs)),Image.LANCZOS)
    p.alpha_composite(fl,(22,h//2-fl.size[1]//2+2))
    p2=p.resize((max(2,int(w*sc)),max(2,int(h*sc))),Image.LANCZOS)
    cx0,cy0=540,225
    return put(c,p2,cx0-p2.size[0]//2,cy0-p2.size[1]//2,al,1)
kind=sys.argv[1];N=int(sys.argv[2]);os.makedirs(kind,exist_ok=True)
fn={"like":like,"sheet":sheet,"flag":flag,"streak":streak}[kind]
for i in range(N):fn(i,N).save(f"{kind}/f{i:04d}.png")
