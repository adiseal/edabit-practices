def fizz_buzz(num):
    # Nested ternary operator
	return "FizzBuzz" if num % 3 == 0 and num % 5 == 0 else "Fizz" if num % 3 == 0 else "Buzz" if num % 5 == 0 else str(num) 
