def add_time(start, duration, weekday = False):

  new_time = ()
  totalHours = ()
  totalMinutes = ()

  # split into hrs,minutes,PmAm
  Split = start.split(" ")
  Time = Split[0].split(":")
  AmPm = Split[1]
  Hour = int(Time[0])
  Minute = int(Time[1])

  #split duration
  durationSplit = duration.split(":")
  durationHour = int(durationSplit[0])
  durationMinute = int(durationSplit[1])

  #convert to miliatry 24hrs
  if AmPm == "PM" :
    Hour = Hour + 12

  #convert to minutes
  Minute = Minute + (Hour*60)
  durationMinute = durationMinute + (durationHour*60)

  #add times
  addMinutes = Minute + durationMinute

  #convert back to hrs and minutes
  totalMinutes = addMinutes % 60
  totalHours = int(addMinutes/60)

  #find hrs and days
  day = 0
  if totalHours > 24:
    day = int(totalHours/24)
    totalHours = totalHours % 24

  #find AmPm
  if totalHours > 11:
    AmPm = "PM"
  else:
    AmPm = "AM"

  #change hrs back to PM
  if totalHours > 12:
    totalHours = totalHours - 12
  if totalHours == 0:
    totalHours = 12

  #add 0
  if len(str(totalMinutes)) == 1:
    totalMinutes = "0" + str(totalMinutes)
  else:
    totalMinutes = str(totalMinutes)

  #print time
  new_time = str(totalHours) + ":" + str(totalMinutes) + " " + AmPm

  #find weekday
  if weekday:
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    pos = 0

    while True:
      if weekday.lower() == days[pos].lower():
        break
      pos = pos + 1
    pos = (pos + day) % 7

    totalDay = days[pos]
    new_time = new_time + ", " + totalDay

#print next day string
  if day != 0:
    if day == 1:
      new_time = new_time + " (next day)"
    else:
      new_time = new_time + " (" + str(day) + " days later)"

  return new_time