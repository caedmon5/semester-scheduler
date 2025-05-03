# utils/icalendar_helpers.py
from datetime import datetime, timedelta
from icalendar import Event

def add_recurring_event(calendar, summary, start_time, end_time, weekday,
                        start_date, end_date, is_busy,
                        category=None, is_private=False):
    """
    Adds weekly recurring events to the calendar between start_date and end_date.

    Args:
        calendar: The icalendar.Calendar object to update.
        summary (str): The event title.
        start_time (datetime.time): Start time of the event.
        end_time (datetime.time): End time of the event.
        weekday (int): Day of the week (0=Monday ... 6=Sunday).
        start_date (datetime.date): First date to include.
        end_date (datetime.date): Last date to include.
        is_busy (bool): Whether to mark the time as busy.
        category (str or None): Optional category (e.g., "admin", "teaching").
        is_private (bool): Whether to add CLASS:PRIVATE to the event.
    """
    current = start_date
    while current.weekday() != weekday:
        current += timedelta(days=1)

    while current <= end_date:
        event = Event()
        start_dt = datetime.combine(current, start_time)
        end_dt = datetime.combine(current, end_time)
        event.add('dtstart', start_dt)
        event.add('dtend', end_dt)
        event.add('summary', summary)

        if is_busy:
            event.add('transp', 'OPAQUE')  # block time
        else:
            event.add('transp', 'TRANSPARENT')  # free time

        if is_private:
            event.add('class', 'PRIVATE')

        if category:
            event.add('categories', category)

        calendar.add_component(event)
        current += timedelta(days=7)
