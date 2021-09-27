from RobotArm import RobotArm

robotArm = RobotArm('exercise 8')

# Jouw python instructies zet je vanaf hier:

robotArm.moveRight()

for i in range(7):
    robotArm.grab()
    for r in range(9):
        robotArm.moveRight()
    robotArm.drop()
    for l in range(8):
        robotArm.moveLeft(); continue





# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()