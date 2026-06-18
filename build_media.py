import os
import re

BASE_DIR = '/Volumes/MacData/Users/yusuf/Dev/markwebsite'
fpath_idx = os.path.join(BASE_DIR, 'index.html')

with open(fpath_idx, 'r') as f:
    content = f.read()

# Extract header and footer
header = content.split('<nav id="navbar">')[0]
footer = '<footer' + content.split('<footer')[1]

media_page = header + """<nav id="navbar">
    <div class="nav-container">
      <a href="index.html" class="nav-logo" id="nav-logo-link">
        <img src="logo.PNG" alt="CAMA Logo" class="nav-logo-img" />
        <div class="logo-text">
          <span class="logo-title">CHILTERN</span>
          <span class="logo-sub">ACADEMY OF MARTIAL ARTS</span>
        </div>
      </a>
      <button class="hamburger" id="hamburger" aria-label="Toggle menu"><span></span><span></span><span></span></button>
      <ul class="nav-links" id="nav-links">
        <li><a href="index.html" class="nav-link">Home</a></li>
        <li><a href="personal-training.html" class="nav-link">Personal Training</a></li>
        <li class="dropdown">
          <a href="#" class="nav-link">Martial Arts ▾</a>
          <ul class="dropdown-menu">
            <li><a href="adult-kungfu.html">🥋 Adult Kung Fu</a></li>
            <li><a href="kids-kungfu.html">👦 Kids Kung Fu</a></li>
            <li><a href="kids-judo.html">🏆 Kids Judo</a></li>
            <li><a href="taichi.html">🌀 Tai Chi</a></li>
            <li><a href="sparx-boxing.html">🥊 SparX Boxing</a></li>
          </ul>
        </li>
        <li><a href="instructors.html" class="nav-link">About</a></li>
        <li><a href="schedule.html" class="nav-link">Classes</a></li>
        <li><a href="media.html" class="nav-link active">Media</a></li>
        <li><a href="contact.html" class="nav-link">Contact</a></li>
      </ul>
    </div>
  </nav>

  <div class="page-hero">
    <div class="section-tag">Gallery</div>
    <h1 class="page-hero-title"><em style="color:var(--red)">Media</em> & Action</h1>
    <p class="page-hero-sub">Experience the training, the people, and the spirit of CAMA</p>
  </div>

  <section class="media-section" id="media-images">
    <div class="container">
      <h2 class="section-title" style="margin-bottom: 2rem; font-size: 2.5rem; text-align: left;">Photo Gallery</h2>
      <div class="media-masonry">
        <!-- Generate images -->
"""

images_dir = os.path.join(BASE_DIR, 'images')
images = [f for f in os.listdir(images_dir) if f.endswith(('.jpg', '.JPG', '.png', '.PNG', '.WEBP', '.webp')) and f != 'logo.PNG' and f != '.DS_Store']
for img in sorted(images):
    media_page += f'        <div class="media-item"><img src="images/{img}" alt="CAMA Photo" loading="lazy" /></div>\n'

media_page += """      </div>
    </div>
  </section>

  <section class="media-section" id="media-videos" style="background: var(--dark-2);">
    <div class="container">
      <h2 class="section-title" style="margin-bottom: 2rem; font-size: 2.5rem; text-align: left;">Videos</h2>
      <div class="video-grid">
"""

videos_dir = os.path.join(BASE_DIR, 'vidoes')
videos = [f for f in os.listdir(videos_dir) if f.endswith('.MP4')]
for vid in sorted(videos):
    media_page += f"""        <div class="video-item">
          <video src="vidoes/{vid}" controls playsinline preload="metadata" style="object-fit: cover;"></video>
        </div>\n"""

media_page += """      </div>
    </div>
  </section>
"""

# Replace page title
media_page = media_page.replace('<title>Chiltern Academy of Martial Arts</title>', '<title>Media Gallery | Chiltern Academy of Martial Arts</title>')

media_page += footer

with open(os.path.join(BASE_DIR, 'media.html'), 'w') as f:
    f.write(media_page)

print("Created media.html")
