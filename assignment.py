
string1 = "Hello "


name = input("Enter your Name: ")

result1 = string1 + name
print(result1)


string3 = ", welcome to Python programming"
final_result = result1 + string3
print(final_result)




text = "Hello jishnu , welcome to Python programming"


print("a. First character:", text[0])


print("b. Last character:", text[-1])


print("c. First 5 characters:", text[:5])


print("d. Last 11 characters:", text[-11:])


print("e. Reversed string:", text[::-1])


print("f. Extracted word:", text[23:29])



strM = "Python beginner tutorial"


print("a. Uppercase:", strM.upper())


print("b. Lowercase:", strM.lower())


print("c. Capitalized:", strM.capitalize())


print("d. Count of 't':", strM.count('t'))


print("e. Replaced string:", strM.replace("Python", "Machine Learning"))





tuple1 = (10, 20, 30)
tuple2 = (40, 50, 60)


t_combine = tuple1 + tuple2
print("a. Combined tuple:", t_combine)


t_repeat = t_combine * 3
print("b. Repeated 3 times:", t_repeat)


print("c. 3rd element:", t_combine[2])


print("d. First 3 elements:", t_combine[:3])


print("e. Last 3 elements:", t_combine[-3:])
