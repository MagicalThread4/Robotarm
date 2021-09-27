from RobotArm import RobotArm; robotArm = RobotArm('exercise 9')

# Jouw python instructies zet je vanaf hier:

left = 4; right = 5


for x in range(11):
    robotArm.grab(); color = robotArm.scan(); print(color)
    for r in range(right): robotArm.moveRight()
    robotArm.drop()
    for l in range(left): robotArm.moveLeft()
    robotArm.grab()
    if color == "green": left = 4  
    elif color == "white": left = 5
    elif color == "red": left = 6


    




# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()