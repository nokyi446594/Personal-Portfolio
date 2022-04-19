from Student import Student
'''
Student121 class in Student121V2.py

Created on March 16, 2022

@author: dcywchan
'''
class Student121(Student):
    '''
    Student121 class to represent each 121COM student object
    '''
    CW1weight = 0.2 # class variable for weights for the coursework 1
    CW2weight = 0.2 # class variable for weights for the coursework 2 
    CW3weight = 0.6 # class variable for weights for the coursework 3
    
    CWweight = 0.7 # class variable for weights for the coursework 
    EXweight = 0.3 # class variable for weights for the exam 
       
    def __init__(self,dataLine):
        '''
        constructor method
        
        Parameters:
        - dataLine with following data feilds
            e.g. "50123456_lam tai man_85.5_80.0_80.0_90.0"
            - studID: student ID
            - name: name of student
            - test: test mark
            - iAsgn: individual assignment mark
            - gAsgn: group assignment mark
            - exam: exam mark
        '''
        studentRec=dataLine.split('_')
        Student.__init__(self,studentRec[0],studentRec[1])
        self.__iAsgn = float(studentRec[2])
        self.__test  = float(studentRec[3])
        self.__gAsgn = float(studentRec[4])
        self.__exam  = float(studentRec[5])
                
    def getTest(self):
        '''
        accessor method to get student test mark
        '''
        return self.__test
    
    def setTest(self, mark):
        '''
        mutator method to get student test mark
        '''
        self.__test = mark
    
    def getIAsgmt(self):
        '''
        accessor method to get student nindividual assignment mark
        '''
        return self.__iAsgn
    
    def setIAsgmt(self, mark):
        '''
        mutator method to set student individual assignment mark
        '''
        self.__iAsgn = mark
            
    def getGAsgmt(self):
        '''
        accessor method to get student group assignment mark
        '''
        return self.__gAsgn
    
    def setGAsgmt(self, mark):
        '''
        mutator method to get student group assignment mark
        '''
        self.__gAsgn = mark
    
    def getExam(self):
        '''
        accessor method to get student examination mark
        '''        
        return self.__exam        
    
    def setExam(self, mark):
        '''
        mutator method to set student examination mark
        '''        
        self.__exam = mark
    
    def getCoursework(self):
        '''
        accessor method to get student coursework mark
        '''              
        return Student121.CW1weight * self.getTest() + \
                Student121.CW2weight * self.getIAsgmt() + \
                Student121.CW3weight * self.getGAsgmt()
                   
    def overall(self):
        '''
        service method to calculate overall mark from the weighted sum of the coursework mark and the the exam mark
        '''
        return Student121.CWweight * self.getCoursework() + \
                Student121.EXweight * self.getExam()
           
    def __str__(self):
        '''
        String representation of student object
        '''
        return '%25s%10.2f%10.2f%10.2f%10.2f'%(Student.__str__(self),self.getIAsgmt(),self.getTest(),self.getGAsgmt(),self.getExam())