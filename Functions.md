# Function calling

## def keyword

def greet(name):
  print(name)

### Use: greet("Alice")

## Positional arguments

def add(a,b):
  return a+b

### Use: result = add(2,3) #5

## Keyword arguments

def greet(name, age):
  print(f"Hello, {name}! You are {age} years old.")

greet(age=25, name="Bob") #Arguments are passed by name, order does not matter

## Default arguments

def greet(name, age=30):
  print(f"Hello, {name}!You are {age} years old")

greet("Charlie") #uses default value
greet("Alice", 25) #Overwrrites default age value

# Function types
> No parameters
> No return values
> Multiple return values
  def min_max(numbers):
     return min(numbers), max(numbers)

  low, high = min_max([1,2,3,4,5])

> Lambda functions - small, anonymous function defined with lambda keyword

# Function recursion

higher order functions - takes other functions as arguments, returns a function, or both
functions as arguments leads to more abstract and reusable code

e.g., 

def apply_function(func, value):
  return func(value)

result = apply_function(lambda x:x**2,5)

# Function Annotations

Attach metadata to function arguments and return values
Python doesn't enforce annotations, used for documentation

def greet(name:str, age:int) -> str:
  return f"Hello, {name}. You are {age} years old."


