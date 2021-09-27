from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')

# Jouw python instructies zet je vanaf hier:

num = 9; num2 = 8


for u in range(5):
    robotArm.grab()
    for x in range(num):
        robotArm.moveRight()
    robotArm.drop()
    num -= 2
    for y in range(num2):
        robotArm.moveLeft()
    robotArm.grab()
    num2 -= 2

robotArm.drop()

    

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()