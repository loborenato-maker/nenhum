from PIL import Image, ImageDraw, ImageFont
W,H=1200,900
BG=(22,34,32); GOLD=(201,168,112); CREAM=(240,233,220); MUTED=(170,178,172)
img=Image.new("RGB",(W,H),BG); d=ImageDraw.Draw(img)
# subtle gradient
for y in range(H):
    t=y/H; c=tuple(int(BG[i]*(1-t*0.35)+ (10,16,15)[i]*t*0.35) for i in range(3)); d.line([(0,y),(W,y)],fill=c)
F="/usr/share/fonts/opentype/inter/"
f=lambda n,s: ImageFont.truetype(F+n,s)
SERIF="/usr/share/fonts/truetype/crosextra/Caladea-Bold.ttf"
import os
if not os.path.exists(SERIF):
    import glob; SERIF=(glob.glob("/usr/share/fonts/**/Caladea-Bold.ttf",recursive=True) or [F+"InterDisplay-Bold.otf"])[0]
M=80
d.text((M,70),"SAÚDE HORMONAL MASCULINA",font=f("Inter-SemiBold.otf",22),fill=GOLD,spacing=4)
d.line([(M,110),(M+90,110)],fill=GOLD,width=3)
ts=ImageFont.truetype(SERIF,64)
y=140
for line in ["Testosterona baixa:","sinais que merecem","investigação"]:
    d.text((M,y),line,font=ts,fill=CREAM); y+=74
y+=30
items=["Cansaço persistente e pouca energia","Queda de libido e de disposição","Perda de força e de massa muscular","Aumento de gordura abdominal","Alterações de humor, foco e sono"]
fi=f("Inter-Regular.otf",30)
for it in items:
    d.ellipse([M,y+11,M+14,y+25],fill=GOLD)
    d.text((M+34,y),it,font=fi,fill=CREAM); y+=50
y+=22
d.text((M,y),"Reposição só com diagnóstico: sintomas + exames + avaliação médica.",font=f("Inter-Medium.otf",24),fill=MUTED)
# footer
d.line([(M,H-110),(W-M,H-110)],fill=(60,74,70),width=1)
d.text((M,H-85),"CLÍNICA SCULPTÉ",font=f("Inter-SemiBold.otf",26),fill=GOLD)
d.text((M,H-50),"Jardim Paulista · São Paulo",font=f("Inter-Regular.otf",20),fill=MUTED)
r="Dr. Renato Lobo · Médico pela USP"; fr=f("Inter-Regular.otf",22)
d.text((W-M-d.textlength(r,font=fr),H-70),r,font=fr,fill=CREAM)
out=os.path.join(os.path.dirname(os.path.abspath(__file__)),"testosterona-baixa-sintomas-gmb-v2.jpg")
img.save(out,quality=92); print(out, os.path.getsize(out))
