import os
import re
import subprocess

pdf = 'N3Doc.pdf'

bat = "@echo off\n\n"

bat += f"magick.exe convert -density 300 {pdf} n3doc.png\n\n"
with open(pdf, mode='rb') as fileIn:
    pdfText = fileIn.read().decode("utf-8", errors="ignore")
rePages = re.compile(r'/Page/\w')
pagesCount = len(rePages.findall(pdfText))

pages = [f'"n3doc-{i}.png"' for i in range(pagesCount)]

index = 0
for page in pages:
    bat += f'magick.exe convert {page} -crop 2x1@ +repage N3RusDoc{index}.png\n'
    index += 1

rus = [f'"N3RusDoc{i}-0.png"' for i in range(pagesCount)]
eng = [f'"N3RusDoc{i}-1.png"' for i in range(pagesCount)]

bat += "magick.exe convert "
for r in rus:
    bat += f'{r} '
bat += "N3RusDoc.pdf\n"

bat += "magick.exe convert "
for e in eng:
    bat += f'{e} '
bat += "N3EngDoc.pdf\n"

with open("doc2lang.bat", mode="w") as fp:
    fp.write(bat)
subprocess.run(["doc2lang.bat"])

for page in pages + eng + ['"doc2lang.bat"']:
    os.remove(page[1:-1])
