# DemoLoop.py
value = 5
while value > 0:
    print ( value )
    value -= 1

score = int(input("점수를 입력:"))

if 90<=score<=100:
    grade = "A"
elif 80<=score<90:
    grade = "B"
elif 70<=score<80:
    grade = "C"
else : 
    grade = "D"

print("등급은:",grade)

lst = [1,2,3,4,5]
for item in map(lambda i:i+10, lst):
    print(item)
    