import re
import os

pages = {
    'personal-training.html': 'pt_bg.png',
    'adult-kungfu.html': 'kungfu_bg.png',
    'kids-kungfu.html': 'kungfu_bg.png',
    'kungfu.html': 'kungfu_bg.png',
    'kids-judo.html': 'judo_bg.png',
    'judo.html': 'judo_bg.png',
    'taichi.html': 'taichi_bg.png',
    'sparx-boxing.html': 'boxing_bg.png',
    'boxing.html': 'boxing_bg.png',
    'fitness.html': 'fitness_bg.png',
    'competition.html': 'smiling_kids.png'
}

base_dir = '/Volumes/MacData/Users/yusuf/Dev/markwebsite'

for filename, bg in pages.items():
    filepath = os.path.join(base_dir, filename)
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, 'r') as f:
        content = f.read()
        
    if '<!-- BACKGROUND WRAPPER -->' in content:
        continue # Already wrapped
        
    wrapper_top = f'''  <!-- BACKGROUND WRAPPER -->
  <div style="position: relative; overflow: hidden; min-height: 100vh;">
    <div style="position: absolute; inset: 0; z-index: -2;">
      <img src="images/{bg}" alt="Background" style="width: 100%; height: 100%; object-fit: cover; object-position: center;" />
    </div>
    <div style="position: absolute; inset: 0; background: linear-gradient(to bottom, rgba(10,10,12,0.6), rgba(10,10,12,0.95)); z-index: -1;"></div>
'''
    wrapper_bottom = '\n  </div> <!-- END BACKGROUND WRAPPER -->\n'

    # Inject after </nav>
    parts = content.split('</nav>', 1)
    if len(parts) == 2:
        content = parts[0] + '</nav>\n' + wrapper_top + parts[1]
        
    # Inject before <footer
    # Reverse split
    parts = content.rsplit('<footer', 1)
    if len(parts) == 2:
        content = parts[0] + wrapper_bottom + '  <footer' + parts[1]
        
    # Specific fix for competition.html
    if filename == 'competition.html':
        content = re.sub(r'<img src="images/smiling_kids\.png".*?/>', '', content)

    with open(filepath, 'w') as f:
        f.write(content)
        
    print(f"Wrapped {filename} with {bg}")

