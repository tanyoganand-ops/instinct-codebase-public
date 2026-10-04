from r import *
INK=(44,42,64); PEACH=(246,192,164); BLUE=(170,190,238); TERRA=(150,62,34); DBLUE=(38,62,150)
CREAM=(250,245,238); NAVY=(52,56,100)
Y0=230; BH=1090
CX=468
def light(t):
    return norm([-0.42+0.32*math.sin(2*math.pi*t/11+0.4)+0.22*bell(t,1.2,2.7), -0.58+0.10*math.sin(2*math.pi*t/7.3), 0.72])
def vals(t):
    if t<6.8:
        u=eout(seg(t,3.5,4.9)); return 64*u,57*u
    u=eio(seg(t,6.8,8.0)); return lerp(64,71,u),lerp(57,78,u)
BR=36
def ball_pos(t):
    v1,v2=vals(t)
    p1=(76+8*v1+30,896); p2=(76+8*v2+30,976)
    g=(CX,884); pill=(700,917)
    lift=0;sx=sy=1.0
    if t<7.9: x,y=p1
    elif t<8.6:
        u=eio(seg(t,7.9,8.6)); x=lerp(p1[0],p2[0],u); y=lerp(p1[1],p2[1],u); lift=70*math.sin(math.pi*u)
        y-=lift
        if u>0.93: pass
    elif t<10.9: x,y=p2
    elif t<11.7:
        u=eio(seg(t,10.9,11.7)); x=lerp(p2[0],g[0],u); y=lerp(p2[1],g[1],u)-60*math.sin(math.pi*u); lift=60*math.sin(math.pi*u)
    elif t<13.3:
        x,y=g
    elif t<13.95:
        u=eio(seg(t,13.3,13.95)); x=lerp(g[0],pill[0],u); y=lerp(g[1],pill[1],u)-110*math.sin(math.pi*u); lift=110*math.sin(math.pi*u)+(1-u)*0
    else:
        s=t-13.95; x,y=pill; y-= abs(math.sin(s*5.5))*20*math.exp(-s*1.6)  # settle bounces
        lift=abs(math.sin(s*5.5))*20*math.exp(-s*1.6)
    # landing squash
    for tl in (8.6,11.7,13.95):
        d=t-tl
        if 0<=d<0.25:
            q=math.sin(math.pi*d/0.25)*0.14; sy=1-q; sx=1+q*0.7
    # drop-in
    a=1.0
    if t<5.9:
        sp=spring(t,5.0); y=y-110*(1-sp); a=seg(t,5.0,5.25)
        if t<5.0: a=0
    return x,y,lift,sx,sy,a
def frame(t):
    L=light(t)
    yaw=1.6*math.sin(2*math.pi*t/7.0)-4.2*bell(t,6.4,7.7)+4.2*bell(t,10.4,11.7)
    pitch=0.9*math.sin(2*math.pi*t/5.3)
    base=Layer(Y0,BH); top=Layer(Y0,BH)
    # ---- rail
    ra=seg(t,3.0,3.6)
    if ra>0:
        oy=26*(1-eout(ra))
        base.clay(816,112,30,7,(244,246,252),L,56,1136+oy,elev=6,alpha=ra*0.6,dome=2,seed=11,gs=0.8,spec=0.1)
        # glass hairlines
        hl=np.zeros((2,816-60),np.float32)+1
        base.over(np.ones((2,756,3),np.float32),hl,86,1138+oy,ra*0.8)
        base.over(np.ones((2,756,3),np.float32),hl,86,1245+oy,ra*0.6)
        base.text("Artificial Analysis - 30 Sep 2026",ANTON,48,(74,70,96),L,CX,1170+oy,alpha=ra,gs=0.5,shadow=False)
        base.text("Sonnet Max / Argon High",ANTON,48,(74,70,96),L,CX,1222+oy,alpha=ra,gs=0.5,shadow=False)
    # ---- tiles
    ty=lerp(lerp(520,390,ss(seg(t,2.7,3.5))),560,ss(seg(t,10.5,11.4)))
    th=lerp(lerp(300,420,ss(seg(t,2.7,3.5))),240,ss(seg(t,10.5,11.4)))
    sc_v=vals(t)
    for i,(tx,col,name,sub,logo,scol,sub_c) in enumerate([
        (56,PEACH,"SONNET 5.5","MAX",'c',TERRA,(100,60,50)),
        (484,BLUE,"GEMINI 4","ARGON HIGH",'g',DBLUE,(48,60,110))]):
        t0=0.0+0.22*i
        sp=spring(t,t0); a=seg(t,t0,t0+0.3)
        bob=4.5*math.sin(2*math.pi*(t/2.8+0.35*i))
        y=ty-300*(1-sp)+bob
        base.clay(388,int(th),44,26,col,L,tx,y,elev=26,alpha=a,dome=10,seed=5+i,spec=0.05)
        base.clay(344,96,28,12,CREAM,L,tx+22,y+22,alpha=a,recess=True,seed=20+i,gs=0.9)
        base.decal(LOGO[logo],tx+194,y+70,a)
        base.text(name,ANTON,56,INK,L,tx+194,y+160,alpha=a,gs=0.9,shadow=False)
        sa=a*(1-seg(t,10.5,10.9))
        base.text(sub,ANTON,48,sub_c,L,tx+194,y+214,alpha=sa,gs=0.9,shadow=False)
        scal=seg(t,3.4,3.9)*(1-seg(t,10.5,10.9))
        if scal>0:
            v=sc_v[i]; base.text(str(int(round(v))),ANTON,128,scol,L,tx+194,y+332,alpha=scal,gs=1.2,elev=8)
    # ---- trough + bars
    tra=seg(t,3.6,4.1)*(1-seg(t,10.5,10.9))
    if tra>0:
        oy=30*(1-eout(seg(t,3.6,4.3)))
        base.clay(816,172,40,16,(228,226,238),L,56,850+oy,alpha=tra,recess=True,seed=31,gs=0.8)
        for i,(bc,v) in enumerate([((236,148,110),sc_v[0]),((112,144,232),sc_v[1])]):
            ln=max(8*v,10)
            ba=tra*seg(t,3.9,4.3)
            base.clay(int(ln+30),56,28,22,bc,L,76-8+0,868+80*i+oy,elev=12,alpha=ba,dome=6,seed=40+i,spec=0.06)
    # ---- top layer text
    def drop_text(txt,fp,size,color,cy,tin,tout,dur_out=0.45,spring_in=True,gs=1.5,cx=CX,off=170):
        a=1.0;oy=0;bl=0
        if t<tin: return
        sp=spring(t,tin); oy=-off*(1-sp); a=seg(t,tin,tin+0.25)
        if tout is not None and t>tout:
            u=seg(t,tout,tout+dur_out); oy+=55*eio(u); a*=1-u; bl=9*u
        if a<=0.01: return
        top.text(txt,fp,size,color,L,cx,cy+oy+1.5*math.sin(2*math.pi*(t/3.1)),alpha=a,gs=gs,blur=bl)
    drop_text("Sonnet 5.5",BOLD,76,INK,340,0.45,2.6)
    drop_text("vs Gemini 4",BOLD,76,INK,426,0.62,2.7,off=45)
    drop_text("TERMINAL-BENCH 4.0",ANTON,60,INK,336,3.1,6.4)
    drop_text("AUTOMATIONBENCH-AA",ANTON,60,INK,336,6.9,10.4)
    def tag(txt,col,tin,tout):
        if t<tin: return
        sp=spring(t,tin); a=seg(t,tin,tin+0.2); oy=-90*(1-sp); bl=0
        if t>tout:
            u=seg(t,tout,tout+0.4); oy+=40*eio(u); a*=1-u; bl=8*u
        if a<=0.01: return
        a_,h_,w_,hh_,p_=textmask(txt,ANTON,64)
        w=int(w_-2*p_+110)
        y=1076+oy
        top.clay(w,84,42,26,col,L,CX-w/2,y-42,elev=18,alpha=a,dome=6,seed=61)
        top.text(txt,ANTON,64,INK,L,CX,y+2,alpha=a,gs=0.9,shadow=False,blur=bl)
    tag("SONNET LEADS",PEACH,5.5,6.4)
    tag("GEMINI LEADS",BLUE,8.6,10.4)
    # verdict
    drop_text("DIFFERENT TESTS.",ANTON,72,NAVY,336,11.0,None,gs=1.6)
    drop_text("DIFFERENT WINNERS.",ANTON,72,NAVY,424,11.25,None,gs=1.6,off=45)
    # CTA pill
    if t>12.4:
        sp=spring(t,12.4); a=seg(t,12.4,12.65)
        sq=0
        d=t-13.95
        if 0<=d<0.4: sq=math.sin(math.pi*min(d/0.4,1))*0.07
        br=0.012*math.sin(2*math.pi*t/2.2)
        h=112*(1-sq+br); cy=1005-110*(1-sp)+ (112-h)/2
        top.clay(560,int(h),int(h/2),34,NAVY,L,CX-280,cy-h/2,elev=22,alpha=a,dome=8,seed=71,spec=0.07)
        top.text("COMMENT VIDEO",ANTON,64,CREAM,L,CX,cy+2,alpha=a,gs=0.9,shadow=False)
    # ball
    if t>=5.0:
        x,y,lift,sx,sy,a=ball_pos(t)
        if a>0:
            top.ball(x,y,BR,L,alpha=a,elev=6+lift*0.9,sx=sx,sy=sy)
    # ---- warp & composite
    bg=bg_frame(L,t)
    def warp(layer,yw,pt,dx,dy):
        arr=np.clip(layer.a*255+0.5,0,255).astype(np.uint8)
        im=Image.fromarray(arr,'RGBA')
        co=persp_coeffs(yw,pt,CX,768-Y0,W_=W,H_=BH)
        im=im.transform((W,BH),Image.PERSPECTIVE,tuple(co),Image.BICUBIC)
        a=np.asarray(im,np.float32)/255
        if dx or dy:
            a=np.roll(a,(int(round(dy)),int(round(dx))),axis=(0,1))
        return a
    wb=warp(base,yaw,pitch,0,0)
    wt=warp(top,yaw*1.0,pitch,-yaw*5.0,-pitch*3.0)
    out=bg
    sl=out[Y0:Y0+BH]
    sl=wb[...,:3]*255+sl*(1-wb[...,3:])
    sl=wt[...,:3]*255+sl*(1-wt[...,3:])
    out[Y0:Y0+BH]=sl
    return Image.fromarray(np.clip(out+0.5,0,255).astype(np.uint8))
if __name__=='__main__':
    import time
    ts=[float(x) for x in sys.argv[1:]]
    ims=[]
    for t in ts:
        t0=time.time(); im=frame(t); print(t,time.time()-t0); ims.append(im.resize((360,640)))
    sheet=Image.new('RGB',(360*len(ims),640))
    for i,im in enumerate(ims): sheet.paste(im,(i*360,0))
    sheet.save('/tmp/b/sheet.png')
