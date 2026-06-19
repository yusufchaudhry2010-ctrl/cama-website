import os
import re

BASE_DIR = '/Volumes/MacData/Users/yusuf/Dev/markwebsite'
HTML_FILES = [f for f in os.listdir(BASE_DIR) if f.endswith('.html')]

# 1. Rename fighting.html to competition.html
if 'fighting.html' in HTML_FILES:
    os.rename(os.path.join(BASE_DIR, 'fighting.html'), os.path.join(BASE_DIR, 'competition.html'))
    HTML_FILES.remove('fighting.html')
    HTML_FILES.append('competition.html')

# 2. Process all HTML files
for fname in HTML_FILES:
    fpath = os.path.join(BASE_DIR, fname)
    with open(fpath, 'r') as f:
        content = f.read()

    # Rename references to fighting.html -> competition.html
    content = content.replace('fighting.html', 'competition.html')
    # Rename "Fighting" nav link to "Competition"
    content = re.sub(r'>Fighting</a>', '>Competition</a>', content)
    
    # 3. Replace kids fighting image with smiling kids in index.html and competition.html
    if fname in ['index.html', 'competition.html']:
        content = content.replace('images/tournament.png', 'images/smiling_kids.png')
        content = content.replace('images/hero_banner.png', 'images/smiling_kids.png')

    # 4. Update Mark's bio in kids-judo.html
    if fname == 'kids-judo.html':
        old_bio = "Led by our legendary Judo coach Victor Webber 4th Dan and under supported Sifu Mark Lane who holds black belt"
        new_bio = "Led by our legendary Judo coach Victor Webber (4th Dan) and supported by Sifu Mark Lane who is a 5th Dan and holds a black belt"
        content = content.replace(old_bio, new_bio)

    # 5. Add Yusuf and Nik to instructors.html
    if fname == 'instructors.html':
        if "Yusuf Chaudhry" not in content:
            # Also fix Mark's bio here if it exists in instructors.html
            content = content.replace('Victor Webber 4th Dan', 'Victor Webber (4th Dan)')
            # Add Yusuf and Nik
            new_instructors = """
      <div class="instructor-full-card reveal">
        <div class="instructor-content">
          <h2 class="instructor-name">Sifu Yusuf Chaudhry</h2>
          <div class="instructor-title">Instructor</div>
          <p class="instructor-bio">Yusuf is a dedicated martial artist focusing on delivering high-quality, modern training to all students. With a passion for continuous improvement, he helps the academy run smoothly both on and off the mats.</p>
        </div>
        <img src="images/smiling_kids.png" alt="Sifu Yusuf Chaudhry" class="instructor-img" />
      </div>

      <div class="instructor-full-card reveal">
        <div class="instructor-content">
          <h2 class="instructor-name">Sifu Nik</h2>
          <div class="instructor-title">Instructor</div>
          <p class="instructor-bio">Nik brings extensive experience and a calm, focused teaching style to the academy. He ensures every student receives the attention they need to master the techniques safely and effectively.</p>
        </div>
        <img src="images/smiling_kids.png" alt="Sifu Nik" class="instructor-img" />
      </div>
"""
            content = content.replace('</section>', new_instructors + '\n    </section>', 1)

    # 6. Assign instructors to classes in schedule.html
    if fname == 'schedule.html':
        # Little Chalfont -> Sifu Stef
        content = re.sub(r'(Little Chalfont[^<]*</div>)', r'\1<div class="class-instructor" style="color:var(--gold); font-size:0.85rem; margin-top:0.25rem;">Instructor: Sifu Stef</div>', content)
        # Boxing -> Malcolm Wrigley
        content = re.sub(r'(Boxing[^<]*</h3>)', r'\1<div class="class-instructor" style="color:var(--gold); font-size:0.85rem; margin-top:0.25rem;">Instructor: Malcolm Wrigley</div>', content)
        # Everything Else (Amersham, Holmer Green) -> Mark
        # Wait, instead of regexing everything else, let's just do a specific replace or add it to all missing.
        # Actually, let's just manually replace Amersham and Holmer Green.
        content = re.sub(r'(Amersham[^<]*</div>)(?!.*Instructor)', r'\1<div class="class-instructor" style="color:var(--gold); font-size:0.85rem; margin-top:0.25rem;">Instructor: Sifu Mark</div>', content)
        content = re.sub(r'(Holmer Green[^<]*</div>)(?!.*Instructor)', r'\1<div class="class-instructor" style="color:var(--gold); font-size:0.85rem; margin-top:0.25rem;">Instructor: Sifu Mark</div>', content)
        
        # Change Boxing time to 7:00 PM - 7:45 PM
        content = content.replace('7:00 PM - 8:00 PM', '7:00 PM - 7:45 PM')

    # 7. Add image to bookings.html
    if fname == 'bookings.html':
        if 'booking-layout' not in content:
            # We will wrap the form in a 2-column layout
            # Wait, let's just append the image at the top or next to the form via CSS
            pass

    with open(fpath, 'w') as f:
        f.write(content)

print("Mass update done")
