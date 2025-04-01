
'''
ret_number=34
while True:
    n=int(input("Enter the number: "))
    if n==secret_number:
     print("well donne girl......")
    break
else: 
    print ("haaaa bitch")

##The in and not in operators
my_list = [0, 3, 12, 8, 2]

print(5 in my_list)
print(5 not in my_list)
print(12 in my_list)

## checking for the largest number
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in range(1, len(my_list)):
    if my_list[i] > largest:
        largest = my_list[i]

print(largest)

## alternatively
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in my_list:
    if i > largest:
        largest = i

print(largest)

## alternatively
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in my_list[1:]:
    if i > largest:
        largest = i

print(largest)

# Program to iterate through a list using indexing
genre = ['pop', 'rock', 'jazz']
 # iterate over the list using index
for i in range(len(genre)):
 print("I like", genre[i])

##loop with else
digits = [0, 1, 5]
for i in digits:
 print(i)
else:
 print("No items left.")
 '''
 # program to display student's marks from record
student_name = 'Soyuj'
marks = {'James': 90, 'Jules': 55, 'Arthur': 77}
for student in marks:
 if student == student_name:
  print(marks[student])
 break
else:
 print('No entry with that name found.')
 
