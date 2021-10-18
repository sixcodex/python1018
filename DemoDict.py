# DemoDict.py
device = {"아이폰":5, "아이패드":10, "윈도우":20}
print( device )
print( len(device) )
print( device["아이폰"] )
device["맥프레"] = 15
device["아이폰"] = 6
print( device )

del device["아이폰"]
for item in device.items():
    print(item)
print("---key, value---")
for k,v in device.items():
    print(k,v)
    

phone = {"kim":"111", "lee":"2222"}
p=phone
print(p)

#교집합을 구하는 함수
def intersect(prelist, postlist):
    #함수내부에만 있는 지역변수
    result=[]
    #단어 글자를 슬라이싱 하는 코드 H(0)|A(1)|M(2)
    for x in prelist:
        #postlist에도 있고 result에는 없는 글자면 추가
        if x in postlist and x not in result:
            result.append(x)
    #루프 다돌고 나면 Return
    return result

#함수 호출
print( intersect("HAM", "SPAM"))
