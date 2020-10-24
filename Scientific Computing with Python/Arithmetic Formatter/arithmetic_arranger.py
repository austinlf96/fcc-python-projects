import re

def arithmetic_arranger(problems, answers= False):
	spaces = {
		0: "",
		1: " ",
		2: "  ",
		3: "   ",
		4: "    ",
		5: "     "
	}
	dashes = {
		1: "---",
		2: "----",
		3: "-----",
		4: "------"
	}
	if len(problems) > 5:
		return "Error: Too many problems."
	else:
		topString = ""
		bottomString = ""
		dashString = ""
		answerString = ""
		for prob in problems:
			parts = prob.split()

			if len(parts) > 3: 
				return "Error: Invalid problem. Please try again."
			if validate(parts[0]) != "Safe":
				return validate(parts[0])
			if validate(parts[2]) != "Safe":
				return validate(parts[2])
			if parts[1] != "+" and parts[1] != "-":
				return "Error: Operator must be '+' or '-'."
			
			answer = solver(parts[0], parts[1], parts[2])
			#print(str(len(str(answer))) + " - " + str(answer))
			if len(parts[0]) > len(parts[2]):

				space = spaces.get(len(parts[0]) - len(parts[2]))
				topString = topString + spaces.get(2) + str(parts[0])
				bottomString = bottomString + str(parts[1]) + " " + space + str(parts[2])
				dashString = dashString + dashes.get(len(parts[0]))
				if answers: 
					if len(str(answer)) == 5:
						specialSpace = spaces.get(1)
					else:
						specialSpace = spaces.get(len(dashes.get(len(parts[0]))) - len(str(answer)))
					answerString = answerString + specialSpace + str(answer)

			elif len(parts[0]) < len(parts[2]):

				space = spaces.get(len(parts[2]) - len(parts[0]))
				topString = topString + spaces.get(2) + space + str(parts[0])
				bottomString = bottomString + str(parts[1]) + " " + str(parts[2])
				dashString = dashString + dashes.get(len(parts[2]))
				if answers: 
					if len(str(answer)) == 5:
						specialSpace = spaces.get(1)
					else:
						specialSpace = spaces.get(len(dashes.get(len(parts[2]))) - len(str(answer)))
					answerString = answerString + specialSpace + str(answer)

			else: 

				topString = topString +spaces.get(2) + str(parts[0])
				bottomString = bottomString + str(parts[1]) + " " + str(parts[2])
				dashString = dashString + dashes.get(len(parts[0]))
				if answers: 
					if len(str(answer)) == 5:
						specialSpace = spaces.get(1)
					else:
						specialSpace = spaces.get(len(dashes.get(len(parts[2]))) - len(str(answer)))
					answerString = answerString + specialSpace + str(answer)
			if prob == problems[len(problems) - 1]:
				break
			topString = topString + spaces.get(4)
			bottomString = bottomString + spaces.get(4)
			dashString = dashString + spaces.get(4)
			if answers:
				answerString = answerString + spaces.get(4)
			#print(topString + "\n" + bottomString + "\n" + dashString + "\n")
		if answers:
			arranged_problems = topString + "\n" + bottomString + "\n" + dashString + "\n" + answerString
		else:	
			arranged_problems = topString + "\n" + bottomString + "\n" + dashString 
		print("\n" + arranged_problems)
		return arranged_problems

def solver(num1, operator, num2):
	if str(operator) == "+":
		result = int(num1) + int(num2)
	elif str(operator) == "-":
		result = int(num1) - int(num2)
	else: 
		return "Error: Operator must be '+' or '-'."
	return result

def validate(number):
	if len(number) > 4:
		return "Error: Numbers cannot be more than four digits."
	elif len(number) < 1:
		return "Error: No number present"
	else: 
		if re.search('\D', str(number)):
			return "Error: Numbers must only contain digits."
		else: 
			return "Safe"