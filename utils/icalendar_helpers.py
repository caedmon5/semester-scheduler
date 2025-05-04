from datetime import datetime, timedelta
from icalendar import Event

def add_recurring_event(cal, summary, start_time_str, end_time_str, day, start_date, end_date,
                         is_busy=True, category=None, is_private=False):
    day_map = {
        "MO": 0, "TU": 1, "WE": 2, "TH": 3, "FR": 4, "SA": 5, "SU": 6
    }

    if day not in day_map:
        raise ValueError(f"Invalid day: {day}")

    # Parse times
    start_time = datetime.strptime(start_time_str, "%H:%M").time()
    end_time = datetime.strptime(end_time_str, "%H:%M").time()

    # Find first occurrence of the correct day
    current = start_date
    while current.weekday() != day_map[day]:
        current += timedelta(days=1)

    event = Event()
    event.add("summary", summary)
    event.add("dtstart", datetime.combine(current, start_time))
    event.add("dtend", datetime.combine(current, end_time))
    event.add("rrule", {
        "freq": "weekly",
        "until": datetime.combine(end_date, end_time)
    })

    if is_busy:
        event.add("transp", "OPAQUE")
    else:
        event.add("transp", "TRANSPARENT")

    if category:
        event.add("categories", category)
    if is_private:
        event.add("class", "PRIVATE")

    cal.add_component(event)
