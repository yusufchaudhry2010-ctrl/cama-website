import os
import re

HTML_FILES = [f for f in os.listdir(".") if f.endswith(".html")]

NEW_FOOTER_BOTTOM = """    <div class="footer-bottom" style="display:flex; flex-direction:column; align-items:center; gap:1.2rem; padding: 2rem 0 1rem 0;">
      <p style="margin:0;">© 2024 Chiltern Academy of Martial Arts. All rights reserved.</p>
      <a href="https://www.visionaryailabs.co.uk/" target="_blank" style="text-decoration:none; display:flex; align-items:center; gap:0.6rem; opacity:0.75; transition:opacity 0.3s ease;" onmouseover="this.style.opacity='1'" onmouseout="this.style.opacity='0.75'">
        <span style="color:rgba(255,255,255,0.6); font-size:0.75rem; text-transform:uppercase; letter-spacing:1px;">Powered by</span>
        <img src="images/visionary_logo.jpg" alt="Visionary AI Labs" style="height:22px; width:auto; border-radius:2px;" onerror="this.style.display='none'" />
        <span style="font-family:var(--font-display); font-size:0.9rem; color:#D4A017; letter-spacing:1px; font-weight:600;">VISIONARY AI LABS LTD</span>
      </a>
    </div>"""

for fname in HTML_FILES:
    with open(fname, "r") as f:
        content = f.read()
    
    # Replace the old footer bottom
    content = re.sub(r"<div class=\"footer-bottom\">\s*<p>.*?</p>\s*</div>", NEW_FOOTER_BOTTOM, content, flags=re.DOTALL)
    
    with open(fname, "w") as f:
        f.write(content)

print("Updated footer bottom with Visionary AI Labs branding.")
