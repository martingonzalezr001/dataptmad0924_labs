"""
This is a dumb calculator that can add and subtract whole numbers from zero to five.
When you run the code, you are prompted to enter two numbers (in the form of English
word instead of number) and the operator sign (also in the form of English word).
The code will perform the calculation and give the result if your input is what it
expects.

The code is very long and messy. Refactor it according to what you have learned about
code simplicity and efficiency.



"""


# Arithmetic operations
def add(n1,n2):
    sum = n1 + n2
    return sum
def subtract(n1,n2):
    minus = n1 - n2
    return minus

def parserLetter(n1_str, n2_str ,dict, op):
    

    '''Set the strings operators into ints to calculate the result and transform it into a string'''
    n1 = 0
    n2 = 0
    
    for key, value in dict.items():
        if key == n1_str:
            n1 = value
        if key == n2_str:
            n2 = value
    print(" N1: " + str(n1))
    print(" N2: " + str(n2))
    
    
    result_str = ''

    
    print(type(op))
    print("Op: ")
    print(op)
    if op == 'add' or op == '+' or op == 'sumar' or op == 'suma' or op == 1 or  op == "1" or op == "+" or op == "plus" :
        result = n1 + n2
        print(result)

    if op == 'subtract' or op == 'restar' or op == 'resta' or op == '-' or op == 'minus':
        result = n1 - n2
        

    else:
        print("....")
        return "I cannot make that operation, goodbye :)"

    for key, value in dict.items():
        print("check check")
        if value == result:
            result_str = key
            print(result_str)

    # Choose arithmetic operation 
    if op == 'add' or op == '+' or op == 'sumar' or op == 'suma' or op == '1' or op == '+' or op == "plus":
        print(n1_str + " + " + n2_str  + " = " + result_str)

        return f"{n1_str} + {n2_str} = {result_str}"
    
    elif op == 'subtract' or op == 'restar' or op == 'resta' or op == '-' or op == 'minus':
        print(n1_str + " - " + n2_str  + " = " + result_str)
        return f"{n1_str} + {n2_str} = {result_str}"
    else:
        return "I cannot make that operation, goodbye :)"


def select_menu():
    '''
    Main menu to select the format operation and if its about numbers calculate them
    '''
    n_format = input("What type of format do would you rather:\n 1. Numbers. \n 2. Letters\n")
    print(n_format)
    n_format = n_format.lower()
    
    if n_format == '1' or n_format == 'numbers'  or n_format == 'nums' or n_format == 'num' or n_format == '':
        num1 = int(input("Introduce the first number from 1 to 5:\n" ))
        num2 = int(input("Introduce the second number from 1 to 5:\n" ))
        type_op = input("What operation would you like to do?\n 1. Add(+)\n 2. Substract(-)\n")
        
        if type_op == 'add' or type_op == '+' or type_op == 'sumar' or type_op == 'suma' or type_op == '1' or type_op == '+' or type_op == "plus" :
            print("The answer is: " + str(num1) + " + " + str(num2) + " = " + str(add(num1,num2)))
        elif type_op == 'subtract' or type_op == 'restar' or type_op == 'resta' or type_op == '-' or type_op == 'minus':
            print("The answer is: " + str(num1) + " - " + str(num2) + " = " + str(subtract(num1,num2)))


    elif n_format == '2' or n_format == 'leters' or n_format == 'letters':
        letter_num ={ 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9, 'ten':10} 
        letter_num1 = (input("Introduce the first number from one to five(with letters):\n"))
        letter_num2 = (input("Introduce the first number from one to five(with letters):\n"))
        type_op = input("What operation would you like to do?\n 1. Add(+)\n 2. Substract(-)\n")
        parserLetter(letter_num1,letter_num2,letter_num,type_op)

    else:
        print("I am not able to answer this question. Check your input.")
       
select_menu()


        







    
    


    
