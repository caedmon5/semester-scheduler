from datetime import date

def get_schedule_module(source):
    if source == "summer2025":
        from schedules.private import summer2025 as module
        return module.schedule, date(2025, 5, 1), date(2025, 8, 30)
    elif source == "fall2025":
        from schedules.private import fall2025 as module
        return module.schedule, date(2025, 9, 1), date(2025, 12, 15)
    else:
        raise ValueError(f"Unknown source module: {source}")
