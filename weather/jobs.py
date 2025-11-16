from dagster import define_asset_job

daily_weather_job = define_asset_job("daily_weather_job", selection=["daily_weather"])
