grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_1=list(students)
students_1.sort()
print(students_1[0:])
average_grades = [sum(grades[0])/len(grades[0]),sum(grades[1])/len(grades[1]),sum(grades[2])/len(grades[2]),sum(grades[3])/len(grades[3]),sum(grades[4])/len(grades[4])]
print(type(average_grades))
print(average_grades)
average = {students_1[0] : average_grades[0],students_1[1] : average_grades[1],students_1[2] : average_grades[2],students_1[3] : average_grades[3],students_1[4] : average_grades[4]}
print(average)
