from datetime import datetime, timedelta
from icalendar import Event

def add_recurring_event(cal, summary, start_time_str, end_time_str, day, start_date, end_date,
                         is_busy=True, category=None, is_private=False):

    int_to_ical_day = ['MO', 'TU', 'WE', 'TH', 'FR', 'SA', 'SU']

    # Normalize `day` to iCalendar format
    if isinstance(day, int):
        try:
            ical_day = int_to_ical_day[day]
        except IndexError:
            raise ValueError(f"Invalid numeric day: {day}")
    elif isinstance(day, str) and day in int_to_ical_day:
        ical_day = day
    else:
        raise ValueError(f"Invalid day format: {day}")

    # Parse times
    if isinstance(start_time_str, str):
        start_time = datetime.strptime(start_time_str, "%H:%M").time()
    else:
        start_time = start_time_str

    if isinstance(end_time_str, str):
        end_time = datetime.strptime(end_time_str, "%H:%M").time()
    else:
        end_time = end_time_str

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
        "byday": ical_day,
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
