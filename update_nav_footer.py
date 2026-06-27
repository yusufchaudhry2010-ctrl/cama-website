import os
import re

HTML_FILES = [f for f in os.listdir('.') if f.endswith('.html')]

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
        <li><a href="schedule.html" class="nav-link {sched_active}">Classes</a></li>
        <li><a href="instructors.html" class="nav-link {about_active}">About Us</a></li>
        <li><a href="bookings.html" class="nav-link nav-cta {book_active}">Book Now</a></li>
      </ul>
    </div>"""

FOOTER_TEMPLATE = """  <footer class="footer">
    <div class="footer-container">
      <div class="footer-brand"><div class="footer-logo"><img src="logo.PNG" alt="CAMA" style="width:48px;height:48px;object-fit:contain;" /><div><span class="footer-name">CHILTERN</span><span class="footer-name-sub">ACADEMY OF MARTIAL ARTS</span></div></div><p class="footer-tagline">Forging Warriors Since 2018</p>
        <div class="footer-social">
          <a href="https://www.facebook.com/ChilternAcademyOfMA/photos?locale=en_GB" target="_blank" class="social-btn" aria-label="Facebook" style="display:flex;align-items:center;justify-content:center;">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M14 13.5h2.5l1-4H14v-2c0-1.03 0-2 2-2h1.5V2.14c-.326-.043-1.557-.14-2.857-.14C11.928 2 10 3.657 10 6.7v2.8H7.5v4H10v12h4v-12z"/></svg>
          </a>
          <a href="https://www.instagram.com/chilternacademyofma/" target="_blank" class="social-btn" aria-label="Instagram" style="display:flex;align-items:center;justify-content:center;">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg>
          </a>
          <a href="https://www.tiktok.com/@chilternacademyma" target="_blank" class="social-btn" aria-label="TikTok" style="display:flex;align-items:center;justify-content:center;">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M19.59 6.69a4.83 4.83 0 0 1-3.77-4.25V2h-3.45v13.67a2.89 2.89 0 0 1-5.2-1.74 2.89 2.89 0 0 1 2.89-2.89 2.88 2.88 0 0 1 1.54.45V8.12a5.83 5.83 0 0 0-1.54-.2 5.89 5.89 0 0 0-5.89 5.89 5.89 5.89 0 0 0 5.89 5.89 5.89 5.89 0 0 0 5.89-5.89V10.4a8.3 8.3 0 0 0 3.64 1.34V8.29a5.1 5.1 0 0 1-1.89-.52z"/></svg>
          </a>
        </div>
      </div>
      <div class="footer-links-group"><h4>Martial Arts</h4><ul><li><a href="adult-kungfu.html">Adult Kung Fu</a></li><li><a href="kids-kungfu.html">Kids Kung Fu</a></li><li><a href="kids-judo.html">Kids Judo</a></li><li><a href="taichi.html">Tai Chi</a></li><li><a href="sparx-boxing.html">SparX Boxing</a></li></ul></div>
      <div class="footer-links-group"><h4>Explore</h4><ul><li><a href="instructors.html">About Us</a></li><li><a href="personal-training.html">Personal Training</a></li><li><a href="holmer-green.html">Locations</a></li><li><a href="competition.html">Competition</a></li><li><a href="media.html">Media</a></li></ul></div>
      <div class="footer-contact"><h4>Contact Us</h4><p>📞 <a href="tel:07545991293">07545 991293</a></p><p>✉️ <a href="mailto:chilternacademyofma@gmail.com">chilternacademyofma@gmail.com</a></p></div>
    </div>
    <div class="footer-bottom"><p>© 2024 Chiltern Academy of Martial Arts. All rights reserved.</p></div>
  </footer>"""

for fname in HTML_FILES:
    with open(fname, 'r') as f:
        content = f.read()
        
    ma_active = 'active' if fname in ['adult-kungfu.html', 'kids-kungfu.html', 'kids-judo.html', 'taichi.html', 'sparx-boxing.html'] else ''
    about_active = 'active' if fname == 'instructors.html' else ''
    sched_active = 'active' if fname == 'schedule.html' else ''
    book_active = 'active' if fname == 'bookings.html' else ''
    
    nav_html = NAV_TEMPLATE.format(
        ma_active=ma_active, about_active=about_active, sched_active=sched_active, book_active=book_active
    )
    
    # regex replace nav
    content = re.sub(r'<div class="nav-container">.*?</ul>\s*</div>', nav_html, content, flags=re.DOTALL)
    
    # regex replace footer
    content = re.sub(r'<footer class="footer">.*?</footer>', FOOTER_TEMPLATE, content, flags=re.DOTALL)
    
    # bump cache to 6
    content = re.sub(r'href="styles\.css(\?v=\d+)?"', 'href="styles.css?v=6"', content)

    with open(fname, 'w') as f:
        f.write(content)
print("Updated all navs and footers")
