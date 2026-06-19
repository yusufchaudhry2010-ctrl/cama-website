import re

with open('/Volumes/MacData/Users/yusuf/Dev/markwebsite/instructors.html', 'r') as f:
    content = f.read()

# Remove the broken Yusuf and Nik from the bottom CTA section
bad_yusuf_nik = """
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
content = content.replace(bad_yusuf_nik, "")

# Insert properly formatted Yusuf and Nik under Victor Webber
proper_yusuf_nik = """
    <!-- YUSUF CHAUDHRY -->
    <div class="instructor-full-card" id="yusuf">
      <div class="instructor-full-img" style="background: var(--dark-3); display: flex; align-items: center; justify-content: center;">
        <span style="color: var(--light-mid); font-family: var(--font-display); font-size: 1.5rem; letter-spacing: 2px;">Image Coming Soon</span>
      </div>
      <div class="instructor-full-body">
        <h2 class="instructor-full-name">Sifu Yusuf Chaudhry</h2>
        <span class="instructor-full-role">Instructor</span>
        <p class="instructor-full-bio">
          Yusuf is a dedicated martial artist focusing on delivering high-quality, modern training to all students. With a passion for continuous improvement, he helps the academy run smoothly both on and off the mats.
        </p>
        <div class="instructor-full-tags">
          <span>Instructor</span><span>Martial Arts</span>
        </div>
      </div>
    </div>

    <!-- SIFU NIK -->
    <div class="instructor-full-card" id="nik">
      <div class="instructor-full-img" style="background: var(--dark-3); display: flex; align-items: center; justify-content: center;">
        <span style="color: var(--light-mid); font-family: var(--font-display); font-size: 1.5rem; letter-spacing: 2px;">Image Coming Soon</span>
      </div>
      <div class="instructor-full-body">
        <h2 class="instructor-full-name">Sifu Nik</h2>
        <span class="instructor-full-role">Instructor</span>
        <p class="instructor-full-bio">
          Nik brings extensive experience and a calm, focused teaching style to the academy. He ensures every student receives the attention they need to master the techniques safely and effectively.
        </p>
        <div class="instructor-full-tags">
          <span>Instructor</span><span>Martial Arts</span>
        </div>
      </div>
    </div>
"""

# Find the end of the instructors-page-grid
content = content.replace('    </div>\n\n  </div>\n\n  <!-- CTA -->', '    </div>\n' + proper_yusuf_nik + '\n  </div>\n\n  <!-- CTA -->')

with open('/Volumes/MacData/Users/yusuf/Dev/markwebsite/instructors.html', 'w') as f:
    f.write(content)

print("Fixed layout")
