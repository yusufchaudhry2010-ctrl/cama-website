import os
import re

BASE_DIR = '/Volumes/MacData/Users/yusuf/Dev/markwebsite'
HTML_FILES = [f for f in os.listdir(BASE_DIR) if f.endswith('.html')]

old_social = """        <div class="footer-social">
          <a href="#" class="social-btn" aria-label="Facebook">f</a>
          <a href="#" class="social-btn" aria-label="Instagram">in</a>
          <a href="#" class="social-btn" aria-label="YouTube">▶</a>
        </div>"""

new_social = """        <div class="footer-social">
          <a href="https://www.facebook.com/ChilternAcademyOfMA/photos?locale=en_GB" target="_blank" class="social-btn" aria-label="Facebook">f</a>
          <a href="https://www.instagram.com/chilternacademyofma/" target="_blank" class="social-btn" aria-label="Instagram">in</a>
          <a href="https://www.tiktok.com/@chilternacademyma" target="_blank" class="social-btn" aria-label="TikTok">tk</a>
        </div>"""

for fname in HTML_FILES:
    fpath = os.path.join(BASE_DIR, fname)
    with open(fpath, 'r') as f:
        content = f.read()
        
    content = content.replace(old_social, new_social)
    
    with open(fpath, 'w') as f:
        f.write(content)

print("Footers patched")
