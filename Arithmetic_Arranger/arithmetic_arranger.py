#receives the arithmetic data and separates the strings into usable variables
def arithmetic_arranger(*args):
  index = 0
  probcount = 0
  num1 = []
  num2 = []
  arith_op = []
  prob_len = []
  equals = []
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
      return ("Error: Too Many Arguments Sent")

  index = 0

  for problem in problems:

    probcount += 1

    #find position of operator
    #error check that it is + or -
    if problem.find('+') > 1:
      spos = problem.find('+')
    elif problem.find('-') > 1:
      spos = problem.find('-')
    else:
      return ("Error: Operator must be '+' or '-'.")

    #seperates the numbers/operator and saves them to corresponding list
    num1.append(str(problem[0:spos].strip()))
    num2.append(str(problem[spos + 1:].strip()))
    arith_op.append(str(problem[spos:spos + 1].strip()))

    #used to determine the length of the problem
    if len(num1[index]) > len(num2[index]):
      prob_len.append(len(num1[index]))
    else:
      prob_len.append(len(num2[index]))

    #Error check that there is not a number input greater than 4 digits long
    if prob_len[index] > 4:
      return ("Error: Numbers cannot be more than four digits.")

    #finds the answer
    #error checks that the nums variables only contain numerical values
    if arith_op[index] == '+':
      try:
        equals.append(str(int(num1[index]) + int(num2[index])))
      except Exception:
        return ("Error: Numbers must only contain digits.")
    else:
      try:
        equals.append(str(int(num1[index]) - int(num2[index])))
      except Exception:
        return ("Error: Numbers must only contain digits.")

    index = index + 1

  #Error checks that there is not more than 5 problems inputed
  if probcount > 5:
    return ("Error: Too many problems.")
  else:
    probcount -= 1

  #Below puts sets up the output and puts it into string (arranged_problems)

  #puts all first numbers into first line of string
  index = 0
  for num in num1:
    arranged_problems += "  "
    if len(num) >= prob_len[index]:
      arranged_problems += num
    else:
      space = len(num)
      while (space < prob_len[index]):
        arranged_problems += " "
        space = space + 1
      arranged_problems += num
    if probcount > index:
      arranged_problems += "    "
    index = index + 1

  arranged_problems += "\n"

  #puts arithmetic operators and second number into second line of string
  index = 0
  for num in num2:
    arranged_problems += arith_op[index] + " "
    if len(num) == prob_len[index]:
      arranged_problems += num
    else:
      space = len(num)
      while (space < prob_len[index]):
        arranged_problems += " "
        space += 1
      arranged_problems += num
    if probcount > index:
      arranged_problems += "    "
    index += 1

  arranged_problems += "\n"

  #puts dashes into third line of string
  index = 0
  for x in prob_len:
    dash = x
    arranged_problems += "--"
    while dash > 0:
      arranged_problems += "-"
      dash -= 1
    if probcount > index:
      arranged_problems += "    "
    index += 1

  #checks if user wants problem solved:
  #if yes, puts answers into fourth line of string
  index = 0
  if answers == True:
    arranged_problems += "\n"
    for num in equals:
      if len(num) > prob_len[index]:
        arranged_problems = arranged_problems + " " + num
      else:
        arranged_problems += "  "
        space = len(num)
        while (space < prob_len[index]):
          arranged_problems += " "
          space += 1
        arranged_problems += num
      if probcount > index:
        arranged_problems += "    "
      index += 1

  return arranged_problems

    
artprob = input("Please enter an Aritmetic Problem: ")
if len(artprob) < 1 : artprob = [['3 + 855', '988 + 40'], True]
print(arithmetic_arranger(artprob))