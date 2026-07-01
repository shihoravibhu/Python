import datetime

birthDate = datetime.date(2006, 11, 7)
today = datetime.date.today()

age_days = today - birthDate

age_years = age_days.days // 365

print("Age in days:", age_days.days)
print("Age in years:", age_years)