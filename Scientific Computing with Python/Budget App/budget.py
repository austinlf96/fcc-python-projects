class Category:
	
	def __init__(self, name):
		self.name = name
		self.ledger = []

	def __str__(self):
		if len(self.name) <= 30:
			name = self.name
		else:
			name = self.name[slice(30)]
		title = name.center(30, "*") + "\n"
		transcript = ""
		for entry in self.ledger:
			transactionDescription = entry["description"]
			transactionAmount = "{:.2f}".format(entry["amount"])
			if len(entry["description"]) > 23:
				transactionDescription = entry["description"][slice(23)]
			if len(str(entry["amount"])) > 7:
				transactionAmount = "1000+"
			transcript += transactionDescription + str(transactionAmount.rjust(30 - len(transactionDescription))) + "\n"
		return title + transcript + "Total: " + str(self.get_balance()) 

	def deposit(self, amount, description =""):
		deposit = {"amount": amount, "description": description}
		self.ledger.append(deposit)

	def withdraw(self, amount, description = ""):
		if self.check_funds(amount):
			withdraw = {"amount": -amount, "description": description}
			self.ledger.append(withdraw)
			return True
		else:
			return False
	
	def get_balance(self):
		balance = 0
		for entry in self.ledger:
			balance += entry["amount"]
		return balance

	def transfer(self, amount, Category):
		if self.check_funds(amount):
			self.withdraw(amount, "Transfer to " + Category.name)
			Category.deposit(amount, "Transfer from " + self.name)
			return True
		else: 
			return False

	def check_funds(self, amount):
		if self.get_balance() < amount:
			return False
		else:
			return True

	def get_expenses(self):
		expenses = 0
		for transaction in self.ledger:
			if transaction["amount"] < 0:
				expenses += transaction["amount"]
		return round(expenses,2)

def create_spend_chart(categories):
	title = "Percentage spent by category\n"
	verticalTicks = ["100| ", " 90| ", " 80| ", " 70| ", " 60| ", " 50| ", " 40| ", " 30| ", " 20| ", " 10| ", "  0| "]
	verticalSpace = "\n"
	horizontalAxis = "\n    -"
	horizontalSpace = "\n"
	horizontalTicks = []
	totalSpent = 0
	longestNumLetters = 0

	if len(categories) < 1:
		return ("Error: No data selected")
	
	for category in categories:
		totalSpent += category.get_expenses()
		horizontalAxis += "---"
		if len(category.name) > longestNumLetters:
			longestNumLetters = len(category.name)
	
	for x in range(longestNumLetters):
		horizontalTicks.append("     ")

	for category in categories:
		percentOs = int((category.get_expenses()/totalSpent) * 10)
		for x in range(1, len(verticalTicks) + 1):
			if x <= percentOs + 1:
				verticalTicks[-x] += "o".ljust(3," ")
			else:
				verticalTicks[-x] += "   "
		for x in range(0, longestNumLetters):
			if x < len(category.name):
				horizontalTicks[x] += category.name[x].ljust(3," ")
			else:
				horizontalTicks[x] += "   "


	verticalSpace = verticalSpace.join(verticalTicks)
	horizontalAxis += "\n"
	horizontalSpace = horizontalSpace.join(horizontalTicks)
	return title + "\n".join(verticalTicks) + horizontalAxis + "\n".join(horizontalTicks)
	