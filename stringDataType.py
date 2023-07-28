str = "Life is too short, You need Python"

print(str[0])


# python indexing
# myStr[0:0:0] << 의미 : 이상:미만:간격

# myStr[0] << 에서 [] 안의 숫자는 index를 의미한다.
print("str의 0번째 인덱스 = " + str[0] + "\n")

# -1 , -2 는 해당 문자열의 0번째 기준 뒤로 1칸 뒤로 2칸을 의미한다.
print("str의 -1번째 인덱스 = " + str[-1] + "\n")

# myStr[0:4] << 는 0번째 index 이상 ~ 4번째 index 미만을 의미하여 >> Life가 출력 됨
print(str[0:4] + "\n")
myStr2 = "20230726_Jason"
print("myStr2 = " + myStr2[:8] + "\n")

# [::2] << 2의 간격으로 띄워진 문자열만 출력된다.
print("2칸 띄운 myStr2 = " + myStr2[::2] + "\n")

# %s는 문자열을 의미하기 때문에 type 상관없이 값을 그대로 보여주기엔 편리함.
dataTy = 77
str2 = "I ate %s apples. so I was sick for %s days." % (1.2, dataTy)
print("str2 = " + str2)

""" 
1. {} 을 사용하기 위해 .foramt("넣고자 하는 값") 을 입력하면 된다. 

2. {} 안에 변수 사용도 가능하다.  
  1) {} 안에 변수 명을 넣어준다. ex) name
  2) 문자열 마지막에 .format() 함수의 매개변수로 변수를 설정해준다.
"""

# 1번 예시
str3 = "Hi I'm {}! Nice to meet you!".format("youngcheol")
print("str3 =" + str3)

# 2번 예시
str4 = "Hi I'm {name}, {age}!  Nice to meet you!".format(name="영철", age=20)
print("str4 = " + str4)


"""
float형 변수 선언 시 형태 > "%f" % 실수 값  
float형 변수 소수점 몇번째 자리까지 노출 시킬것인가? > "%0.4f" % 실수 값
여기서 0.4 의 의미는 소수점 몇번째 까지 자를 것인가에 대한 설정
"""
myFloat = "%f" % 0.342789157652156
print("myFloat = " + myFloat)


"""
count 함수
 - 해당 문자열에서 찾고자 하는 값만 출력
"""

myCount = "hobby"
print("myCount(b) = " + myCount.count("b"))
