# 📆 Semester Scheduler

Generate `.ics` calendar files from structured weekly schedule templates. Designed to support academic planning for teaching, research, and admin tasks across terms.

---

## 🚀 Quick Start

Generate a calendar:

```bash
python generate_schedule.py --source fall2025 --output data/fall_schedule.ics --start 2025-09-01 --end 2025-12-15
```

- `--source` refers to a file like `schedules/private/fall2025.py`
- `--output` is the destination `.ics` file
- `--start` and `--end` set the date range (defaults: May–August)

---

## 📁 Directory Structure

```
schedules/
├── model.py            # Public sample
└── private/
    ├── .gitkeep
    ├── README.md       # Instructions for private use
    ├── summer2025.py   # User-defined, git-ignored
    └── fall2025.py

data/
├── .gitkeep
└── README.md           # Calendar outputs (git-ignored)

utils/
└── icalendar_helpers.py
```

---

## 📐 Schedule Format

Each schedule file defines a list of tuples like this:

```python
from datetime import time

schedule = [
    ("ENGL 3450A", 0, time(9, 0), time(9, 50), True, "teaching", False),
    ("Writing", 1, time(10, 0), time(12, 0), True, "research", False),
    ("Therapy", 3, time(14, 0), time(15, 0), True, "personal", True),
]
```

Tuple fields:
1. `summary` (str) — Event label
2. `weekday` (int) — 0=Mon ... 6=Sun
3. `start_time` (datetime.time)
4. `end_time` (datetime.time)
5. `is_busy` (bool)
6. `category` (str, optional)
7. `is_private` (bool, optional)

Only the first 5 fields are required. Additional metadata is optional.

---

## 🔐 Privacy Guidelines

- `schedules/private/` is git-ignored by default
- `.ics` files are not tracked either
- You may add `.gitkeep` and `README.md` to preserve folder visibility

Do **not** commit real schedules or calendar exports.

---

## 🧩 Modular & Reusable

This system is designed for easy reuse:
- Add or modify schedule files per semester
- Swap source files without changing your generator
- Use categories for future visualizations or filtered exports
