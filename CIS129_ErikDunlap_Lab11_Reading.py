#Erik Dunlap
#CIS129 22853
#Program that read grades.txt


def main():
    print('Taken from grades.txt')
    with open('grades.txt', 'r') as grades:
        totalGrade= 0
        counter= 0
        first= True
        print(f'{"Grades":>7}{"Total":>8}{"Number":>8}{"Average":>9}')
        for grade in grades:
            grade= grade.strip()
            totalGrade+= float(grade)
            counter+= 1
        average= totalGrade/counter
        grades.seek(0)
        for grade in grades:
            grade= float(grade.strip())
            if first== True:
                print(f'{grade:>7.2f}{totalGrade:>8.2f}{counter:>8.2f}{average:>8.2f}')
                first= False
            else:
                print(f'{grade:>7.2f}')
            
main()          
