import copy
import random
# Consider using the modules imported above.

class Hat:

	def __init__(self, **keywords):
		self.contents = []
		for balls in keywords:
			for x in range(0, keywords[balls]):
				self.contents.append(balls)

	def draw(self, numBalls):
		#contentsCopy = copy.copy(self.contents)
		removedBalls = []
		if numBalls >= len(self.contents):
			removedBalls = copy.deepcopy(self.contents)
			self.contents.clear()
			return removedBalls
		for x in range(0, numBalls):
			ballIndex = random.randint(0, len(self.contents) - 1)
			removedBall = self.contents.pop(ballIndex)
			removedBalls.append(removedBall)
		return removedBalls			

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
	attempts = 0	
	successes = 0
	for x in range(0, num_experiments):
		experimentHat = copy.deepcopy(hat)
		removedExperimentBalls = experimentHat.draw(num_balls_drawn)
		requiredBallsDrawn = True
		for ball in expected_balls:
			if removedExperimentBalls.count(ball) >= expected_balls[ball]:
				requiredBallsDrawn = True
			else: 
				requiredBallsDrawn = False
				break
		if requiredBallsDrawn:
			successes += 1
		attempts += 1
	return successes/attempts