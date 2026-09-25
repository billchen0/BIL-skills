from pathlib import Path
import shutil, subprocess, sys
from PIL import Image, ImageDraw
root=Path(__file__).resolve().parents[1]; out=root/'qa/rendered'; out.mkdir(parents=True,exist_ok=True)
lo=shutil.which('libreoffice') or shutil.which('soffice')
if not lo:
    print('LibreOffice not found. Skipping rendering; install LibreOffice and rerun to create qa/rendered and qa/contact-sheet.png.')
    sys.exit(0)
for deck in [root/'templates/lab-meeting-slide-library.pptx',root/'examples/lab-meeting-slide-library-demo.pptx']:
    target=out/deck.stem; target.mkdir(exist_ok=True)
    subprocess.run([lo,'--headless','--convert-to','pdf','--outdir',str(target),str(deck)],check=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    pdftoppm=shutil.which('pdftoppm')
    if pdftoppm:
        subprocess.run([pdftoppm,'-png',str(target/(deck.stem+'.pdf')),str(target/'slide')],check=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
images=list(out.glob('**/*.png'))
if images:
    thumbs=[]
    for p in images:
        im=Image.open(p).convert('RGB'); im.thumbnail((320,180)); thumbs.append((p.name,im.copy()))
    sheet=Image.new('RGB',(960,((len(thumbs)+2)//3)*210),'white'); d=ImageDraw.Draw(sheet)
    for i,(name,im) in enumerate(thumbs):
        x=(i%3)*320; y=(i//3)*210; sheet.paste(im,(x,y)); d.text((x+6,y+184),name,fill=(20,47,107))
    sheet.save(root/'qa/contact-sheet.png')
    print('Rendered previews and contact sheet')
