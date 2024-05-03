#Erik Dunlap
#CIS129 22853
#Program that records any number of grades


def main():
    allGrades= []
    print('This is for recording your students grades')
    print('If you are not a teacher please immediately enter \'y\'')
    print('Enter \'y\' any time to stop')
    while True:
        grade = getValidFloatOrSentinel('Enter a student\'s grade: ')
        if grade== 'y' and allGrades== []:
            print('No Grades Entered')
            break
        elif grade== 'y':
            with open('grades.txt', mode='w') as grades:
                for number in range(len(allGrades)):
                    grades.write(f'{allGrades[number]:>6.2f}\n')
            print('Grades successfully saved as grades.txt')
            break
        else:
            allGrades+= [grade]
    print('Thank you for using the program')


def getValidFloatOrSentinel(msg):
    '''Returns a float between 100 and 0 or the sentinel'''
    while True:
        userInput= input(msg)
        if userInput== 'y':
            return userInput
        try:
            validInput= float(userInput)
            if 100>= validInput >= 0:
                return validInput
            else:
                print('Invalid Number')
        except ValueError:
            if 'a' <= userInput.lower() <= 'd' or userInput.lower()== 'f':
                print('Please enter a number')
            else:
                print('Invalid Input')

main()
