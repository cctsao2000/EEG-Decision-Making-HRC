import glob, os
EVENTDICT = {'QUESTION':1,'CONFIRM':2,'SUBMIT':3,'FINISHED':4}

def read_log_event(filename):
    event_data = []
    event_row = 0
    with open(filename, 'r') as f:
        for line in f.readlines():
            log_list = line.split()
            event_row += round(float(log_list[0])/4)
            event = EVENTDICT[log_list[1]]
            event_data.append([event_row, event])
            if event == 3:
                event_row = 1
            else:
                event_row = 0
    return event_data
        
def write_eeg_event(filename, eeg_event):
    with open(filename, 'r') as fr:
        eeg_data = []
        for line in fr.readlines()[:-1]:
            eeg_row = line.split()
            eeg_data.append(eeg_row)
        for event in eeg_event:
            eeg_data[event[0]-1][9] = event[1]
        with open(filename, 'w') as fw:
            text=''
            for row in eeg_data:
                for column in row:
                    text+=str(column)
                    text+=' '
                text+='\n '
            fw.write(text)

def main():
    os.chdir('logfile')
    for logfile in glob.glob('*test?.txt'):
        write_eeg_event(f'../eegevent/{logfile}',read_log_event(logfile))

if __name__ == '__main__':
    main()        