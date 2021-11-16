"""
섭씨온도를 입력 받아서 화씨로 변환하기
"""
def fah_convert(celsius) :
    return ((9/5)*float(celsius)+32)

print("변환하고 싶은 섭씨온도를 입력하세요 >> ")
user_input = input()
print(type(user_input), user_input)

fah=fah_convert(user_input)
print("화씨 온도 : " + str(user_input))
print("섭씨 온도 : {0:.2f}".format(fah))
