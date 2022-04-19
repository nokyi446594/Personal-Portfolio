from Student import Student
from Student121 import Student121
import fileinput
import matplotlib.pyplot as plt
import sys
test = []
data = [] # list of Student121 objects
error = ['Invalid Cw1mark','Invalid Testmark','Invalid Cw2mark','Invalid Exammark']#error name
def is_number(n):
    try:
        float(n)
        return True
    except ValueError:
        pass
def bubblesort(seq):

    for i in range(len(seq)-1):
        for j in range(len(seq)-1,i,-1):
            if seq[j-1].getName() > seq[j].getName():
                seq[j-1], seq[j] = seq[j], seq[j-1]
    
    return seq
 
def displayFile(datafile):
    for line in fileinput.input(datafile):
        sys.stdout.write(line)
        
def readData(datafile):
    '''
    readData() to read in student mark data and store in a list
    '''
    fileIn = open(datafile, 'r') # open inputfile using paramepasster datafile

    lines = fileIn.read().splitlines() # read in all transaction lines
    if len(lines) == 0 :
        raise Exception ('Empty input file ')
    for line in lines:
        test = line.split('_')  
        correct = True
        if len(test) != 6:#do not use the line which have less than or more than  datas
            sys.stderr.write(line + 'invalid date\n')
            correct = False
        if test[0] == '':#do not use lines which have missing data
            sys.stderr.write(line + 'missing studentID\n')
            correct = False
        elif test[1] == '':
            sys.stderr.write(line + 'missing studentName\n')
            correct = False    
        for i in range(4):#do not use line which have wrong mark
            if is_number(test[i+2]) != True :
                sys.stderr.write(line + error[i] + '\n')
                correct = False
                break
            elif float(test[i+2]) > 100 or float(test[i+2]) < 0 :
                sys.stderr.write(line + error[i] + '\n')
                correct = False
                break
        i = 0
        while i < Student.numStudent:# do not use duplicate data
            if data[i].getStudID() == test[0] and data[i].getName() == test[1] :
               sys.stderr.write(line + 'duplicate date\n')
               correct = False
               break
            elif data[i].getStudID() == test[0]:
                sys.stderr.write(line + 'or' + e + 'invalid studentid\n')
                correct = False
                break  
            else:
                i  += 1
        if correct == True :
            data.append(Student121(line)) # append each record to list of student data
def printalldata():
    '''
    menuItem2() to print valid student mark data 
    '''
    print('%-10s%-15s%10s%10s%10s%10s'%('Stud ID','Name','CW1 mark', 'Test mark',
                               'CW2 mark','Exam mark'))
    print('='*65)

    # loop to print out each components
    for e in data:
        print(e)

def adjustment():
    try:
        studentID = input("studentID: ")
        if studentID == '':
            raise Exception ('Invalid student ID')
        studentName = input("studentName: ")
        if studentName == '':
            raise Exception ('Invalid studentName')
        markQ = ["CW1mark: ","testMark: ","CW2mark: ","examMark: "]
        mark = ['','','','']
        for i in range(4):
            mark[i] = input(markQ[i])
            if mark[i] == '':
                raise Exception(error[i])
                break
            elif is_number(mark[i]) == False:
                raise Exception(error[i])
                break
            elif float(mark[i]) > 100 or float(mark[i]) < 0:
                raise Exception(error[i])
                break
        CW1mark = float(mark[0])
        testMark = float(mark[1])
        CW2mark = float(mark[2])
        examMark = float(mark[3])
        i = 0
        for i in range(Student.numStudent):
            if data[i].getStudID() == studentID:
                if data[i].getName() != studentName:
                   raise Exception('incorrect StudentID or StudentName ')
                else:
                    if data[i].getTest() != testMark:
                        data[i].setTest(testMark)
                    if data[i].getIAsgmt() != CW1mark:
                        data[i].setIAsgmt(CW1mark)
                    if data[i].getGAsgmt() != CW2mark:
                        data[i].setGAsgmt(CW2mark)
                    if data[i].getExam() != examMark:
                        data[i].setExam(examMark)
        if i == Student.numStudent:
            raise Exception ('Invalid student ID')
        
        overallmark()   

    except Exception as exception:
        sys.stderr.write(str(exception)+'\n')
   
def overallmark():
    '''
    menuItem4() to print student mark with overall result  
    '''
    print('%-10s%-15s%10s%10s%10s%10s%10s%10s'%('Stud ID','Name','CW1 mark', 'Test mark',
                               'CW2 mark','Exam mark','CW mark','Overall'))
    print('='*85)

    # loop to print out each components
    for e in bubblesort(data):
        print("%65s%10.2f%10.2f"%(e,e.getCoursework(),e.overall()))

def selectstudent():
    '''
    menuItem4() to print student mark with overall result < 40  
    '''
    print('%-10s%-15s%10s%10s%10s%10s%10s%10s'%('Stud ID','Name','CW1 mark', 'Test mark',
                               'CW2 mark','Exam mark','CW mark','Overall'))
    print('='*85)

    # loop to print out each components
    for e in bubblesort(data):
        if e.overall() < 40:
            print("%65s%10.2f%10.2f"%(e,e.getCoursework(),e.overall()))   
  
def plot():  

    fig = plt.figure(figsize=(10,8))    # width x height in inches
    ax1 = fig.add_subplot(111)     
    gradeFeq = {'A':0,'B':0,'C':0,'D':0,'F':0}
    
    for e in data:
        if e.overall() < 40:
            gradeFeq['F'] += 1
        elif e.overall() < 50:
            gradeFeq['D'] += 1            
        elif e.overall() < 65:
            gradeFeq['C'] += 1 
        elif e.overall() < 75:
            gradeFeq['B'] += 1   
        else:
            gradeFeq['A'] += 1                          
    
    ax1.bar(['A','B','C','D','F'],
        [gradeFeq['A'],gradeFeq['B'],gradeFeq['C'],gradeFeq['D'],gradeFeq['F']])
    ax1.set_xlabel('Grade')
    ax1.set_ylabel('Student Numbers')
    ax1.set_title('Grade Distribution')
    plt.show()     
                
def main():
    instructions = """\nEnter one of the following:
       1 to print the contents of input data file
       2 to print all valid input data
        3 to enter adjustment marks
       4 to print all students overall mark 
       5 to overall mark all students whose mark less than 40
       6 to plot distribution of grade
       Q to end \n"""
    
    while True:
        sys.stderr.flush()    
        sys.stdout.write (instructions)        
        choice = input( "Enter 1 to 6 " ) 
        sys.stdout.flush()
        
        if choice == "1":
            displayFile(sys.argv[1])
        elif choice == "2":
            printalldata()          
        elif choice == "3":
            adjustment()
        elif choice == "4":
            overallmark()
        elif choice == "5":
            selectstudent()
        elif choice == "6":
            plot()
        elif choice == "Q":
            break

    print ("End Grade Processing App")

if __name__ == "__main__":
    try:
        sys.argv = ['markdata1.dat','markdata2.dat']
        displayFile(sys.argv[1])
        readData(sys.argv[1])
        main()
    except IndexError as error:
        sys.stderr.write('Type \"python grade.py filename\" to run program\n')
    except Exception as error:
        sys.stderr.write(str(error)+'\n')
