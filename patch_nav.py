import re
import os

BASE_DIR = '/Volumes/MacData/Users/yusuf/Dev/markwebsite'
HTML_FILES = ['index.html', 'instructors.html', 'adult-kungfu.html', 'kids-kungfu.html', 'kids-judo.html', 'personal-training.html', 'sparx-boxing.html', 'taichi.html', 'contact.html', 'bookings.html', 'schedule.html']

NAV_TEMPLATE = """    <div class="nav-container">
      <a href="index.html" class="nav-logo" id="nav-logo-link">
        <img src="logo.PNG" alt="CAMA Logo" class="nav-logo-img" />
        <div class="logo-text">
          <span class="logo-title">CHILTERN</span>
          <span class="logo-sub">ACADEMY OF MARTIAL ARTS</span>
        </div>
      </a>
      <button class="hamburger" id="hamburger" aria-label="Toggle menu"><span></span><span></span><span></span></button>
      <ul class="nav-links" id="nav-links">
        <li><a href="index.html" class="nav-link {home_active}">Home</a></li>
        <li><a href="personal-training.html" class="nav-link {pt_active}">Personal Training</a></li>
        <li class="dropdown">
          <a href="#" class="nav-link {ma_active}">Martial Arts ▾</a>
          <ul class="dropdown-menu">
            <li><a href="adult-kungfu.html">🥋 Adult Kung Fu</a></li>
            <li><a href="kids-kungfu.html">👦 Kids Kung Fu</a></li>
            <li><a href="kids-judo.html">🏆 Kids Judo</a></li>
            <li><a href="taichi.html">🌀 Tai Chi</a></li>
            <li><a href="sparx-boxing.html">🥊 SparX Boxing</a></li>
          </ul>
        </li>
        <li><a href="instructors.html" class="nav-link {about_active}">About</a></li>
        <li><a href="schedule.html" class="nav-link {sched_active}">Classes</a></li>
        <li><a href="contact.html" class="nav-link {contact_active}">Contact</a></li>
        <li><a href="bookings.html" class="nav-link nav-cta {book_active}">Book Now</a></li>
      </ul>
    </div>"""

for fname in HTML_FILES:
    fpath = os.path.join(BASE_DIR, fname)
    if not os.path.exists(fpath): continue
    
    with open(fpath, 'r') as f:
        content = f.read()
        
    # Determine active states
    home_active = 'active' if fname == 'index.html' else ''
    pt_active = 'active' if fname == 'personal-training.html' else ''
    ma_active = 'active' if fname in ['adult-kungfu.html', 'kids-kungfu.html', 'kids-judo.html', 'taichi.html', 'sparx-boxing.html'] else ''
    about_active = 'active' if fname == 'instructors.html' else ''
    sched_active = 'active' if fname == 'schedule.html' else ''
    contact_active = 'active' if fname == 'contact.html' else ''
    book_active = 'active' if fname == 'bookings.html' else ''
    
    nav_html = NAV_TEMPLATE.format(
        home_active=home_active, pt_active=pt_active, ma_active=ma_active, 
        about_active=about_active, sched_active=sched_active, 
        contact_active=contact_active, book_active=book_active
    )
    
    # regex replace inside <nav id="navbar">...</nav>
    content = re.sub(r'<div class="nav-container">.*?</ul>\s*</div>', nav_html, content, flags=re.DOTALL)
    
    # Make background overlays lighter for all disciplines
    content = re.sub(r'background:linear-gradient\([^)]+\)', 'background:linear-gradient(90deg,rgba(10,10,10,0.6) 0%,rgba(10,10,10,0) 80%)', content)
    
    with open(fpath, 'w') as f:
        f.write(content)

print("Nav and gradient fixes complete")
