import os
import re

images_dir = '/Volumes/MacData/Users/yusuf/Dev/markwebsite/images'
media_file = '/Volumes/MacData/Users/yusuf/Dev/markwebsite/media.html'

# Find the whatsapp images
whatsapp_images = [f for f in os.listdir(images_dir) if f.startswith('WhatsApp Image')]
whatsapp_images.sort()

new_images_html = ""
for i, old_name in enumerate(whatsapp_images):
    new_name = f"whatsapp_photo_{i+1}.jpg"
    os.rename(os.path.join(images_dir, old_name), os.path.join(images_dir, new_name))
    
    # Generate HTML
    new_images_html += f"""
        <div class="media-item">
          <img src="images/{new_name}" alt="CAMA Martial Arts Training" loading="lazy" />
        </div>"""

with open(media_file, 'r') as f:
    content = f.read()

# Inject the new HTML into the masonry container before it closes
# We know the masonry div ends eventually. We can inject right after the last media-item.
# Let's just find the last media-item block and insert after it.

parts = content.rsplit('</div>\n      </div>', 1) # Trying to find the end of masonry
if len(parts) == 2:
    # This might match the end of the masonry div
    new_content = parts[0] + new_images_html + '\n      </div>\n      </div>' + parts[1]
    with open(media_file, 'w') as f:
        f.write(new_content)
    print("Injected into media.html using strict split")
else:
    print("Could not find the exact split point, attempting regex")

