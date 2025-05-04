## 📅 Generating a Schedule

To generate a `.ics` calendar file from a semester schedule, use:

```bash
python generate_schedule.py --source summer2025 --output data/summer2025.ics --start 2025-05-01 --end 2025-08-30
```

### 🧾 Arguments

| Argument       | Required | Description                                                                 |
|----------------|----------|-----------------------------------------------------------------------------|
| `--source`     | No       | The name of the schedule module (default: `summer2025`).                    |
| `--output`     | Yes      | Path where the `.ics` file should be saved.                                 |
| `--start`      | No       | Start date for recurring events (default set by `load_schedule.py`).        |
| `--end`        | No       | End date for recurring events (default set by `load_schedule.py`).          |

---

### 🗂 Schedule Source Files

Place your structured weekly schedule tuples in:

```
schedules/private/summer2025.py
schedules/private/fall2025.py
```

Each file should define a `schedule` list in this format:

```python
from datetime import time

schedule = [
    ("Event Title", weekday, start_time, end_time, is_busy, category, is_private),
]
```

---

### 🔁 Customizing Sources

To add a new schedule module (e.g., `spring2026.py`), create it in `schedules/private/`, then update `load_schedule.py`:

```python
elif source == "spring2026":
    from schedules.private import spring2026 as module
    return module.schedule, date(2026, 1, 1), date(2026, 4, 30)
```
