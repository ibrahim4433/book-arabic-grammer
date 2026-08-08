import re

with open('plans/page_164-plan_9kdou.md', 'r') as f:
    text = f.read()

text = text.replace('صَدْرًا: تَمْيِيزٌ مَنْسُوبٌ', 'صَدْرًا: تَمْيِيزٌ مَنْصُوبٌ')
text = text.replace('[POET_NAME]:', '[POET_NAME]: (1878 - 1946م)')

with open('plans/page_164-plan_9kdou.md', 'w') as f:
    f.write(text)
