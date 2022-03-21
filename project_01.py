import random
random.seed(1234)
name = input('What is your name? ')
print(f'Hello {name}, welcome to the multiplication practice!')
correct = wrong = 0

number_of_questions = int(input('How many questions do you want? '))
upper_range = number_of_questions + 1

for number in range(1, upper_range):
    rand_a = random.randint(1,10)
    rand_b = random.randint(1,10)
    correct_answer = rand_a * rand_b
    answer = int(input(f'Q{number}: {rand_a} x {rand_b} = '))

    if answer == correct_answer:
        print('Correct!')
        correct += 1
    else:
        print(f'Sorry, {rand_a} x {rand_b} = {correct_answer}')
        wrong += 1

print(f'Thanks for the session {name}')

grade = (correct/number_of_questions)*100
score = round(grade)

print(f'Correct answers = {correct}, wrong answers = {wrong}')
print(f'Score = {score}')

if grade == 100:
    print('Perfect!')
elif grade >= 85:
    print('Excellent work!')
elif 85 > grade >= 70:
    print('Not too bad')
elif 70 > grade >= 50:
    print('Passing grade')
else:
    print('You need to practice more!')
