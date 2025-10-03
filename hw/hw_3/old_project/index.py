from datetime import date, timedelta, datetime
from loguru import logger

launch_date = date(day=10, month=2, year=2022)

print(launch_date)
print(type(launch_date))

# =================================

delta = timedelta(days=42)

some_future = launch_date + delta

print(some_future)

# =================================


times = datetime(month=3, day=8, year=2022) + timedelta(days=3, hours=5, minutes=6)
print(times)
print(type(times))


# =================================


logger.info("program started")
