#project1 - string concation
adj=input("adjective:")
verb1=input("verb:")
verb2=input("verb:")
famous_person=input("famous person")
madlib=f"Computer scince {adj}\
this is verb {verb1} and this is second {verb2} this is famous person {famous_person}"
print(madlib)

#project2  -  guess the number
import random

def guess(x):
    random_number=random.randint(1,x)
    guess=0
    while guess !=random_number:
        guess=int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print('Sorry, guess agin. too low.')
        elif guess > random_number:
            print('Sorry, guess agin. too high.')
        
    print(f"guess is correct{random_number}")
    
guess(10)       
