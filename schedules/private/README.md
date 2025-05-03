# 🗂️ Private Schedules

This folder is for **your actual working schedules**, one file per semester.

These files are ignored by version control, **except for this README file** and `.gitkeep`, which preserve the folder and explain usage.

## 📄 Add Your Schedules

Create files like:

- `fall2025.py`
- `summer2025.py`

Each must define a list called `schedule`:

```python
from datetime import time

schedule = [
    ("Writing", 1, time(9, 0), time(11, 0), True),
    ("Teaching", 3, time(13, 30), time(14, 45), True),
]
