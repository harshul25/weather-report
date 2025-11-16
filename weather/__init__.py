from dagster import Definitions
from .assests import daily_weather
from .jobs import daily_weather_job
from .schedules import daily_weather_schedule

defs = Definitions(
    assets=[daily_weather],
    jobs=[daily_weather_job],
    schedules=[daily_weather_schedule],
)
