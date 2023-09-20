# change 80 to 89
student_marks=[60,80,90,98]
student_marks[1]=89
print(student_marks)

# Adding a new item to the list
student_marks.append(55)
print(student_marks)

# Size of the list having appended
print(len(student_marks))

# Python program to sum up all items in the list
print(sum(student_marks))

list1=input("Enter items of list1:")
list2=input("Enter items of list2:")
def common_member(list1, list2):
    result = True
    for x in list1:
        for y in list2:
            if x == y:
                result = True
                return result
print(common_member(list1, list2))
