import os

media_file = '/Volumes/MacData/Users/yusuf/Dev/markwebsite/media.html'

with open(media_file, 'r') as f:
    lines = f.readlines()

new_lines = []
skip = False
for line in lines:
    if '<div class="media-item">\n' in line and 'whatsapp_photo_1' in line:
        skip = True # start skipping the broken block
        
    if skip:
        if '</div>' in line and '</div>\n' in line and '      </div>\n' in line:
            # We hit the end of the broken block. Wait, let's just use string replace.
            pass
            
