import random
import operator
def problem():
    operators = {
        '+':operator.add,
        '-':operator.sub,
        '*':operator.mul,
        '/':operator.truediv
    }

    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operation = random.choice(list(operators.keys()))
    answer = float(round(operators.get(operation)(num1, num2),3))
    print(f'What is {num1}{operation}{num2}')
    return answer

def ask_question():
    answer = problem()
    try:
        guess = float(input('Enter your answer: '))
    except ValueError:
        return ""
    return guess == answer

def game():
    score = 0
    while True:
        if ask_question()==True:
            score+=10
            print('Correct!')
        else:
            print('Incorrect!')
            break
    print(f'======Game Over======\n Your score is {score}\nKeep going!')

if __name__=="__main__":
    game()
