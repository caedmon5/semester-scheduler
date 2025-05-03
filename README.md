# Semester Scheduler

Generate `.ics` calendar files from structured weekly routines. Designed for academics or professionals who work in recurring cycles (e.g. teaching semesters, writing blocks, supervision, or admin).

This project supports modular calendar planning with reusable schedule definitions for each semester.

## 🔐 Privacy Best Practices

We strongly recommend:

- Storing your real schedule in `schedules/private.py`
- Adding `schedules/private.py` and `*.ics` to your `.gitignore`
- Never committing actual calendar files or personal data

---

## 🚀 Quick Start

### 1. Install requirements

```bash
pip install icalendar
```

### 2. Generate a calendar

```bash
python generate_schedule.py --semester summer --output summer2025.ics
```

This will create a calendar file based on the summer schedule defined in `schedules/model.py`.

---

## 📁 Project Structure

```text
semester-scheduler/
├── generate_schedule.py         # CLI entry point
├── schedules/
│   ├── model.py                 # Sample weekly schedule (template)
│   └── private.py (ignored)     # Optional personal schedule
├── utils/
│   └── icalendar_helpers.py     # Event logic
├── data/
│   └── output/                  # ICS files (optional)
├── .gitignore
└── README.md
```

---

## 🧩 Using Your Own Schedule

The default configuration uses `schedules/model.py`.

To customize:

1. Copy the template:

    ```bash
    cp schedules/model.py schedules/private.py
    ```

2. Open `generate_schedule.py` and replace:

    ```python
    from schedules.model import schedule
    ```

    with:

    ```python
    from schedules.private import schedule
    ```

3. Edit `schedules/private.py` with your real schedule.

We recommend adding this line to `.gitignore`:

```gitignore
schedules/private.py
```

---

## 📅 Event Format

Each schedule is a list of 5-tuples:

```python
("Label", day_of_week, start_time, end_time, is_busy)
```

Where:
- `day_of_week`: 0 = Monday, ..., 6 = Sunday
- `is_busy`: if `True`, event blocks availability (shown as busy)

Example:

```python
("Writing", 1, time(9, 0), time(11, 0), True)
```

---

## 🛠️ Roadmap

- [ ] Add support for biweekly events
- [ ] Export Google Calendar import instructions
- [ ] Support for holidays and exceptions

---

## 📝 License

MIT License (see LICENSE file)

---

## 👤 Maintainer

[caedmon5](https://github.com/caedmon5)
