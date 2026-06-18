import re

with open('/Volumes/MacData/Users/yusuf/Dev/markwebsite/index.html', 'r') as f:
    content = f.read()

# Remove the tournament modal
content = re.sub(r'<!-- TOURNAMENT MODAL -->.*</body>', '</body>', content, flags=re.DOTALL)

# Add the slideshow HTML
old_hero = """    <div class="hero-bg">
      <img src="images/tournament.png" alt="Martial Arts" class="hero-img" />
      <div class="hero-overlay"></div>
    </div>"""

new_hero = """    <div class="hero-bg slideshow">
      <img src="images/tournament.png" alt="Martial Arts" class="hero-img slide show" />
      <img src="images/image2.jpg" alt="Martial Arts" class="hero-img slide" />
      <img src="frontcover.png" alt="Martial Arts" class="hero-img slide" />
      <div class="hero-overlay"></div>
    </div>"""

content = content.replace(old_hero, new_hero)

with open('/Volumes/MacData/Users/yusuf/Dev/markwebsite/index.html', 'w') as f:
    f.write(content)
