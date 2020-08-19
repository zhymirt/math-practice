import random
def basic_math(x, y, op):
    return op(x, y) if x is not None and y is not None and op else None

def check_answer(x, y, op, answer, error=0.001):
    correct = basic_math(x, y, op)
    # print(answer-correct)
    return correct is not None and abs(answer-correct) < error

def get_op( val):
    if val == "addition":
        return lambda x, y : x + y, '+'
    elif val == "multiplication":
        return lambda x, y : x * y, '*'
    elif val == "subtraction":
        return lambda x, y : x - y, '-'
    elif val == "division":
        return lambda x, y : x / y if y != 0 else 'undefined', '/'
    elif val == "exponent":
        return lambda x, y : x ** y, '^'
    else:
        print("Unknown operation")
        return None, None
def is_num(number):
    if number.isnumeric():
        return True
    elif number[0] == '-':
        return len(number) > 1 and number[1] != '-' and is_num(number[1:])
    elif number.__contains__('.'):
        numbers = list(filter(str, number.split('.')))
        if not numbers or len(numbers) < 1 or len(numbers) > 2:
            return False
        return all(map(is_num, numbers))
    return False
    # return number.isnumeric() or (number[0] == '-' and is_num(number[1:])) or (number)

def begin_training():
    print('Welcome to the math practice program.')
    answer = ''
    operator, op_sign = None, None
    while not operator:
        answer = input('What would you like to work on today?\n')
        operator, op_sign = get_op(answer) if answer and get_op(answer) else None
    print("Let's get started!")
    while answer != 'exit':
        number_1 = random.randint(0, 100)
        number_2 = random.randint(0, 100)
        answer = input(str(number_1)+' '+op_sign+' '+str(number_2) + ' = ? (or "exit" to quit)\n')
        if answer == 'exit':
            exit()
        elif is_num(answer):
            print("Correct" if check_answer(number_1, number_2, operator, float(answer))
                else "The correct answer is "+str(basic_math(number_1, number_2, operator)))
        else:
            print('Unknown command')
# nice_comments = ['Great job!', 'Excellent!', 'Nice!', 'Spectacular!', 'Epic!', 'Amazing', 'Keep it up!']
begin_training()