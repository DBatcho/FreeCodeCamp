#receives the arithmetic data and separates the strings into usable variables
def arithmetic_arranger (*args):
    index = 0
    num1 = []
    num2 = []
    arith_op = []
    prob_len = []
    equals = []
    large_len = 0
    arranged_problems = ""
    answers = False

    for i in args:
        if index == 0:
            problems = i 
            index += 1
        elif index == 1:
            answers = i
            index += 1
        else:
            print("Error: Too Many Arguments Sent")
            quit()

    index = 0

    for problem in problems:

        #find position of operator
        #error check that it is + or -
        if problem.find('+') > 1:
            spos = problem.find('+')
        elif problem.find('-') > 1:
            spos = problem.find('-')
        else:
            print("Error: Operator must be '+' or '-'.")
            quit()
    
        #seperates the numbers/operator and saves them to corresponding list
        num1.append(str(problem[0 : spos].strip()))
        num2.append(str(problem[spos+1 : ].strip()))
        arith_op.append(str(problem[spos : spos+1].strip()))

        #used to determine the length of the problem
        if len(num1[index]) > len(num2[index]):
            large_len = len(num1[index])
        else:
            large_len = len(num2[index])

        #Error check that there is not a number input greater than 4 digits long
        if large_len > 4:
            print("Error: Numbers cannot be more than four digits.")
            quit()

        #finds the answer if user requested
        #error checks that the nums variables only contain numerical values
        if answers == True:
            if arith_op[index] == '+':
                try:
                    equals.append(str(int(num1[index]) + int(num2[index])))
                except:
                    print("Error: Numbers must only contain digits.")
                    quit()
            else:
                try:
                    equals.append(str(int(num1[index]) - int(num2[index])))
                except:
                    print("Error: Numbers must only contain digits.")
                    quit()

            #used to determine the length of the problem
            if large_len < len(equals[index]):
                large_len = len(equals[index])

        #saves the longest length of the problem to list
        prob_len.append(large_len)
        index = index + 1

    #Error checks that there is not more than 5 problems inputed
    if index > 5:
        print ("Error: Too many problems.")
        quit()


    #Below puts sets up the output and puts it into string (arranged_problems)
        
    
    #puts all first numbers into first line of string
    index = 0
    for num in num1:
        arranged_problems += "  "
        if len(num) >= prob_len[index]:
            arranged_problems += num + "    "
        else:
            space = len(num)
            while (space < prob_len[index]):
                arranged_problems += " "
                space = space + 1
            arranged_problems += num + "    "
        index = index + 1
    
    arranged_problems += "\n"

    #puts arithmetic operators and second number into second line of string
    index = 0
    for num in num2:
        arranged_problems += arith_op[index] + " "
        if len(num) == prob_len[index]:
            arranged_problems += num + "    "
        else:
            space = len(num)
            while (space < prob_len[index]):
                arranged_problems += " "
                space = space + 1
            arranged_problems += num + "    "
        index = index + 1
    
    arranged_problems += "\n"

    #puts dashes into third line of string
    for x in prob_len:
        index = x
        arranged_problems += "--"
        while index > 0:
            arranged_problems += "-"
            index = index - 1
        arranged_problems += "    "

    #checks if user wants problem solved:
    #if yes, puts answers into fourth line of string
    index = 0
    if len(equals) > 0:
        arranged_problems += "\n"
        for num in equals:
            arranged_problems += "  "
            if len(num) >= prob_len[index]:
                arranged_problems += num + "    "
            else:
                space = len(num)
                while (space < prob_len[index]):
                    arranged_problems += " "
                    space = space + 1
                arranged_problems += num + "    "
            index = index + 1

    return arranged_problems

    
artprob = input("Please enter an Aritmetic Problem: ")
if len(artprob) < 1 : artprob = ["2 + 698", "3801 - 2", "45 + 43", "123 + 49", "293 + 332"]
answers = input ("Do you want the answers: ")
if len(answers) < 1 : answers = True
print(arithmetic_arranger(artprob, answers))