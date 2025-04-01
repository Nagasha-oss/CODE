
'''
String1="Geeks"
print("first character of the string is:",String1[0] )
## creating a list with many 
List=['Geeks','Nagasha','tina']
print(List[0])

## if statement and nesting
num=int(input("Enter a number:"))
if num==80:   
    print(num," Yes it is.") 
    if num<=80:
     print("its less than 80")
    else:
     print("its not the one")
elif num==30:  
     print("You have passed")
else:
 print( "its negative")
 
 ##loops
 ##for loop summing up numbers
sum=0
List =[1,2,3,4,5,6,7,8,9,10]
for i in List:
    sum +=i##same as sum+1
    print("the sum of the numbers in the list is:",sum)##outputting the sum
    
    ##range
    ##range starts counting from zero and increases by one
    ## range doesnt store values
print(range(10))
lista=list(range(10))
print(lista)

##range with 2 parameters
print(range(2,8))
listb=list(range(2,8))
print(listb)

##sets
set1=set("GeeksforGeeks")
print("\nSet with the use of String: ",set1)
print(set1)
set2=set(["geeks","For","Geeks"])
print("\n set eith the use of List: ")
print(set2)
print("geeks" in set2)

##a simple python program to demonstrate iteration through a list using an index
music=["rock","nagasha","tom"]
for i in music:
    if i==music[1]:
        continue
    print(music)
    

     ## while loop adding natural numbers
n = int(input("Enter how many natural numbers you want to add: "))
sum=0 #initialize the sum
i=1 #initialize i as index to one
while(i<= n):
     sum +=i #sum=sum +i
     print("the sum of the",i,"natural numbers is: ",sum)
     i +=1 #i= i+1
     
     ##break  and continue statements
for val in "string":
     print('in for loop',val)
     if val=="i":
            break# you can replace this with break if you want to stop so it will stop at"i"in the word string
     print('out of loop')   

##pass statement 
sequence =[1,2,3,4,5,6,7,8,9,10]
for val in sequence:
     pass
print('The end')

## greeting function
def greet (name):
     print("Hello",name,"!How are you")
greet("Paula")
greet("Nagasha")

## adding functions
def add(a,b):
     return(a+b)
sum=add(2,3)
print(sum)   
## equality operator
var = 0  # Assigning 0 to var
print(var == 0)

var = 1  # Assigning 1 to var
print(var == 0)

## not equal operator
var = 0  # Assigning 0 to var
print(var != 0)
 
var = 1  # Assigning 1 to var
print(var != 0)

n=int(input("Enter the number:"))
print(n>100)

# Read three numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

# We temporarily assume that the first number
# is the largest one.
# We will verify this soon.
largest_number = number1

# We check if the second number is larger than the current largest_number
# and update the largest_number if needed.
if number2 > largest_number:
    largest_number = number2

# We check if the third number is larger than the current largest_number
# and update the largest_number if needed.
if number3 > largest_number:
    largest_number = number3

# Print the result
print("The largest number is:", largest_number)

largest_number = -999999999
number = int(input())
if number == -1:
    print(largest_number)
    exit()
if number > largest_number:
    largest_number = number
# Go to line 02

name = input("Enter flower name: ")

if name == "Spathiphyllum":
    print("Yes - Spathiphyllum is the best plant ever!")
elif name == "spathiphyllum":
    print("No, I want a big Spathiphyllum!")
else:
    print("Spathiphyllum! Not", name + "!")

number=int(input("Enter year number: "))
if number < 1582:
    print(" not within  the Greg calender")
else:
 if number%4 != 0:
    print("Common yaer")
 elif number%100 != 0:
    print("Leap year") 
 elif number%400 !=0:
    print("Common year")    
 else :
    print("Leap year")
    
while True:
    print("I'm stuck inside a loop.")

# A program that reads a sequence of numbers
# and counts how many numbers are even and how many are odd.
# The program terminates when zero is entered.

odd_numbers = 0
even_numbers = 0

# Read the first number.
number = int(input("Enter a number or type 0 to stop: "))

# 0 terminates execution.
while number != 0:
    # Check if the number is odd.
    if number % 2 == 1:
        # Increase the odd_numbers counter.
        odd_numbers += 1
    else:
        # Increase the even_numbers counter.
        even_numbers += 1
    # Read the next number.
    number = int(input("Enter a number or type 0 to stop: "))

# Print results.
print("Odd numbers count:", odd_numbers)
print("Even numbers count:", even_numbers)

## counter variable 
counter = 6 # the number of times 
while counter != 0: #as long as counter is not 0
    print("Inside the loop.", counter)# print 
    counter -= 1# and it will be subtracting by one 
print("Outside the loop.", counter)#and when it reaches Zero it prints that

secret_number=34
while True:
    n=int(input("Enter the number: "))
    if n==secret_number:
       print("well donne girl......")
       break
    else: 
       print ("haaaa bitch")

import time
for i in range(1,6):
    print(f" {i} Misisipi",)
    time.sleep(1)
print ("ready or no, here i come")

word = input("Enter a word (or 'chupacabra' to exit): ")
while True:
    if word == "chupacabra":
        print("You've successfully left the loop.")
        break
    
        
# Ask the user to enter a word
user_word = input("Enter a word: ")

# Convert the word to upper case
user_word = user_word.upper()

# Iterate through each letter in the word
for letter in user_word:
    # If the letter is a vowel, continue to the next iteration
    if letter in 'AEIOU':
        continue
    # Print the letter if it is not a vowel
    print(letter)

word = "Python"
for letter in word:
    print(letter, end="*")

text = "OpenEDG Python Institute"
for letter in text:
    if letter == "P":
        break
    print(letter, end="")

text = "pyxpyxpyx"
for letter in text:
    if letter == "x":
        continue
    print(letter,end="")

for i in range(0, 3):
    print(i)
else:
    print(i, "else")
    '''
 ### logical operators not
var=1
print(var > 0)
print(not (var <= 0))
'''
var=1
print(var != 0)
print(not (var == 0))
 
 ### replaces what is in that postion
list_1 = [1,2,3,4,5,6]
list_2 = list_1
list_1[1] = 8
print(list_2)
this will output will be[1,8,3,4,5,6]by replacing 2 in the place of 2 in its position

##brings all its contents along when we use [:]
list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)
  this will output 1 because list 2 took all the contents of list 1

##replacing elements of lists
numbers = [10, 5, 7, 2, 1]
print("Original list contents:", numbers)  # Printing original list contents.
 
numbers[0] = 111
print("New list contents: ", numbers)  # Current list contents.

##still on replacement
numbers = [10, 5, 7, 2, 1]
print("Original list contents:", numbers)  # Printing original list contents.

numbers[0] = 111
print("\nPrevious list contents:", numbers)  # Printing previous list contents.

numbers[1] = numbers[4]  # Copying value of the fifth element to the second.
print("New list contents:", numbers)  # Printing current list contents.
print(numbers[0]) # Accessing the list's first element.
print("\nList length:", len(numbers))  # Printing the list's length.
print(numbers)  # Printing the whole list.

## deleting a number in a list
numbers = [10, 5, 7, 2, 1]
del numbers[1]# Removing the second element from the list.
print(len(numbers))
print(numbers)

## negative indices
numbers = [111, 7, 2, 1]
print(numbers[-1])#it print 1

###small assignment
hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.
number =int(input("enter a number: "))# Step 1: write a line of code that prompts the user
hat_list[2]=number# to replace the middle number with an integer number entered by the user.
print(hat_list)
del hat_list[4]# Step 2: write a line of code that removes the last element from the list.
print(hat_list)
print("length of the list: ",len(hat_list))# Step 3: write a line of code that prints the length of the existing list.
print(hat_list)

### adding elements to lists using append[value] and insert[location,value]
numbers = [111, 7, 2, 1]
print(len(numbers))
print(numbers)

###

numbers.append(4)## adds 4 in the list but at the end

print(len(numbers))## print 4
print(numbers)##[111,7,2,1]

###

numbers.insert(0, 222)## adds 222 in the first position
print(len(numbers))##prints 6
print(numbers)##[222,111,7,2,1,4]

## adding things to an empty list
##using append
my_list = []  # Creating an empty list.

for i in range(5):
    my_list.append(i + 1)

print(my_list)

##using insert
my_list = []  # Creating an empty list.

for i in range(5):
    my_list.insert(0, i + 1)

print(my_list)##it will be reverse this time[5,4,3,2,1]

##adding elements in a list
my_list = [10, 1, 8, 3, 5]
total = 0

for i in range(len(my_list)):## the length of the list is 5 so its the same asa range 5
    total += my_list[i]

print(total)
## this will do the same as above
my_list = [10, 1, 8, 3, 5]
total = 0
 
for i in my_list:
    total += i
 
print(total)
 ### exchanging of positions between elements
my_list = [10, 1, 8, 3, 5]

my_list[0], my_list[4] = my_list[4], my_list[0]
my_list[1], my_list[3] = my_list[3], my_list[1]

print(my_list)
##exchanging of positions between elements using for loop
for i in range(length // 2):
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]## length of the list is the one we are reffering to as length

print(my_list)

## assignment
# Step 1: Create an empty list named beatles
beatles = []

# Step 2: Use the append() method to add the following members of the band to the list: John Lennon, Paul McCartney, and George Harrison
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

# Display the list after step 2
print("After step 2:", beatles)

# Step 3: Use the for loop and the append() method to prompt the user to add the following members of the band to the list: Stu Sutcliffe, and Pete Best
new_members = ["Stu Sutcliffe", "Pete Best"]
for member in new_members:
    beatles.append(member)

# Display the list after step 3
print("After step 3:", beatles)

# Step 4: Use the del instruction to remove Stu Sutcliffe and Pete Best from the list
del beatles[-2]  # Remove Stu Sutcliffe
del beatles[-1]  # Remove Pete Best

# Display the list after step 4
print("After step 4:", beatles)

# Step 5: Use the insert() method to add Ringo Starr to the beginning of the list
beatles.insert(0, "Ringo Starr")

# Display the final list
print("After step 5:", beatles)
del my_list  # deletes the whole list
 
 ## more on lists[:]
 # Copying the entire list.
list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)

# Copying some part of the list.
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list)
##negative indices
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:-1]
print(new_list)## output will be[8,6,4]

If the start specifies an element lying further than the one described by the end (from the list's beginning), the slice will be empty:
my_list = [10, 8, 6, 4, 2]
new_list = my_list[-1:1]
print(new_list)

 If you omit the start in your slice, it is assumed that you want to get a slice beginning at the element with index 0.
In other words, the slice of this form:
my_list[:end]
my_list[0:end]
my_list = [10, 8, 6, 4, 2]
new_list = my_list[:3]
print(new_list)

Similarly, if you omit the end in your slice, it is assumed that you want the slice to end at the element with the index len(my_list).

In other words, the slice of this form:

my_list[start:]
my_list[start:len(my_list)]
 
my_list = [10, 8, 6, 4, 2]
new_list = my_list[3:]
print(new_list)

  and if you omit both start and end you print the whole list 
  
## more about the del instruction
my_list = [10, 8, 6, 4, 2]
del my_list[1:3]
print(my_list)## it will output [10,4,2]
 ## deleting all elements
my_list = [10, 8, 6, 4, 2]
del my_list[:]
print(my_list)## and the output will be []
## removing the slice
my_list = [10, 8, 6, 4, 2]
del my_list## the del instruction will delete itself
print(my_list) ## will output an error
'''










