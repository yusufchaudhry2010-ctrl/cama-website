import os
import re

BASE_DIR = '/Volumes/MacData/Users/yusuf/Dev/markwebsite'
HTML_FILES = [f for f in os.listdir(BASE_DIR) if f.endswith('.html')]

new_social = """<div class="footer-social">
          <a href="https://www.facebook.com/ChilternAcademyOfMA/photos?locale=en_GB" target="_blank" class="social-btn" aria-label="Facebook" style="display:flex;align-items:center;justify-content:center;">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M14 13.5h2.5l1-4H14v-2c0-1.03 0-2 2-2h1.5V2.14c-.326-.043-1.557-.14-2.857-.14C11.928 2 10 3.657 10 6.7v2.8H7.5v4H10v12h4v-12z"/></svg>
          </a>
          <a href="https://www.instagram.com/chilternacademyofma/" target="_blank" class="social-btn" aria-label="Instagram" style="display:flex;align-items:center;justify-content:center;">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg>
          </a>
          <a href="https://www.tiktok.com/@chilternacademyma" target="_blank" class="social-btn" aria-label="TikTok" style="display:flex;align-items:center;justify-content:center;">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M19.59 6.69a4.83 4.83 0 0 1-3.77-4.25V2h-3.45v13.67a2.89 2.89 0 0 1-5.2-1.74 2.89 2.89 0 0 1 2.89-2.89 2.88 2.88 0 0 1 1.54.45V8.12a5.83 5.83 0 0 0-1.54-.2 5.89 5.89 0 0 0-5.89 5.89 5.89 5.89 0 0 0 5.89 5.89 5.89 5.89 0 0 0 5.89-5.89V10.4a8.3 8.3 0 0 0 3.64 1.34V8.29a5.1 5.1 0 0 1-1.89-.52z"/></svg>
          </a>
        </div>"""

for fname in HTML_FILES:
    fpath = os.path.join(BASE_DIR, fname)
    with open(fpath, 'r') as f:
        content = f.read()
        
    # Check if footer-social already exists
    if 'footer-social' not in content:
        # If it doesn't, we need to inject it into the footer-brand div.
        # Find: <p class="footer-tagline">Forging Warriors Since 2018</p></div>
        # And inject it before the closing </div>
        content = content.replace('<p class="footer-tagline">Forging Warriors Since 2018</p></div>', '<p class="footer-tagline">Forging Warriors Since 2018</p>\n        ' + new_social + '\n      </div>')
        
        with open(fpath, 'w') as f:
            f.write(content)
            print(f"Injected into {fname}")

print("Injection complete")
