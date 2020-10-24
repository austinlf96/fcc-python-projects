class Rectangle:

	def __init__(self, width, height):
		self.width = width
		self.height = height

	def __str__(self):
		return self.__class__.__name__ + "(width=" + str(self.width) + ", height=" + str(self.height) + ")"

	def set_width(self, width):
		self.width = width

	def set_height(self, height):
		self.height = height

	def get_area(self):
		return self.width * self.height

	def get_perimeter(self):
		return (2 * self.width) +(2 * self.height)

	def get_diagonal(self):
		return ((self.width ** 2) + (self.height ** 2)) ** .5

	def get_picture(self):
		picture = ""
		if self.width > 50 or self.height > 50:
			return "Too big for picture."
		else:
			for x in range(0, self.height):
				line = ""
				for y in range(0, self.width):
					line += "*"
				line += "\n"
				picture += line
			return picture			

	def get_amount_inside(self, shape):
		fittingShapesNum = 0
		if self.width < shape.width:
			return fittingShapesNum
		elif self.height < shape.height:
			return fittingShapesNum
		else:
			fittingShapesNum = int(self.get_area()/shape.get_area())
			return fittingShapesNum

class Square(Rectangle):

	def __init__(self, side):
		super().__init__(side, side)
		#self.side = side
	def __str__(self):
		return self.__class__.__name__ + "(side=" + str(self.width) + ")"

	def set_side(self, side):
		super().set_width(side)
		super().set_height(side)
	

	
