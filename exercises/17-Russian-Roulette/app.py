import random

bullet_position = 3

def spin_chamber():
	chamber_position = random.randint(1,6)
	return chamber_position

#  DON'T CHANGE THE CODE ABOVE
def fire_gun():
	if bullet_position == spin_chamber():
		return "You are dead madafaking!"
	else:
		return "Keep playing!"


print(fire_gun())