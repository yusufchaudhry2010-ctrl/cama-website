with open('/Volumes/MacData/Users/yusuf/Dev/markwebsite/bookings.html', 'r') as f:
    content = f.read()

old_form = '<form id="booking-form" novalidate>'
new_form = '''<form id="booking-form" action="https://formsubmit.co/iyusufc.buisness@gmail.com" method="POST">
        <!-- FormSubmit Configuration -->
        <input type="hidden" name="_subject" value="New CAMA Booking / Enquiry!">
        <input type="hidden" name="_next" value="https://yusufchaudhry2010-ctrl.github.io/cama-website/bookings.html?success=true">
        <input type="hidden" name="_captcha" value="false">'''

content = content.replace(old_form, new_form)

# I should also update the JS so it doesn't prevent default submission if it does.
with open('/Volumes/MacData/Users/yusuf/Dev/markwebsite/main.js', 'r') as f:
    js_content = f.read()
    
# Remove preventDefault to allow form submission to FormSubmit
js_content = js_content.replace("e.preventDefault();", "// e.preventDefault(); // Allowed to submit to FormSubmit")
# Remove the fake success alert since FormSubmit handles the redirect
js_content = js_content.replace("btn.innerHTML = 'Booking Request Sent!';", "// FormSubmit will handle redirect")

with open('/Volumes/MacData/Users/yusuf/Dev/markwebsite/main.js', 'w') as f:
    f.write(js_content)

with open('/Volumes/MacData/Users/yusuf/Dev/markwebsite/bookings.html', 'w') as f:
    f.write(content)

print("Form updated")
