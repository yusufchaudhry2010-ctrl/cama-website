import os
import re

BASE_DIR = '/Volumes/MacData/Users/yusuf/Dev/markwebsite'
fpath_idx = os.path.join(BASE_DIR, 'index.html')

with open(fpath_idx, 'r') as f:
    content = f.read()

# Extract header and footer
header = content.split('<nav id="navbar">')[0]
footer = '<footer' + content.split('<footer')[1]
# clean up any injected modal script from footer just in case
footer = re.sub(r'<!-- TOURNAMENT MODAL -->.*?</script>', '', footer, flags=re.DOTALL)

fighting_page = header + """<nav id="navbar">
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
        <li><a href="fighting.html" class="nav-link active">Fighting</a></li>
        <li><a href="instructors.html" class="nav-link">About</a></li>
        <li><a href="schedule.html" class="nav-link">Classes</a></li>
        <li><a href="media.html" class="nav-link">Media</a></li>
        <li><a href="contact.html" class="nav-link">Contact</a></li>
      </ul>
    </div>
  </nav>

  <div class="page-hero">
    <div class="section-tag">Competition</div>
    <h1 class="page-hero-title"><em style="color:var(--red)">Fighting</em> Tournament</h1>
    <p class="page-hero-sub">Step into the ring and test your skills</p>
  </div>

  <section style="padding: 6rem 2rem; max-width: 900px; margin: 0 auto; text-align: center;">
    <h2 class="section-title" style="margin-bottom: 2rem;">Get Experience With Fighting</h2>
    
    <p class="about-text" style="font-size: 1.2rem; margin-bottom: 2rem;">
      We are going to start doing this soon! Learn proper defence and competition rules using authentic head gear and body guards. 
      <br><br>
      <strong style="color:var(--white);">Open to ALL AGES!</strong> Fights will be strictly matched according to your grade and age so everyone competes safely and fairly.
    </p>

    <div style="background: var(--dark-3); border-left: 4px solid var(--gold); padding: 2.5rem; border-radius: var(--radius-lg); text-align: left; margin: 3rem 0; box-shadow: var(--shadow-card);">
      <h3 style="font-family: var(--font-display); color: var(--gold); font-size: 2rem; margin-bottom: 1rem; letter-spacing: 1px;">Our Goal When We Start</h3>
      <p style="font-size: 1.1rem; color: var(--light); line-height: 1.8;">
        To expand our fighting program to other clubs and make this a proper, official, and professional fighting experience. We're building this big, focusing on proper body conditioning and the core training we already practice!
      </p>
    </div>

    <img src="images/tournament.png" alt="Kids Sparring" style="width: 100%; border-radius: var(--radius-lg); margin-top: 2rem; box-shadow: var(--shadow-image);" />

    <div style="margin-top: 4rem;">
      <a href="contact.html" class="btn btn-primary btn-large">Register Your Interest</a>
    </div>
  </section>
"""

# Replace page title
fighting_page = fighting_page.replace('<title>Chiltern Academy of Martial Arts</title>', '<title>Fighting Tournament | Chiltern Academy of Martial Arts</title>')

fighting_page += footer

with open(os.path.join(BASE_DIR, 'fighting.html'), 'w') as f:
    f.write(fighting_page)

print("Created fighting.html")
