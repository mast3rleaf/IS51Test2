


"""
The program is trying to display the number of grades, the average grades, and the percentage of grades
that are above the average grade by using the scores listed in the Final.txt. There will two functions,
function1 will initialize the application and function2 will calculate the percentage of grades that are 
above the average grade.

function1 will be the main function to initialize the application by assigning the grades in Final.txt into a list
of integers and then calculating the average.
funtion2 will calculate the percent above average by taking the count of tests taken divided by the grade average.

The program will then ouput like so:
Number of grades:

Average grade:

Percentage of grades above average: 
"""

"""

#calculate_percent_above_average
count = 0
for grade in grades 
    if grade > avg 
return  (x * 100) / len(grades)

#main 
f = open('Final.txt')
grades = []
for line in f: 
    grades.append
"Number of grades:"
avg = 0
for grade in grades:
    avg += grade
avg /= len(grades)
"Average grade:", avg
"Percentage of grades above average:"

main
"""



def calculate_percent_above_average(grades, avg):
    count = 0
    for grade in grades:
        if (grade > avg):
            count += 1
    return ((count/len(grades))*100)

def main():
    f = open('Final.txt')
    grades = []
    for line in f:
        grades.append(int(line.strip()))
    print("Number of grades:", len(grades))
    avg = 0
    for grade in grades:
        avg += grade 
    avg = avg/len(grades)
    print("Average grade:", avg)
    print("Percentage of grades above average: {:.2f}%".format(calculate_percent_above_average(grades,avg)))

main()