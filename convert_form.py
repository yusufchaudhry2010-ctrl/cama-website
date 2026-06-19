with open('/Volumes/MacData/Users/yusuf/Dev/markwebsite/bookings.html', 'r') as f:
    content = f.read()

# Change the form back to a generic form without formsubmit
import re
content = re.sub(r'<form id="booking-form" action="https://formsubmit.co/iyusufc.buisness@gmail.com" method="POST">', '<form id="booking-form">', content)
content = re.sub(r'<!-- FormSubmit Configuration -->.*<input type="hidden" name="_captcha" value="false">', '', content, flags=re.DOTALL)

with open('/Volumes/MacData/Users/yusuf/Dev/markwebsite/bookings.html', 'w') as f:
    f.write(content)

with open('/Volumes/MacData/Users/yusuf/Dev/markwebsite/main.js', 'r') as f:
    js = f.read()

# Replace the form logic with mailto logic
new_js = """
  // Form handling via mailto fallback
  const bookingForm = document.getElementById('booking-form');
  if (bookingForm) {
    bookingForm.addEventListener('submit', (e) => {
      e.preventDefault();
      
      const firstName = document.getElementById('first-name').value;
      const lastName = document.getElementById('last-name').value;
      const email = document.getElementById('email').value;
      const phone = document.getElementById('phone').value;
      const discipline = document.getElementById('discipline').value;
      const exp = document.getElementById('experience').value;
      const msg = document.getElementById('message').value;

      const subject = encodeURIComponent('New CAMA Booking: ' + firstName + ' ' + lastName);
      let body = `Name: ${firstName} ${lastName}%0D%0A`;
      body += `Email: ${email}%0D%0A`;
      body += `Phone: ${phone}%0D%0A`;
      body += `Class of Interest: ${discipline}%0D%0A`;
      body += `Experience Level: ${exp}%0D%0A%0D%0A`;
      body += `Message:%0D%0A${msg}`;

      window.location.href = `mailto:iyusufc.buisness@gmail.com?subject=${subject}&body=${body}`;
      
      const btn = bookingForm.querySelector('button[type="submit"]');
      btn.innerHTML = 'Opening Email App...';
      setTimeout(() => { btn.innerHTML = 'Send Booking Request'; }, 3000);
    });
  }
"""

js = re.sub(r'const bookingForm.*// FormSubmit will handle redirect\n    \}\);\n  \}', new_js, js, flags=re.DOTALL)

with open('/Volumes/MacData/Users/yusuf/Dev/markwebsite/main.js', 'w') as f:
    f.write(js)

print("Converted to mailto")
