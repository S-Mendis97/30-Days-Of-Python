print("\n### Exercise 16 ###")
print("------------------")


from datetime import datetime
now = datetime.now()

print("\n1. Current day, month, year, hour, minute, and timestamp")
print("Day:", now.day)
print("Month:", now.month)
print("Year:", now.year)
print("Hour:", now.hour)
print("Minute:", now.minute)
print("Timestamp:", now.timestamp())



formatted_date = now.strftime("%m/%d/%Y, %H:%M:%S")
print("\n2. Format the current date using this format: %m/%d/%Y, %H:%M:%S ->", formatted_date)



date_string = "5 December, 2019"
date_object = datetime.strptime(date_string, "%d %B, %Y")

print("\n3. Today is 5 December, 2019. Change this time string to time ->", date_object)



new_year = datetime(now.year + 1, 1, 1)
time_to_new_year = new_year - now

print("\n4. Calculate time difference between now and new year:", time_to_new_year)



date_1970 = datetime(1970, 1, 1)
time_since_1970 = now - date_1970

print("\n5. Calculate time difference between now and 1 January 1970:", time_since_1970)


print("\n6. What can the datetime module be used for?")
print("- Time series analysis")
print("- Recording timestamps of activities")
print("- Adding timestamps to blog posts")
print("- Calculating ages")
print("- Calculating deadlines and time differences")
print("- Scheduling events\n")