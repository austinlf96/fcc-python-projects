def add_time(start, duration, weekday = False):
	#These are for proper case output
	days = {
		0: "Sunday", 
		1: "Monday", 
		2: "Tuesday", 
		3: "Wednesday",
		4: "Thursday", 
		5: "Friday", 
		6: "Saturday"
	}
	#These are for catching case errors
	lowerCaseDays = [
		"sunday", 
		"monday", 
		"tuesday", 
		"wednesday", 
		"thursday", 
		"friday", 
		"saturday"]
	start = start.split()
	duration = duration.split()
	startTime = start[0].split(":")
	durationTime = duration[0].split(":")
	daysLater = 0
	startHour = int(startTime[0])
	startMinutes = int(startTime[1])
	durationHour = int(durationTime[0])
	durationMinutes = int(durationTime[1])
	finalHour = 0
	finalMinutes = startMinutes + durationMinutes
	newDay = ""
	
	if weekday:
		if weekday.lower() in lowerCaseDays:
			index = lowerCaseDays.index(weekday.lower())		
			newDay = ", " + days.get(index)

	if start[1] == "PM":
		startHour += 12
	if finalMinutes < 10:
			finalMinutes = "0" + str(finalMinutes)
			finalHour = startHour + durationHour
	elif finalMinutes < 60:
			finalHour = startHour + durationHour
	elif finalMinutes >= 60:
		finalMinutes -= 60
		finalHour = startHour + durationHour + 1
		#Add zero to front of minutes
		if finalMinutes < 10:
			finalMinutes = "0" + str(finalMinutes)
			finalHour = startHour + durationHour + 1
	
	if finalHour == 0:
		finalTime = str("12:" + str(finalMinutes) + " AM")
	
	elif (finalHour < 12):
		finalTime = str(finalHour) + ":" + str(finalMinutes) + " AM" + newDay

	elif (12 <= finalHour and finalHour < 24):
		finalHour -= 12
		finalTime = str(str(finalHour) + ":" + str(finalMinutes) + " PM" + newDay)
		if finalHour == 0:
			finalTime = str("12:" + str(finalMinutes) + " PM" +newDay)
	elif (finalHour >= 24):
		daysLater = int(finalHour/24)
		if weekday:
			if weekday.lower() in lowerCaseDays:
				index = lowerCaseDays.index(weekday.lower())		
				newDay = ", " + days.get((index + daysLater)%7)
		finalHour -= daysLater * 24

		if daysLater == 1:
			daysLater = " (next day)"
		else:
			daysLater = " (" + str(daysLater) + " days later)"

		if finalHour == 0:
			finalTime = str("12:" + str(finalMinutes) + " AM" + newDay + daysLater)
		elif (finalHour < 12):
			finalTime = str(str(finalHour) + ":" + str(finalMinutes) + " AM" + newDay + daysLater)
		elif (12 < finalHour and finalHour < 24):
			finalHour -= 12
			finalTime = str(str(finalHour) + ":" + str(finalMinutes) + " PM" + newDay + daysLater)

	return finalTime