import re

# 1. Update schedule.html background brightness
sched_file = '/Volumes/MacData/Users/yusuf/Dev/markwebsite/schedule.html'
with open(sched_file, 'r') as f:
    content = f.read()

content = content.replace('linear-gradient(to bottom, rgba(10,10,12,0.7), rgba(10,10,12,0.95))',
                          'linear-gradient(to bottom, rgba(10,10,12,0.4), rgba(10,10,12,0.85))')

with open(sched_file, 'w') as f:
    f.write(content)

print("Schedule updated")
