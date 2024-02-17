def add_time(start, duration, day=None):
  #parse start_time
  #Convert to 12-hour format
  #cool map function
  start_time, period = start.split()
  start_hour, start_minute = map(int, start_time.split(':'))

  #parse the duration time
  duration_hour, duration_minute = map(int, duration.split(':'))

  #calculate new time
  new_hour = start_hour + duration_hour
  new_minute = start_minute + duration_minute

  if period == "PM":
    new_hour += 12

  #remainder issues minutes
  new_hour += new_minute // 60
  new_minute %= 60

  #remainder issues hours
  # // floor devision whole number
  #want to see how many days we are on
  days_passed = new_hour // 24
  new_hour %= 24

  #What is final day of the week
  if day:
    days = [
        "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",
        "Sunday"
    ]
    day_index = (days.index(day.capitalize()) + days_passed) % 7
    new_day = days[day_index]

  #f strings are new and cool
  next_day = ""
  if days_passed == 1:
    next_day = " (next day)"
  elif days_passed > 1:
    next_day = f" ({days_passed} days later)"

  #AM/PM block
  if new_hour >= 12:
    new_hour -= 12
    period = "PM"
  else:
    period = "AM"

  #Edge case
  if new_hour == 0:
    new_hour = 12

  new_time = f"{new_hour}:{new_minute:02} {period}"

  #add day of week
  if day:
    new_time += f", {new_day}"

  #add next day or days later
  new_time += next_day

  return new_time
