from RobotArm import RobotArm

robotArm = RobotArm('exercise 7')

# Jouw python instructies zet je vanaf hier:


robotArm.moveRight(); n = 0

for i in range(30): 
    robotArm.grab(), robotArm.moveLeft(), robotArm.drop(), robotArm.moveRight(); n = n + 1
    if n == 6:
        robotArm.moveRight(), robotArm.moveRight() 
        n = 0; continue


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()