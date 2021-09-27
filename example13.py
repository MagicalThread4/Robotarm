from RobotArm import RobotArm

robotArm = RobotArm()
robotArm.randomLevel(1,7)

# Jouw python instructies zet je vanaf hier:

place = 1


for x in range(7):
    robotArm.grab()
    color = robotArm.scan()
    if len(color) == 0:
        break
    for y in range(place):
        robotArm.moveRight()
    robotArm.drop()
    place += 1
    for u in range(place):
        robotArm.moveLeft()
        
    



# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()