# schedules/model.py
from datetime import time

# Example weekly schedule structure
# Format: ("Label", day_of_week, start_time, end_time, is_busy)
# day_of_week: 0 = Monday ... 6 = Sunday

schedule = [
    ("Morning Reading", 0, time(8, 0), time(9, 30), False),
    ("Team Check-in", 0, time(10, 0), time(11, 0), True),
    ("Deep Work Block", 1, time(9, 30), time(11, 30), True),
    ("Admin and Email", 2, time(14, 0), time(15, 30), True),
    ("Lab Meeting", 3, time(13, 0), time(14, 30), True),
    ("Project Planning", 4, time(10, 0), time(12, 0), True),
    ("Weekly Wrap-Up", 4, time(15, 0), time(16, 30), True),
]
