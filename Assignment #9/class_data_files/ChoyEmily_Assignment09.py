"""
Name: Emily Choy
Date: 04/29/18
Program: Assignment #9
"""

# PART 1: prompt user to open a filename
try:
    filename = input ( "Enter a class file to open (ex: 'class_'): " )
    filename = filename + ".txt" 
    file_open = open(filename, "r")

except:
    print ("Sorry there is no such file.")

else: 
    print ("Successfully opened", filename)


# PART 2: grade the exams
    data = file_open.read()
    print("Successfully opened", filename)
    answerkey =["B","A","D","D","C","B","D","A","C","C","D","B","A","B","A","C","B","D","A","C","A","A","B","D","D"
    #cut apart data based on line breaks
    lines = alldata.split("\n")

    #visit each line in the file
    rejected = 0
    good = 0
    totalstudents = 0
    
    #list to hold each students score
    scores = []
    
    #go through each students answers
    for line in lines:
        studentinfo = line.split(",")
        if len(studentinfo) != 26:
            rejected += 1
            totalstudents += 1
        else:
            good +=1
            totalstudents += 1
            #grading goes here
            #get just the students answers in a list
            justanswers = studentinfo[1:]

            #accumulator to record the points each student receives
            studentscore = 0

            #go through each answer and see if its correct, wrong, or skipped
            for i in justanswers:
                if i == answerkey[justanswers.index(i)]:
                    studentscore += 4
                elif i != answerkey[justanswers.index(i)]:
                    studentscore -= 1                
                else:
                    studentscore += 0
                
                #add the score to the scores list
                scores.append(studentscore)
    print("Grade summary:")
    print("Total students:", totalstudents)
    print("Rejected:", rejected)
    print("Highest score:", max(scores))
    print("Lowest score:", min(scores))
