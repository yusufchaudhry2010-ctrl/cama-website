import re

html_path = '/Volumes/MacData/Users/yusuf/Dev/markwebsite/media.html'
with open(html_path, 'r') as f:
    content = f.read()

# Valid images
images = [
    '12550733-e490-453e-a3c3-837af3304075.JPG',
    '2172c2e8-4672-42d1-83ba-6166e4ffb1c8.JPG',
    '569919201_18345448207204285_7657117713369347374_n.jpg',
    '570115047_18345448282204285_5134055943656707869_n.jpg',
    '571192796_18345448171204285_622339734830428278_n.jpg',
    '571238009_18345448216204285_7963088568420857341_n.jpg',
    '581236206_18349439812204285_3507313815916949126_n.jpg',
    '583698297_18349845493204285_4932316749202134843_n.jpg',
    '585211874_1418394516954536_1357814725408411304_n.jpg',
    '587967220_18350561863204285_8453692680389686787_n.jpg',
    '655962964_18365329717204285_359658482346455874_n.jpg',
    '683388362_1561567495970570_7081931025399775173_n.jpg',
    '704507125_1580310060762980_5879331242350311653_n.jpg',
    '716310675_18376614205204285_6805631051651093581_n.jpg',
    '99a8c5bf-d6e5-49fa-b609-5fdea487771b.JPG',
    'temp_image_AD8CC5AC-BE52-4F56-860F-53B362482E53.WEBP'
] # 16 images exactly (multiple of 4)

gallery_html = '<div class="media-masonry">\n'
for img in images:
    gallery_html += f'        <div class="media-item"><img src="images/{img}" alt="CAMA Photo" loading="lazy" /></div>\n'
gallery_html += '      </div>'

# Replace masonry div
content = re.sub(r'<div class="media-masonry">.*?</div>\s+</div>\s+</section>', gallery_html + '\n    </div>\n  </section>', content, flags=re.DOTALL)

# Make container wider
content = content.replace('<div class="container">\n      <h2 class="section-title" style="margin-bottom: 2rem; font-size: 2.5rem; text-align: left;">Photo Gallery</h2>', '<div class="container" style="max-width: 1400px;">\n      <h2 class="section-title" style="margin-bottom: 2rem; font-size: 2.5rem; text-align: left;">Photo Gallery</h2>')

with open(html_path, 'w') as f:
    f.write(content)

print("Gallery rebuilt")
