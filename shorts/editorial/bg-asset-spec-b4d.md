# B4d depth-lane bg asset spec (replicable)
Canvas 1080x1920, 30fps, 450 frames. Page is a pure function of t (index.html seek(t)). Base bg #f4f4f2 with two static washes: ellipse 900x700 at 20%/15% #e6eef6 and ellipse 900x800 at 85%/80% #f6e9e8. Nothing in the bg drifts except the lane props.

## Lane motion (all right to left, wrap)
x_left = 1080 - ((x0 + speed*t) mod (1080 + w)); y = y0 + bob*sin(2pi t/3.1 + ph); rotation = tilt + 0.5deg*sin(1.7t+ph).
depth zoom: prog=(x0+speed*t mod P)/P; fore scale = .55 + .70*sin(pi*prog); mid scale = .80 + .32*sin(pi*prog); back 1.0.
- back: speed 120px/s, blur 1.6px, opacity .42, z under story, bob 8
- mid: speed 270px/s, blur 0, opacity 1, z under story cards, bob 14
- fore: speed 620px/s, blur 6px, opacity .80, z over story, bob 10; centres kept above y~140 or below y~1400 so they never cover text
ph is a seeded value (LCG seed 7, see index.html R()).

## Assets (kind,size px,y0,x0)
back (clay CSS shapes, pastel palette): sphere 90,160,0 (blue, palette idx1) / pill 90,980,900 (peach, idx0) / cube 80,1180,500 (blue, idx3) / sphere 110,1380,0 (blue, idx1) / cube 90,1600,640 (rose, idx5) / sphere 100,420,1300 (butter, idx4). All with animation `pulse`.
mid: sphere PNG 190,360,0 anim squash / donut PNG 230,1010,700 anim wobble / terminal chip 170,760,350 (tilt -6, anim hop + cursor blink) / Claude lockup chip 110,170,500 / Gemini lockup chip 110,1700,1100 / bars chip 150,1560,200 (tilt 6, anim hop2 + bar heights pulse).
fore: sphere PNG 280,40,0 anim squash / pill 230,1440,250 anim wave / donut PNG 400,1620,500 anim wobble.

## Colours
- Sphere PNG recoloured purple to blue: hue shift -0.18 (HSV), result approx #8FB4EA clay blue.
- Donut PNG recoloured green to light orange: hue shift -0.295, saturation x1.45, value x1.15, result approx #F2AE80.
- Clay CSS palette [light, mid, shade]: peach #fbd9c8/#f0b79b/#d99879; blue #cfe0f8/#9cbcec/#7a9bd2 (replaced the old lilac); mint #d4eddf/#acd8bf/#86bb9e; butter #fbf0bd/#f1dc8a/#d8bf62; rose #f8d3de/#eeb0c3/#d38ea5. Fill radial-gradient(circle at 30% 26%, light 0, mid 58%, shade 130%) plus soft drop and inset shadows.
Source PNGs: assets/orig-sphere.png, orig-donut.png (v11b bank), recoloured clay-sphere.png, clay-donut.png.

## Animations (applied to the inner element, origin bottom centre for hop/squash, centre otherwise)
- hop (period 2.3s, jump 55px, land squash 10%/13% x/y over 13% of the cycle, stretch 4%/7% in air): terminal chip. Extra: cursor underscore opacity .2+.8*(.5+.5 sin(5.5t)).
- hop2 (2.7s, 45px): bars chip; its three bars re-height each frame h=18+36*(.5+.5 sin(2.6t + 1.4i)), y=82-h in a 100 viewBox.
- squash (1.8s, jump = .22*width, squash/stretch x1.2): spheres.
- wobble: perspective(700px) rotateX(20deg*sin(1.3t+ph)) rotateY(26deg*sin(.9t+1.7ph)): donuts. A wobble, not a spin.
- wave: skewX(9deg*sin(2t+ph)) scaleY(1+.08 sin(4t+ph)): fore pill.
- pulse: scale(1+.07 sin(2t+ph)): back shapes.
