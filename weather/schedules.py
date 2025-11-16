from dagster import ScheduleDefinition
from .jobs import daily_weather_job

daily_weather_schedule = ScheduleDefinition(
    job=daily_weather_job,
    cron_schedule="0 8 * * *",  # Every day at 8AM
)
