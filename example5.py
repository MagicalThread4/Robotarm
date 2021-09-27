from RobotArm import RobotArm

robotArm = RobotArm('exercise 5')

# Jouw python instructies zet je vanaf hier: 
robotArm.moveRight(), robotArm.grab()


j = 1   
while j < 8:
    for i in range(8): robotArm.moveRight()
    robotArm.drop()
    for i in range(8): robotArm.moveLeft()
    robotArm.grab()
    j =  j + 1


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()