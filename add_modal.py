import re

with open('/Volumes/MacData/Users/yusuf/Dev/markwebsite/index.html', 'r') as f:
    content = f.read()

# 1. Update hero image
content = content.replace('<img src="frontcover.png" alt="Martial Arts" class="hero-img" />', '<img src="images/tournament.png" alt="Martial Arts" class="hero-img" />')

# 2. Add Modal before </body>
modal_html = """
  <!-- TOURNAMENT MODAL -->
  <div class="tournament-modal" id="tournamentModal">
    <div class="tournament-modal-content">
      <button class="tournament-modal-close" onclick="document.getElementById('tournamentModal').classList.remove('active')" aria-label="Close Modal">&times;</button>
      <h2 class="tournament-title">FIGHTING TOURNAMENT</h2>
      <p class="tournament-desc">
        Get experience with fighting! Learn proper defence and competition rules using authentic head gear and body guards. <br><br>
        <strong style="color:var(--white);">Open to ALL AGES!</strong> Fights will be strictly matched according to your grade and age.
      </p>
      <div class="tournament-goal">
        <strong style="color:var(--gold); display:block; margin-bottom:0.5rem; text-transform:uppercase; letter-spacing:1px; font-size:0.9rem;">Our Goal</strong>
        To expand our fighting program and start competing with other clubs. We're making this big, focusing on proper body conditioning and the core training we already practice!
      </div>
      <button class="btn btn-primary" onclick="document.getElementById('tournamentModal').classList.remove('active')" style="width: 100%; font-size: 1.1rem; padding: 1rem; border-radius: 8px;">Got It, Let's Go!</button>
    </div>
  </div>
  <script>
    // Show modal shortly after page load
    window.addEventListener('DOMContentLoaded', () => {
      setTimeout(() => {
        document.getElementById('tournamentModal').classList.add('active');
      }, 600);
    });
  </script>
</body>"""

if "<!-- TOURNAMENT MODAL -->" not in content:
    content = content.replace("</body>", modal_html)

with open('/Volumes/MacData/Users/yusuf/Dev/markwebsite/index.html', 'w') as f:
    f.write(content)
