#6) შექმენით პროგრამა სადაც გამოიყენებთ While loop - ს. 
#თქვენი დავალება იქნება ის, რომ მომხამრებელს შემოატანინოთ რიცხვი და თქვენ უნდა გამოიცნოთ ეს რიცხვი, ხოლო ყოველ არ გამოცნობილ რიცხვზე ისევ თავიდან უნდა შეგეკითხოთ და შეიყვანოთ რიცხვი.


num = int(input('Enter a number: '))
guess_num = int(input('Guess the number: '))


while num != guess_num:
    guess_the_number_again = int(input('Guess the number again: '))
    