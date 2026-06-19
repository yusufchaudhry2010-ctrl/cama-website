import os

img_dir = '/Volumes/MacData/Users/yusuf/Dev/markwebsite/images'
valid_exts = {'.png', '.jpg', '.jpeg', '.webp', '.gif', '.heic'}

images = [f for f in os.listdir(img_dir) if os.path.splitext(f)[1].lower() in valid_exts]
print(f"Total images: {len(images)}")
