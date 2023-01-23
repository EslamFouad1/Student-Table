#!/usr/bin/env python
# coding: utf-8

# ## Student File Reader ADT:
# 
# **A student file reader is used to extract student records from external storage. The five data components of the individual records are extracted and stored in a storage object specific for this collection of student records.**
# 
# 1. StudentFileReader(filename): Creates a student reader instance for extracting student records from the given file. The type and format of the file is dependent on the specific implementation.
# 
# 2. open(): Closes the connection to the input source. If the connection is not currently open, an exception is raised.
# 
# 3. fetchRecord(): Extracts the next student record from the input source and returns a reference to a storage object containing the data. None is returned when there are no additional records to be extracted. An exception is raised if the connection to the input source was previously closed.
# 
# 4. fetchAll(): The same as fetchRecord(), but extracts all student records (or those remaining) from the input source and returns them in a Python list.

# In[5]:


# Produces a student report from data extracted from an external source.


"""
from studentfile import StudentFileReader

# Name of the file to open.
FILE_NAME = "students.txt"


"""

def main():
    #Extract the student records from the given text file.
    reader = StudentFileReader(FILE_NAME)
    reader.open()
    studentList = reader.fetchAll()
    reader.close()
    
    # Sort the list by id number. Each object is passed to the lambda
    # expression which returns the idNum field of the object.
    
    studentList.sort(key = lambda rec: rec.idNum)
    
    #Print the student report.
    printReport(studentList)
    
#Prints the student report.
def printReport(theList):
    # The class names associated with the class codes.
    classNames = (None, "Freshman", "Sophomore", "Junior", "Senior")
    
    # Print the header.
    print("LIST OF STUDENTS".center(50))
    print("")
    print("%-5s %-25s %-10s %-4s" % ('ID', 'NAME', 'CLASS', 'GPA'))
    print("%5s %25s %10s %4s" % ('-' * 5, '-' * 25, '-' * 10, '-' * 4))
    
    #Prints the body.
    
    for record in theList:
        print("%5d %-25s %-10s %4.2f" %              (record.idNum,              record.lastName + ', ' + record.firstName,
             classNames[record.classCode], record.gpa))
        
    # Add a footer
    print("-" * 50)
    print("Number of students: ", len(theList))
    
# Executes the main routine.
main()


# In[6]:


class StudentRecord:
    
    def __init__(self):
        self.idNum = 0
        self.firstName = None
        self.lastName = None
        self.classCode = 0
        self.gpa = 0.0


# In[7]:


# Listing 1.6 The studentfile.py module:

# Implementation of the StudentFileReader ADT using a text file as the
# input source in which each field is stored on a separate line.

class StudentFileReader:
    # Create a new student reader instance.
    
    def __init__(self, inputSrc):
        self._inputSrc = inputSrc
        self._inputFile = None
        
        # Open a connection to the input file.
    def open(self):
        self._inputFile = open(self._inputSrc, "r")
        
        # Close he connection to the input file.
    def close(self):
        self._inputFile.close()
        self._inputFile = None
        
        # Extract all student records and store them in a list.
    def fetchAlL(self):
        theRecords = list()
        student = self.fetchRecord()
        
        while student != None:
            theRecords.append(student)
            student = self.fetchRecord()
        return theRecords
    
    
    # Extract the next student record from the file.
    def fetchRecord(self):
        # Read the first line of the record.
        line = self._inputFile.readline()
        if line == "":
            return None
        
        # If there is another record, create a storage object and fill it.
        Student = StudentRecord()
        student.idNum = int(line)
        student.firstName = self._inputFile.readline().rstrip()
        student.lastName = self._inputFile.readline().rstrip()
        student.classCode = int(self._inputFile.readline())
        student.gpa = float(self._inputFile.readline())
        return student 
# Storage class used for an individual student record.

class StudentRecord:
    
    def __init__(self):
        self.idNum = 0
        self.firstName = None
        self.lastName = None
        self.classCode = 0
        self.gpa = 0.0


# In[ ]:




