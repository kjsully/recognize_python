num1 = 42 #variable declaration, number
num2 = 2.3 #variable devlaration, number - float/decimal?
boolean = True #variable declaration, boolean
string = 'Hello World' #variable declaration, initialize string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] ##variable declaration initialize list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} ##variable declaration initialize dictionary
fruit = ('blueberry', 'strawberry', 'banana') ##variable declaration initialize tuple
print(type(fruit)) #log statement
print(pizza_toppings[1]) #log statement - access list value
pizza_toppings.append('Mushrooms') #log statement - add list value
print(person['name']) #log statement - access list value
person['name'] = 'George' #log statement - change value
person['eye_color'] = 'blue' #log statment - change value
print(fruit[2]) #log statement - access value

if num1 > 45: #conditional if
    print("It's greater")#log statement
else: #conditional else
    print("It's lower") #log statement

if len(string) < 5: #length check 
    print("It's a short word!") #log statement 
elif len(string) > 15: #conditional else if, length check
    print("It's a long word!") #log statement
else: # conditional else
    print("Just right!") #log statement

for x in range(5): #for loop - start, parameter
    print(x) #log statement
for x in range(2,5): #for loop - start, paramenters
    print(x)#log statement
for x in range(2,10,3):#for loop - start, paramenters
    print(x)#log statement
x = 0 #variable declaration, number
while(x < 5): #while loop
    print(x) #log statement
    x += 1 #while loop - increment

pizza_toppings.pop() #delete list value
pizza_toppings.pop(1) #delete list value with index of 1

print(person) #log 
person.pop('eye_color') #delete, access value
print(person) #log statement

for topping in pizza_toppings: #access list value.. or dictionary? also for loop
    if topping == 'Pepperoni': #conditional if, string
        continue #continue
    print('After 1st if statement') #log statement 
    if topping == 'Olives': #if statement, string
        break #for loop break

def print_hello_ten_times(): #function declaration
    for num in range(10): #for loop
        print('Hello')#log statement

print_hello_ten_times() #log statement, function called

def print_hello_x_times(x): #log statemement, access value
    for num in range(x): #for loop, parameter
        print('Hello') #log statement, string

print_hello_x_times(4) #log statement, fucntion called, argument

def print_hello_x_or_ten_times(x = 10):#function declaration, parameter
    for num in range(x): #for loop, parameter
        print('Hello')

print_hello_x_or_ten_times()#log statement, function called
print_hello_x_or_ten_times(4)#log statement, function called, argument


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)