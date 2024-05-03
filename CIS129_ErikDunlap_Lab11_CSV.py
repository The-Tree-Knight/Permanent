#Erik Dunlap
#CIS129 22853
#Program to allow a teacher to record a student's exam grades in a CSV

import csv

def main():
    studentFirstName= []
    studentLastName= []
    studentGrade1= []
    studentGrade2= []
    studentGrade3= []
    teacherName= 'David'
    answer= getYOrN(f'Hello {teacherName}. this program is to convert student grades into\
computer readable material. Are you ready to start?\n')
    if answer== 'yes':
        while answer== 'yes':
            studentFirstName+= [getValidName('Enter the Student\'s First Name: ')]
            studentLastName+= [getValidName('Enter the Student\'s Last Name: ')]
            studentGrade1+= [getValidGrade('Enter the Student\'s First Exam Score: ')] 
            studentGrade2+= [getValidGrade('Enter the Student\'s Second Exam Score: ')]
            studentGrade3+= [getValidGrade('Enter the Student\'s Third Exam Score: ')]
            answer= getYOrN('Do you want to go again?: ')
        with open('grades.csv', mode='w', newline='') as grades:
            writer= csv.writer(grades)
            for i in range(len(studentFirstName)):
                writer.writerow([studentFirstName[i], studentLastName[i], studentGrade1[i], studentGrade2[i], studentGrade3[i]])
            print('Successfully saved as grades.csv')
            print('Thank you for using this program')
    else:
        print('No Grades Entered')

def getYOrN(msg):
    '''Gets a yes or no answer from a user'''
    while True:
        answer= input(msg).lower()
        if answer== 'y' or answer== 'ye' or answer== 'yes':
            return 'yes'
        elif answer== 'n' or answer== 'no':
            return 'no'
        else:
            print('Invalid Answer')

def getValidName(msg):
    '''Gets a non-empty name'''
    while True:
        name= input(msg)
        checkEmptyName= list(name)
        inspectedName= removeSpaces(checkEmptyName)
        if inspectedName== []:
            print('Please enter non-spaces')
        else:
            name= name.strip()
            return name

def getValidGrade(msg):
    '''Get's a student's exam score as a number'''
    while True:
        try:
            userInt= input(msg)
            validInt= int(userInt)
            return validInt
        except ValueError:
            if 'a' <= userInt.lower() <= 'd' or userInt.lower()== 'f':
                print('Input as a number')
            else:
                print('Invalid Input')

def removeSpaces(word):
    '''Takes a list and removes the spaces'''
    word2= word.copy()
    for i in range(len(word2)):
        if word2[i]== ' ':
            word.remove(' ')
    return word
                    
main()
