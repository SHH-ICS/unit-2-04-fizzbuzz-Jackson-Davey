# My Python Program
# Task:  use if statements to output the result of the game fizzbuzz.  
# Start at 1
# For multiples of 3, output   Fizz
# For multiples of 5, output   Buzz
# For multiples of 15, output   FizzBuzz
# End at 32

for index in range(1,33):
  myNumber = index
  if myNumber % 15 == 0:
    myNumber = ("FizzBuzz")
  else:
    if myNumber % 5 == 0:
      myNumber = ("Buzz")
    else:
      if myNumber % 3 == 0:
        myNumber = ("Fizz")
  print(myNumber)
