dict_marks = {'Alice': 85, 'Bob':56, 'John':72}
name = input('Enter the student\'s name: ')
if(name in dict_marks):
    print(name,'\'s marks: ', dict_marks[name])
else:
    print("Student not found.")