# isinstance.py
class Person : 
    pass
class Bird : 
    pass
class Student(Person):
    pass
p, s = Person(), Student()

print("p is instance of Person:", isinstance(p,Person))
print("p is instance of Person:", isinstance(s,Student))
print("p is instance of Person:", isinstance(p,object))
print("p is instance of Person:", isinstance(p,Bird))
print("p is instance of Person:", isinstance(int,object))


