# generate_schedule.py
import argparse
from datetime import datetime, date
from icalendar import Calendar
from schedules.private import schedule
from utils.icalendar_helpers import add_recurring_event

def main():
    parser = argparse.ArgumentParser(description="Generate an ICS file from a private schedule.")
    parser.add_argument("--output", required=True, help="Path to output .ics file")
    parser.add_argument("--start", help="Start date in YYYY-MM-DD format (default: 2025-05-01)")
    parser.add_argument("--end", help="End date in YYYY-MM-DD format (default: 2025-08-30)")
    args = parser.parse_args()

    start_date = datetime.strptime(args.start, "%Y-%m-%d").date() if args.start else date(2025, 5, 1)
    end_date = datetime.strptime(args.end, "%Y-%m-%d").date() if args.end else date(2025, 8, 30)

    cal = Calendar()
    cal.add('prodid', '-//Semester Scheduler//')
    cal.add('version', '2.0')

    for summary, day, start_time, end_time, is_busy in schedule:
        add_recurring_event(cal, summary, start_time, end_time, day, start_date, end_date, is_busy)

    with open(args.output, 'wb') as f:
        f.write(cal.to_ical())

if __name__ == "__main__":
    main()
