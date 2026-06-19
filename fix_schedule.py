import re

sched_file = '/Volumes/MacData/Users/yusuf/Dev/markwebsite/schedule.html'
boxing_file = '/Volumes/MacData/Users/yusuf/Dev/markwebsite/sparx-boxing.html'

# 1. Fix SparX Boxing file time
with open(boxing_file, 'r') as f:
    boxing_content = f.read()
boxing_content = boxing_content.replace('6:30pm – 7:15pm', '7:00pm – 7:45pm')
with open(boxing_file, 'w') as f:
    f.write(boxing_content)

# 2. Fix Schedule file times and instructors
with open(sched_file, 'r') as f:
    sched = f.read()

# Fix Tuesday Boxing Time
sched = sched.replace('<tr><td>Tuesday</td><td>6:30pm – 7:15pm</td><td><span class="badge-discipline">🥊 SparX Boxing</span></td><td>All Levels</td><td>Holmer Green Village Hall</td><td>CAMA Instructor</td></tr>',
                      '<tr><td>Tuesday</td><td>7:00pm – 7:45pm</td><td><span class="badge-discipline">🥊 SparX Boxing</span></td><td>All Levels</td><td>Holmer Green Village Hall</td><td>Malcolm Wrigley</td></tr>')

# Replace Boxing instructor generally (Saturday)
sched = sched.replace('<tr><td>Saturday</td><td>9:30am – 10:15am</td><td><span class="badge-discipline">🥊 SparX Boxing</span></td><td>All Levels</td><td>Hazlemere Memorial Hall</td><td>CAMA Instructor</td></tr>',
                      '<tr><td>Saturday</td><td>9:30am – 10:15am</td><td><span class="badge-discipline">🥊 SparX Boxing</span></td><td>All Levels</td><td>Hazlemere Memorial Hall</td><td>Malcolm Wrigley</td></tr>')

# Find all remaining rows in schedule.html
# We want to replace 'CAMA Instructor' with the right person.
# Rule: If 'Little Chalfont' in row -> Sifu Steff
#       Else -> Sifu Mark Lane

def replace_instructor(match):
    row = match.group(0)
    # Check location
    if 'Little Chalfont' in row:
        row = row.replace('CAMA Instructor', 'Sifu Steff')
    elif 'CAMA Instructor' in row:
        row = row.replace('CAMA Instructor', 'Sifu Mark Lane')
    return row

# Regex to match a full tr inside the tbody (this requires care to just target table rows with CAMA Instructor)
sched = re.sub(r'<tr.*?>.*?CAMA Instructor.*?</tr>', replace_instructor, sched)

with open(sched_file, 'w') as f:
    f.write(sched)

print("Schedule updated!")
