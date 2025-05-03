# utils/icalendar_helpers.py
from icalendar import Calendar, Event
from datetime import datetime, timedelta
from uuid import uuid4

def add_recurring_event(cal, summary, start_time, end_time, day_of_week, start_date, end_date, is_busy):
    event = Event()
    event.add('summary', summary)
    start_dt = datetime.combine(start_date, start_time)
    end_dt = datetime.combine(start_date, end_time)

    event.add('dtstart', start_dt)
    event.add('dtend', end_dt)
    event.add('rrule', {
        'freq': 'weekly',
        'byday': ['MO', 'TU', 'WE', 'TH', 'FR'][day_of_week],
        'until': datetime.combine(end_date, end_time)
    })
    event.add('uid', str(uuid4()))
    event.add('transp', 'OPAQUE' if is_busy else 'TRANSPARENT')
    cal.add_component(event)
