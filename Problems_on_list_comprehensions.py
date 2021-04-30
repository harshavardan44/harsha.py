""""
1. Program that computes the value of a+ba+bba with given digits as the value of a and b.
Hint: Suppose the following input is supplied to the program:
9 and 3
Then, the output should be:
9+39+339=387

2. Program to use a list comprehension to square each even number in a list. The list is input by a sequence of comma-separated numbers.
Hint:
Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9
Then, the output should be:
4,16,36,64

3. Program which accepts a string as input and print the characters that have even indexes.
Hint:
If the following string is given as input to the program:
S1a2i3R4a5m6I7B8B9A
Then, the output of the program should be:
SaiRamIBBA

4. Program to make a list whose elements are intersection of the above given lists.
Hint:
With two given lists [204501,204503,204506,204528,204534,204535] and [204512,204524,204535,204503,204528].
Intersection is 204503, 204528, 204535

5. Program to print this list after removing all duplicate values with original order reserved.
Hint: With a given list [204501,204503,204506,204528,204534,204535,204512,204524,204535,204503,204528]
The output should be: [204501,204503,204506,204512,204524,204528,204534,204535]
"""

#Problem 1
a = input("enter the number")
b = input("enter the number")
n1 = int("%s" % a)
print(n1)
n2 = int("%s%s" % (b,a))
print(n2)
n3 = int("%s%s%s" % (b,b,a))
print(n3)
print(n1+n2+n3)

#Problem 2
a = []
c = int(input("Enter the number of elements in the list: "))
print("Enter the entries of the list:")
for j in range(c):  
     a.append(int(input()))

odd_list = [i**2 for i in a if (i % 2 == 0)]
print(odd_list)

#Problem 3
print("Please enter text to print::")
inputchars = input()

if inputchars:
	string = ""
	for i in inputchars:
		if inputchars.index(i)%2 == 0:
			string += str(i)

print('-------------------')
print("You Entered:", inputchars)
print("Result:")
print(string)


#Problem 4
def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3
  
lst1 = [204501,204503,204506,204528,204534,204535]
lst2 = [204512,204524,204535,204503,204528]
print(intersection(lst1, lst2))

#Problem 5
def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list

duplicate = [204501,204503,204506,204528,204534,204535,204512,204524,204535,204503,204528]
print(Remove(duplicate))
