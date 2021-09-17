#Salaries

l = []
num = int(input("Enter the number of coworkers: "))
for i in range(1, num + 1):
    el = int(input("Enter the salaries: "))
    l.append(el)
    l.sort()
print("The difference is = ", l[-1] - l[0])
				
# Boring numbers
number = input("Please input the number: ")
first_digit = number[0]
print(number)
if number != number[0] * len(number):
    print("The number is interesting")
else:
    print("The number is boring")

#line segment intersection problem
a_1 = int(input("Please input a1", ))
b_1 = int(input("Please input b1", ))
a_2 = int(input("Please input a2", ))
b_2 = int(input("Please input b2", ))

l_a = [elem for elem in range(a_1, a_2+1)]
l_b = [el for el in range(b_1, b_2+1)]
lst_intersection = [elements for elements in l_a if elements in l_b]
print("the intersection gives ", lst_intersection)


# Largest number
number = int(input("Please input the number "))
lst_number = list(map(int, str(number)))
new_list = lst_number.copy()
lst_number.sort(reverse=True)
print(new_list)
print(lst_number)
test_list = list(map(int, lst_number))
number_new = int(''.join(map(str, test_list)))
if number_new > number:
    print("Yes, it is possible")
else:
    print("No, it is not possible")
print(number_new)


# Number of divisors

number = int(input(("Please input the number" )))

number_of_div = 0

for i in range(1, number+1):
    if number % i == 0:
        number_of_div +=1
print("The number has", number_of_div, "divisors")

# Quadratic Equation

a = float(input("Please input a"))
b = float(input("Please input b"))
c = float(input("Please input c"))

D = b**2 - 4 * a * c

if a == 0:
    print("Non-quadratic equation")
    if b == 0 and c == 0:
        print("Infinite solutions")
    if b == 0 and c != 0:
        print("No solution")
    if b != 0:
        x = c/b
        print("Only one solution to your linear equation:", x)
else:
    print("Quadratic equation")
    if D < 0:
        print(" Discriminant: ", D, "D<0. The equation has no solutions")
    if D == 0:
        x_0 = (-b) / (2 * a)
        print(" Discriminant: ", D, "There is one solution:", x_0)
    elif D > 0:
        x_1 = (-b + D**(-1/2)) / (2 * a)
        x_2 = (-b - D**(-1/2)) / (2 * a)
        print("The solutions are", x_1, "and", x_2)


#list 1 // convert a list of characters into a string.
lst = ['a', 'b', 'c', 'd']
str_1 = ''.join(lst)
print(str_1)

#list 2// Second largest number

l_7 = [1, 2, -8, -2, 0, -2]
l_7.sort()
print(l_7[-2])





