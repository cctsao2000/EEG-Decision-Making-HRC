import glob, os
import pandas as pd
import numpy as np 

def scorecalc(testdata, test_type):
    testdata.loc[testdata['Difficulty']=='E', ['Score']] = 6
    testdata.loc[testdata['Difficulty']=='D', ['Score']] = 12
    if test_type == 'pretest':
        testdata['Score'] = np.where(testdata['CorrectAns'] == testdata['Ans'], testdata['Score'], testdata['Score']/-3)  
        return pd.DataFrame([[testdata['Score'].sum()]])
    else:
        testdata['Score w/Robot'] = np.where(testdata['CorrectAns'] == testdata['Ans2nd'], testdata['Score'], testdata['Score']/-3)  
        testdata['Score'] = np.where(testdata['CorrectAns'] == testdata['Ans1st'], testdata['Score'], testdata['Score']/-3)  
        return pd.DataFrame([[testdata['Score'].sum(),testdata['Score w/Robot'].sum()]])

def acceptancecalc(testdata):
    testdata['Accept'] = np.where(testdata['RobotAns'] == testdata['Ans2nd'], 1, 0)  
    return pd.DataFrame([[testdata['Accept'].sum()]])

TESTSCORECOL = {'pretest':3,'test1':5,'test2':7}
TESTACCEPTANCECOL = {'test1':9,'test2':10}
def fillxlsx(filename):
    with pd.ExcelWriter('../EEG_Pilot.xlsx', mode='a',if_sheet_exists='overlay', engine='openpyxl') as writer:
        test_data = pd.read_csv(filename)
        file_split = filename.split('_')
        test_type = file_split[2][:-4]
        pid = int(file_split[1])
        scorecalc(test_data, test_type).to_excel(writer, sheet_name='Data', index=False, header=False, startrow=pid+1, startcol=TESTSCORECOL[test_type])
        if test_type != 'pretest':
            acceptancecalc(test_data).to_excel(writer, sheet_name='Data', index=False, header=False, startrow=pid+1, startcol=TESTACCEPTANCECOL[test_type])

def main():
    os.chdir('csv')
    for csvfile in glob.glob("*.csv"):
        fillxlsx(csvfile)

if __name__ == '__main__':
    main()