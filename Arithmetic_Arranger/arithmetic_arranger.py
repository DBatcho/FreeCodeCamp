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

# below is all the test cases
"""
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
test_cases = [
    pytest.param(
        [['3801 - 2', '123 + 49']],
        '  3801      123\n'
        '-    2    +  49\n'
        '------    -----',
        'Expected different output when calling "arithmetic_arranger()" with ["3801 - 2", "123 + 49"]',
        id='test_two_problems_arrangement1'),
    pytest.param(
        [['1 + 2', '1 - 9380']],
        '  1         1\n'
        '+ 2    - 9380\n'
        '---    ------',
        'Expected different output when calling "arithmetic_arranger()" with ["1 + 2", "1 - 9380"]',
        id='test_two_problems_arrangement2'),
    pytest.param(
        [['3 + 855', '3801 - 2', '45 + 43', '123 + 49']],
        '    3      3801      45      123\n'
        '+ 855    -    2    + 43    +  49\n'
        '-----    ------    ----    -----',
        'Expected different output when calling "arithmetic_arranger()" with ["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]',
        id='test_four_problems_arrangement'),
    pytest.param(
        [['11 + 4', '3801 - 2999', '1 + 2', '123 + 49', '1 - 9380']],
        '  11      3801      1      123         1\n'
        '+  4    - 2999    + 2    +  49    - 9380\n'
        '----    ------    ---    -----    ------',
        'Expected different output when calling "arithmetic_arranger()" with ["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"]',
        id='test_five_problems_arrangement'),
    pytest.param(
        [['44 + 815', '909 - 2', '45 + 43', '123 + 49',
          '888 + 40', '653 + 87']],
        'Error: Too many problems.',
        'Expected calling "arithmetic_arranger()" with more than five problems to return "Error: Too many problems."',
        id='test_too_many_problems'),
    pytest.param(
        [['3 / 855', '3801 - 2', '45 + 43', '123 + 49']],
        "Error: Operator must be '+' or '-'.",
        '''Expected calling "arithmetic_arranger()" with a problem that uses the "/" operator to return "Error: Operator must be '+' or '-'."''',
        id='test_incorrect_operator'),
    pytest.param(
        [['24 + 85215', '3801 - 2', '45 + 43', '123 + 49']],
        'Error: Numbers cannot be more than four digits.',
        'Expected calling "arithmetic_arranger()" with a problem that has a number over 4 digits long to return "Error: Numbers cannot be more than four digits."',
        id='test_too_many_digits'),
    pytest.param(
        [['98 + 3g5', '3801 - 2', '45 + 43', '123 + 49']],
        'Error: Numbers must only contain digits.',
        'Expected calling "arithmetic_arranger()" with a problem that contains a letter character in the number to return "Error: Numbers must only contain digits."',
        id='test_only_digits'),
    pytest.param(
        [['3 + 855', '988 + 40'], True],
        '    3      988\n'
        '+ 855    +  40\n'
        '-----    -----\n'
        '  858     1028',
        'Expected solutions to be correctly displayed in output when calling "arithmetic_arranger()" with ["3 + 855", "988 + 40"] and a second argument of `True`.',
        id='test_two_problems_with_solutions'),
    pytest.param(
        [['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40'], True],
        '   32         1      45      123      988\n'
        '- 698    - 3801    + 43    +  49    +  40\n'
        '-----    ------    ----    -----    -----\n'
        ' -666     -3800      88      172     1028',
        'Expected solutions to be correctly displayed in output when calling "arithmetic_arranger()" with five arithmetic problems and a second argument of `True`.',
        id='test_five_problems_with_solutions'),
]
"""