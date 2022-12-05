import glob, os
import csv

# 受測者編號-pretest.csv
# 題號, 難度, 正確答案, 作答時間, 受測者答案
# 受測者編號-test1/test2.csv
# 題號, 難度, 正確答案, 機器人答案, 第一次作答時間, 第一次受測者答案, 第二次作答時間, 第二次受測者答案
PRETEST = ['B', 'C', 'C', 'B', 'B', 'D']
PRETEST_DIFFICULTY = ['E','D','E','D','E','D']
# high ability
TEST1   = ['C', 'C', 'D', 'B', 'A', 'D']
ROBOT1  = ['C', 'C', 'D', 'A', 'A', 'B']
TEST1_DIFFICULTY = ['E','E','D','D','E','D']
# low ability
TEST2   = ['B', 'C', 'A', 'D', 'B', 'C']
ROBOT2  = ['A', 'C', 'A', 'C', 'D', 'B'] 
TEST2_DIFFICULTY = ['D','E','E','D','D','E']

def pretest_data(filename, difficulty, answers):
    data = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            timecode = line.split()
            if timecode[1] == 'QUESTION':
                q = int(timecode[2]) # 問題編號
                qt = round(float(timecode[0]))
            elif timecode[1] == 'SUBMIT':
                s = timecode[2] # 答案
                st = round(float(timecode[0]))
                data.append([q, difficulty[q-1], answers[q-1], st - qt, s])

    with open(f'../csv/{filename[:-4]}.csv', 'w', newline='') as output:
        writer = csv.writer(output)
        writer.writerow(['QID', 'Difficulty', 'CorrectAns', 'Time(ms)', 'Ans'])
        for d in data:
            writer.writerow(d)

def test_data(filename, difficulty, answers, robots):
    data = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            timecode = line.split()
            if timecode[1] == 'QUESTION':
                q = int(timecode[2])  # 問題編號
                qt = round(float(timecode[0]))
            elif timecode[1] == 'CONFIRM':
                c = timecode[2]  # 第一次答案
                ct = round(float(timecode[0]))
            elif timecode[1] == 'SUBMIT':
                s = timecode[2]  # 第二次答案
                st = round(float(timecode[0]))
                data.append([q, difficulty[q-1], answers[q-1], robots[q-1], ct - qt, c, st - ct, s])

    with open(f'../csv/{filename[:-4]}.csv', 'w', newline='') as output:
        writer = csv.writer(output)
        writer.writerow(['QID', 'Difficulty', 'CorrectAns', 'RobotAns', 'Time1st(ms)', 'Ans1st', 'Time2nd(ms)', 'Ans2nd'])
        for d in data:
            writer.writerow(d)

def output_csv(filename):
    test_type = filename[9:-4]
    if test_type == 'pretest':
        pretest_data(filename,PRETEST_DIFFICULTY, PRETEST)
    elif test_type == 'test1':
        test_data(filename,TEST1_DIFFICULTY, TEST1, ROBOT1)
    elif test_type == 'test2':
        test_data(filename,TEST2_DIFFICULTY, TEST2, ROBOT2)   

def main():
    os.chdir('logfile')
    for logfile in glob.glob('*.txt'):
        output_csv(logfile)

if __name__ == '__main__':
    main()