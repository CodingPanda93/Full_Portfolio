from random import randint

print "Scores and Grades"
for count in range(1,10): #loops counting 1-100
    num = randint(70,100)
    if (num <=70):
        grade = "D"
    elif (num <=80):
        grade = "C"
    elif (num <=90):
        grade = "B"
    else:
        grade = "A"
    print "Score:", num, "; Your grade is", grade
print "End of the program. Bye!"
