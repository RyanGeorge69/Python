from datetime import datetime

now = datetime.now()  # current date and time

year = now.strftime("%Y")
print("Year:", year)

month = now.strftime("%m")
print("Month:", month)

day = now.strftime("%d")
print("Day:", day)

hour_24 = now.strftime("%H")
print("Hour (24-hour):", hour_24)

hour_12 = now.strftime("%I")
print("Hour (12-hour):", hour_12)

minute = now.strftime("%M")
print("Minute:", minute)

second = now.strftime("%S")
print("Second:", second)

am_pm = now.strftime("%p")
print("AM/PM:", am_pm)

weekday_name = now.strftime("%A")
print("Weekday Name:", weekday_name)

weekday_abbr = now.strftime("%a")
print("Weekday Abbreviation:", weekday_abbr)

month_name = now.strftime("%B")
print("Month Name:", month_name)

month_abbr = now.strftime("%b")
print("Month Abbreviation:", month_abbr)

week_number = now.strftime("%U")
print("Week number (Sunday as first day):", week_number)

day_of_year = now.strftime("%j")
print("Day of the year:", day_of_year)

timezone_name = now.strftime("%Z")
print("Timezone name:", timezone_name)

full_date_time = now.strftime("%c")
print("Locale’s appropriate date and time:", full_date_time)

iso_format = now.strftime("%x")
print("Locale’s appropriate date:", iso_format)

iso_time = now.strftime("%X")
print("Locale’s appropriate time:", iso_time)
