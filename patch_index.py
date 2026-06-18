import re

with open('/Volumes/MacData/Users/yusuf/Dev/markwebsite/index.html', 'r') as f:
    content = f.read()

video_section = """
  <!-- VIDEO GALLERY SECTION -->
  <section class="video-gallery" id="videos">
    <div class="container">
      <div class="section-header">
        <div class="section-tag">Action & Training</div>
        <h2 class="section-title">See Us In <em>Action</em></h2>
        <p class="section-desc">Get a glimpse of our training sessions, techniques and the dojo atmosphere.</p>
      </div>
      
      <div class="video-grid">
        <div class="video-item">
          <video src="vidoes/v24044gl0000d6134v7og65p82grih0g.MP4" muted loop playsinline onmouseover="this.play()" onmouseout="this.pause()"></video>
          <div class="video-overlay"></div>
          <div class="video-icon"><svg><path d="M8 5v14l11-7z"/></svg></div>
        </div>
        <div class="video-item">
          <video src="vidoes/v24044gl0000d762me7og65pume356f0.MP4" muted loop playsinline onmouseover="this.play()" onmouseout="this.pause()"></video>
          <div class="video-overlay"></div>
          <div class="video-icon"><svg><path d="M8 5v14l11-7z"/></svg></div>
        </div>
        <div class="video-item">
          <video src="vidoes/v24044gl0000d8707lfog65s9v9aqqo0.MP4" muted loop playsinline onmouseover="this.play()" onmouseout="this.pause()"></video>
          <div class="video-overlay"></div>
          <div class="video-icon"><svg><path d="M8 5v14l11-7z"/></svg></div>
        </div>
        <div class="video-item">
          <video src="vidoes/v24044gl0000d8atj87og65l4805q9dg.MP4" muted loop playsinline onmouseover="this.play()" onmouseout="this.pause()"></video>
          <div class="video-overlay"></div>
          <div class="video-icon"><svg><path d="M8 5v14l11-7z"/></svg></div>
        </div>
        <div class="video-item">
          <video src="vidoes/2fdac8f2-102c-4296-838e-8bfd611b0d1c.MP4" muted loop playsinline onmouseover="this.play()" onmouseout="this.pause()"></video>
          <div class="video-overlay"></div>
          <div class="video-icon"><svg><path d="M8 5v14l11-7z"/></svg></div>
        </div>
      </div>
    </div>
  </section>
"""

# Replace the closing tag of the classes section, right before the CTA section starts
# The CTA section starts with '  <!-- CTA SECTION -->'
content = content.replace('  <!-- CTA SECTION -->', video_section + '\n  <!-- CTA SECTION -->')

with open('/Volumes/MacData/Users/yusuf/Dev/markwebsite/index.html', 'w') as f:
    f.write(content)
