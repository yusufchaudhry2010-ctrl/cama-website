import os
import re

HTML_FILES = [f for f in os.listdir(".") if f.endswith(".html")]

NEW_FOOTER_BOTTOM = """    <div class="footer-bottom" style="display:flex; flex-direction:column; align-items:center; gap:1.2rem; padding: 2rem 0 1rem 0;">
      <p style="margin:0;">© 2024 Chiltern Academy of Martial Arts. All rights reserved.</p>
      <a href="https://www.visionaryailabs.co.uk/" target="_blank" style="text-decoration:none; display:inline-flex; align-items:center; gap:0.8rem; opacity:1; transition:transform 0.3s ease, filter 0.3s ease; padding: 0.6rem 1.2rem; border: 1px solid rgba(212,160,23,0.4); border-radius: 8px; background: rgba(0,0,0,0.4);" onmouseover="this.style.transform='scale(1.03)'; this.style.filter='brightness(1.2)'" onmouseout="this.style.transform='scale(1)'; this.style.filter='brightness(1)'">
        <span style="color:var(--light-mid); font-size:0.75rem; text-transform:uppercase; letter-spacing:1px;">Powered by</span>
        <img src="images/visionary_logo.jpg" alt="[Visionary AI Logo]" style="height:28px; width:auto; border-radius:4px;" />
        <span style="font-family:var(--font-display); font-size:1rem; color:#D4A017; letter-spacing:1px; font-weight:600; text-decoration: underline; text-decoration-color: rgba(212,160,23,0.5); text-underline-offset: 4px;">VISIONARY AI LABS LTD ↗</span>
      </a>
    </div>"""

for fname in HTML_FILES:
    with open(fname, "r") as f:
        content = f.read()
    
    # Replace the old footer bottom
    content = re.sub(r"<div class=\"footer-bottom\">\s*<p>.*?</p>\s*<a.*?</a>\s*</div>", NEW_FOOTER_BOTTOM, content, flags=re.DOTALL)
    
    # Bump cache buster to v=8
    content = re.sub(r"href=\"styles\.css(\?v=\d+)?\"", "href=\"styles.css?v=8\"", content)
    
    with open(fname, "w") as f:
        f.write(content)

print("Updated footer bottom with much more obvious clickable button.")
