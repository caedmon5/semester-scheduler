# generate_schedule.py
import argparse
from datetime import datetime, date
from icalendar import Calendar
from load_schedule import get_schedule_module  # <== this is new
from utils.icalendar_helpers import add_recurring_event

def main():
    parser = argparse.ArgumentParser(description="Generate an ICS file from a structured weekly schedule.")
    parser.add_argument("--source", default="summer2025", help="Name of the schedule module in schedules/private (without .py)")
    parser.add_argument("--output", required=True, help="Path to output .ics file")
    parser.add_argument("--start", help="Start date in YYYY-MM-DD format (default: schedule default)")
    parser.add_argument("--end", help="End date in YYYY-MM-DD format (default: schedule default)")
    args = parser.parse_args()

    # Load selected schedule
    schedule, default_start, default_end = get_schedule_module(args.source)

    # Use provided dates or fall back to schedule defaults
    start_date = datetime.strptime(args.start, "%Y-%m-%d").date() if args.start else default_start
    end_date = datetime.strptime(args.end, "%Y-%m-%d").date() if args.end else default_end

    cal = Calendar()
    cal.add('prodid', '-//Semester Scheduler//')
    cal.add('version', '2.0')

    for entry in schedule:
        if len(entry) == 5:
            summary, day, start_time, end_time, is_busy = entry
            category = None
            is_private = False
            rrule = None
        elif len(entry) == 6:
            summary, day, start_time, end_time, is_busy, category = entry
            is_private = False
            rrule = None
        elif len(entry) == 7:
            summary, day, start_time, end_time, is_busy, category, is_private = entry
            rrule = None
        elif len(entry) == 8:
            summary, day, start_time, end_time, is_busy, category, is_private, rrule = entry
        else:
            raise ValueError(f"Invalid schedule entry length: {len(entry)} fields")

        add_recurring_event(cal, summary, start_time, end_time, day, start_date, end_date,
                            is_busy, category, is_private, rrule)


    with open(args.output, 'wb') as f:
        f.write(cal.to_ical())

if __name__ == "__main__":
    main()
