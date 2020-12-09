# Checks if input is wrong
def error_finder(problems):

    def fails_individual_test(array, function):
    # Tests the values using the other defined functions
        for x in array:
            if function(x):
                return True
        
        return False


    def too_many_problems(problems):
    # Limit is Five
    # Error: Too many problems.
        if len(problems) > 5:
          return True
        else:
          return False
          

    def inappropriate_operator(problem):
    # Only + and -
    # Error: Operator must be '+' or '-'.
        y = 0

        for x in problem:
            if x == " ": # Finding white space
                break

            y = y + 1
        
        if problem[y + 1] == '+' or problem[y + 1] == '-':
            return False
        else:
            return True


    def not_only_digits(problem):
    # Only digits
    # Error: Operands must only contain digits.
        for x in problem:
            if x == ' ' or x == '+' or x == '-':
                continue
            elif '9' >= x >= '0':
                continue
            else:
                return True
                
        return False


    def above_operand_length(problem):
    # 4 digits in length
    # Error: Numbers cannot be more than four digits.
        y = 0

        for x in problem: # Resets on white spaces

            if '9' >= x >= '0':
                y += 1
            else:
                y = 0
          
            if y > 4:
                return True
        
        return False

    
    if too_many_problems(problems):
        return "Error: Too many problems."
    
    if fails_individual_test(problems, inappropriate_operator):
        return "Error: Operator must be '+' or '-'."

    if fails_individual_test(problems, above_operand_length):
        return "Error: Numbers cannot be more than four digits."

    if fails_individual_test(problems, not_only_digits):
        return "Error: Numbers must only contain digits."
        
    return 0
          
# Gives the output if the input is right
def answer(problems, logic):
    # Firstly, getting the numbers
    def list_numbers(problems):
    
        numbers = list()
        j = ""

        for x in problems:
            for i in x:
                if i == " ":
                    if j != "":
                        numbers.append(int(j)) # first number
                        j = ""
                        continue

                elif i == "+" or i == "-":
                    numbers.append(i)
                    continue
                
                else:
                    j = j + i
            
            numbers.append(int(j)) # second number
            j = ""


        return numbers
      

    def widest_numbers(numbers):
      
        biggest = list()
        y = 0

        for x in numbers:
            if x == '+' or x == "-":
                number1 = numbers[y - 1]
                number2 = numbers[y + 1]

                if number1 > number2:
                    biggest.append(len(str(number1)))
                else:
                    biggest.append(len(str(number2)))
                
            y = y + 1
        
        return biggest
        
      
    def visual(numbers, widest, logic=False):

        output = ""
        result = 0 # operation result
        y = 0 # numbers
        z = 0 # spaces
        w = 1 # iterations

        # First line
        for x in widest:
            spaces = x - len(str(numbers[y])) + 2 # Operand + operator spaces
            
            while z < spaces:
                output = output + " "
                z = z + 1
            
            z = 0
            
            output = output + str(numbers[y]) # First line number

            y = y + 3

            if w != len(widest): # Last number
                output = output + "    " # 4 required spaces

            w = w + 1

        output = output + "\n"

        # Second line
        y = 1
        z = 0
        w = 1

        for x in widest:

            output = output + str(numbers[y]) # Operator

            spaces = x - len(str(numbers[y + 1])) + 1 # Operand + operator spaces
            
            while z < spaces:
                output = output + " "
                z = z + 1

            z = 0

            output = output + str(numbers[y + 1]) # Second line number

            y = y + 3

            if w != len(widest): # Last number
                output = output + "    " # 4 required spaces

            w = w + 1

        output = output + "\n"

        # Third line
        z = 0
        w = 1

        for x in widest:
            
            spaces = x + 2 # length of ---

            while z < spaces:
                output = output + "-"
                z = z + 1
            
            z = 0
            
            if w != len(widest):
                output = output + "    "
            
            w = w + 1

        if logic == True:
            y = 1
            z = 0
            w = 1

            output = output + "\n"

            for x in widest:
                
                if numbers[y] == "+":
                    result = numbers[y - 1] + numbers[y + 1]
                elif numbers[y] == "-":
                    result = numbers[y - 1] - numbers[y + 1]

                y = y + 3
                
                spaces = x - len(str(result)) + 2

                while z < spaces:
                    output = output + " "
                    z = z + 1
            
                z = 0

                output = output + str(result)

                if w != len(widest): # Last number
                    output = output + "    "

                w = w + 1

        return output


    numbers = list_numbers(problems)
    widest = widest_numbers(numbers)
    return visual(numbers, widest, logic)


def arithmetic_arranger(problems, logic=False):
    
    error = error_finder(problems)

    if error:
        return error
    else:
        arranged_problems = answer(problems, logic)
        return arranged_problems