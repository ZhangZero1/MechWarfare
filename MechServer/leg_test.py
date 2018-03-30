from maestroInterface import MaestroInterface
from time import sleep

#Change port key's value in the JSON file accordingly
robot = MaestroInterface('myConfigLegs')
robot.open_connection()

def test_single_servos(robot_obj, pos):
    for i in range(12):
        robot_obj.send_single_command(i, pos)
        print "Moving servo {}".format(i)
        #Change sleep time as you wish
        sleep(2)

def test_each_leg(robot_obj, pos):
    leg_pos = [pos, pos, pos]
    for i in range(0, 12, 3):
        robot_obj.send_multi_command(i, 3, leg_pos)
        print "Moving leg {}".format(i/3 + 1)
        sleep(2)
        
def test_whole_robot(robot_obj, pos):
    leg_pos = [pos]*12
    robot_obj.send_multi_command(0, 12, leg_pos)
    print "Moving all servos to {}".format(leg_pos[0])
    sleep(2)
    
def main():
    Y,N = 0,1
    i = input("Enter capital Y to run the test \
    series function main(), \
    or capital N to go straight to python shell")
    if i==1:
        print "Your robot object's variable name is 'robot'(no quotations)"
        print "Test functions: test_single_servos(robot), \
        test_each_leg(robot), test_whole_robot(robot)"
        return
    test_single_servos(robot, 1400)
    test_each_leg(robot, 1600)
    test_whole_robot(robot, 1400)
    
if __name__=='__main__':
    main()
    
    
