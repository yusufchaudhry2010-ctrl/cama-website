import os

BASE_DIR = '/Volumes/MacData/Users/yusuf/Dev/markwebsite'
HTML_FILES = [f for f in os.listdir(BASE_DIR) if f.endswith('.html')]

missing_footer = []
for fname in HTML_FILES:
    fpath = os.path.join(BASE_DIR, fname)
    with open(fpath, 'r') as f:
        if '<footer' not in f.read():
            missing_footer.append(fname)

print("Files missing footer:", missing_footer)
