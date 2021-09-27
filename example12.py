from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')

# Jouw python instructies zet je vanaf hier:
place = 0
end  = 10
back = 0
right = 9
robotArm.speed = 1

for x in range(20):
    robotArm.grab()
    place += 1
    white = robotArm.scan()
    if white == 'red':
        back = end - place
        for x in range(back):
            robotArm.moveRight()
        robotArm.drop()
        for x in range(back):
            robotArm.moveLeft()
            place = 0
            back = 0
    else:
        robotArm.drop()
        robotArm.moveRight()




# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()