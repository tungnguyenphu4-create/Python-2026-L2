#Exercise 1:
import math

def calculate_area(radius):
    return math.pi * radius ** 2
try:
    radius_input = float(input("Enter the radius of the circle in units: "))
    if radius_input < 0:
        print("Radius cannot be negative. Please enter a positive number.")
    else:
        area = calculate_area(radius_input)
        print(f"the area of the circle is: {area: .2f} square units")
except ValueError:
    print("Invalid input. Please enter a numeric value for the radius.")

#Exercise 2:
def celsius_to_fahrenheit(celsius): 
    fahrenheit = (celsius * 9/5) + 32 
    return fahrenheit 
# Example usage 
celsius = float(input("Enter temperature in Celsius: ")) 
fahrenheit = celsius_to_fahrenheit(celsius) 
print(f"{celsius} degrees Celsius is equal to {fahrenheit:.2f} degrees Fahrenheit.")
#Exercise 3:
import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
#Exercise 4:
def is_prime(num): 
    if num <= 1: 

        return False 
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0: 
            return False
    return True

number = 0 
if is_prime(number): 
    print(f"{number} is a prime number.") 
else: 
    print(f"{number} is not a prime number.")
#Exercise 5:
colors = ['red', 'yellow', 'green', 'blue', 'black']
i = input('what is your favorite color:')
if i in colors[0:5]:
    print(colors.index(i))
else:
    print('false')

#Exercise 6:
range1 = list(range(0, 7))          # 0, 1, 2, 3, 4, 5, 6
range2 = list(range(1, 11, 3))      # 1, 4, 7, 10
range3 = list(range(5, 0, -1))      # 5, 4, 3, 2, 1
range4 = list(range(6, -4, -2))     # 6, 4, 2, 0, -2
 
if __name__ == "__main__":
    print("range1:", range1)
    print("range2:", range2)
    print("range3:", range3)
    print("range4:", range4)
#Exercise 7:
def remove_dollar_sign(s):
    return s.replace("$", "")
 
 
if __name__ == "__main__":
    text = input("Enter a string? ")
    print(remove_dollar_sign(text))
#Exercise 8:
def extract_even(l):
    return [x for x in l if x % 2 == 0]
 
 
if __name__ == "__main__":
    sample = [1, 4, 5, -1, 10]
    print("Original list:", sample)
    print("Even numbers: ", extract_even(sample))
#Exercise 9:
def factorial(n):
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
 
 
if __name__ == "__main__":
    num = int(input("Enter a non-negative integer? "))
    print(f"{num}! = {factorial(num)}")
#Exercise 10:
def get_divisors(n):
    return [i for i in range(1, n + 1) if n % i == 0]
 
 
if __name__ == "__main__":
    num = int(input("Enter a number? "))
    print(f"Divisors of {num}: {get_divisors(num)}")
#Exercise 11:
import math
 
 
def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
 
 
if __name__ == "__main__":
    x1 = float(input("Enter x1? "))
    y1 = float(input("Enter y1? "))
    x2 = float(input("Enter x2? "))
    y2 = float(input("Enter y2? "))
    print(f"Distance = {distance(x1, y1, x2, y2)}")
#Exercise 12:
def print_pattern(m, n):
    for i in range(m):
        row = ""
        for j in range(n):
            if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                row += "* "
            else:
                row += "  "
        print(row.rstrip())
 
 
if __name__ == "__main__":
    rows = int(input("Enter number of rows (m)? "))
    cols = int(input("Enter number of columns (n)? "))
    print_pattern(rows, cols)