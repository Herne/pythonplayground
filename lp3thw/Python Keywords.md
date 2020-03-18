# with ... as ...
| Keyword | Description                    | Example           |
| ------- | ------------------------------ | ----------------- |
| as      | Part of the with-as statement. | with X as Y: pass |
```python
with open("x.txt") as f:
    data = f.read()
```
# assert
| Keyword | Description                             | Example               |
| ------- | --------------------------------------- | --------------------- |
| assert  | Assert (ensure) that something is true. | asset False, "Error!" |
```python
# initializing list of foods temperatures 
batch = [ 40, 26, 39, 30, 25, 21] 

# initializing cut temperature 
cut = 26

# using assert to check for temperature greater than cut 
for i in batch: 
	assert i >= 26, "Batch is Rejected"
	print (str(i) + " is OK")
```
```
40 is OK
26 is OK
39 is OK
30 is OK
```
```
Traceback (most recent call last):
  File "/home/bd45fb65343814a85b6c19bbe366b419.py", line 13, in 
    assert i >= 26, "Batch is Rejected"
AssertionError: Batch is Rejected
```
# class
| Keyword | Description               | Example           |
| ------- | ------------------------- | ----------------- |
| class   | Define a class. | class Person(object) |

```python
class Dog: 
	
	# A simple class 
	# attribute 
	attr1 = "mammal"
	attr2 = "dog"

	# A sample method 
	def fun(self): 
		print("I'm a", self.attr1) 
		print("I'm a", self.attr2) 

# Driver code 
# Object instantiation 
Rodger = Dog() 

# Accessing class attributes 
# and method through objects 
print(Rodger.attr1) 
Rodger.fun() 
```

# break
| Keyword | Description                    | Example           |
| ------- | ------------------------------ | ----------------- |
| break      | Stop this loop right now. | while True: break |
```python
# Python program to 
# demonstrate break statement 

s = 'geeksforgeeks'
# Using for loop 
for letter in s: 

	print(letter) 
	# break the loop as soon it sees 'e' 
	# or 's' 
	if letter == 'e' or letter == 's': 
		break

print("Out of for loop") 
print() 

i = 0

# Using while loop 
while True: 
	print(s[i]) 

	# break the loop as soon it sees 'e' 
	# or 's' 
	if s[i] == 'e' or s[i] == 's': 
		break
	i += 1

print("Out of while loop") 

```
```
g
e
Out of for loop

g
e
Out of while loop
```


# continue

| Keyword  | Description                                  | Example              |
| -------- | -------------------------------------------- | -------------------- |
| continue | Don't process more of the loop, do it again. | while True: continue |

```python
# loop from 1 to 10  
for i in range(1, 11):

    # If i is equals to 6,    
    # continue to next iteration    
    # without printing   
    if i == 6:
        continue
    else:
        # otherwise print the value  
        # of i  
        print(i, end=" ")

```

# pass

| Keyword | Description          | Example           |
| ------- | -------------------- | ----------------- |
| pass    | This block is empty. | def empty(): pass |

```python
# Python program to demonstrate 
# pass statement 


s = "geeks"

# Empty loop 
for i in s: 
	# No error will be raised 
	pass

# Empty function 
def fun(): 
	pass

# No error will be raised 
fun() 

# Pass statement 
for i in s: 
	if i == 'k': 
		print('Pass executed') 
		pass
	print(i) 
```

```
g
e
e
Pass executed
k
s
```

# try ... except ... finally ...

| Keyword | Description                                        | Example                          |
| ------- | -------------------------------------------------- | -------------------------------- |
| try     | Try this block, and if exception, go to except.    | try: pass                        |
| except  | If an exception happens, do this.                  | except ValueError as e: print(e) |
| finally | Exceptions or not, finally do this no matter what. | finally: pass                    |

```python
def divide(x, y): 
    try: 
        # Floor Division : Gives only Fractional Part as Answer 
        result = x // y 
        print("Yeah! Your answer is :", result) 
    except ZeroDivisionError: 
        print("Sorry! You are dividing by zero.")
    finally:
        print("This is always executed.")

# Look at parameters and note the working of Program 
divide(3, 0) 
```

```
Sorry! You are dividing by zero.
This is always executed.
```

# exec

| Keyword | Description             | Example               |
| ------- | ----------------------- | --------------------- |
| exec    | Run a string as Python. | exec 'print("hello")' |

```python
# Python program to illustrate use of exec to 
# execute a given code as string. 

# function illustrating how exec() functions. 
def exec_code(): 
	LOC = """ 
def factorial(num): 
	fact=1 
	for i in range(1,num+1): 
		fact = fact*i 
	return fact 
print(factorial(5)) 
"""
	exec(LOC) 
	
# Driver Code 
exec_code() 
```

```
120
```

# lambda

| Keyword | Description                        | Example                    |
| ------- | ---------------------------------- | -------------------------- |
| lambda  | Create a short anonymous function. | s = lambda y: y ** y; s(3) |

```python
# Python program to demonstrate 
# lmabda functions 


def power(n): 
	return lambda a : a ** n 

# base = lambda a : a**2 get 
# returned to base 
base = power(2) 

print("Now power is set to 2") 

# when calling base it gets 
# executed with already set with 2 
print("8 powerof 2 = ", base(8)) 

# base = lambda a : a**5 get 
# returned to base 
base = power(5) 
print("Now power is set to 5") 

# when calling base it gets executed 
# with already set with newly 2 
print("8 powerof 5 = ", base(8)) 
```

```
Now power is set to 2
8 powerof 2 = 64
Now power is set to 5
8 powerof 5 = 32768
```

```python
# Python program to demonstrate 
# lambda functions inside map() 
# and filter() 


a = [100, 2, 8, 60, 5, 4, 3, 31, 10, 11] 

# in filter either we use assignment or 
# conditional operator, the pass actual 
# parameter will get return 
filtered = filter (lambda x: x % 2 == 0, a) 
print(list(filtered)) 

# in map either we use assignment or 
# conditional operator, the result of 
# the value will get returned 
mapped = map(lambda x: x % 2 == 0, a) 
print(list(mapped))

```

```
[100, 2, 8, 60, 4, 10]
[True, True, True, True, False, True, False, False, True, False]
```

# raise
| Keyword | Description                              | Example                |
| ------- | ---------------------------------------- | ---------------------- |
| raise   | Raise an exception when things go wrong. | raise ValueError("No") |

```python
def example(): 
	try: 
		int('N/A') 
	except ValueError as e: 
		raise RuntimeError('A parsing error occurred') from e

example() 
```

```bash
Traceback (most recent call last):
  File "testraise.py", line 3, in example
    int('N/A') 
ValueError: invalid literal for int() with base 10: 'N/A'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "testraise.py", line 7, in <module>
    example() 
  File "testraise.py", line 5, in example
    raise RuntimeError('A parsing error occurred') from e
RuntimeError: A parsing error occurred
```

# yield

| Keyword | Description                     | Example                      |
| ------- | ------------------------------- | ---------------------------- |
| yield   | Pause here and return to caller | def X(): yield Y; X().next() |

```python
# Python3 code to demonstrate 
# yield keyword 

# generator to print even numbers 
def print_even(test_list) : 
	for i in test_list: 
		if i % 2 == 0: 
			yield i 

# initializing list 
test_list = [1, 4, 5, 6, 7] 

# printing initial list 
print ("The original list is : " + str(test_list)) 

# printing even numbers 
print ("The even numbers in list are : ", end = " ") 
for j in print_even(test_list): 
	print (j, end = " ") 
```

```
The original list is : [1, 4, 5, 6, 7]
The even numbers in list are :  4 6 
```

