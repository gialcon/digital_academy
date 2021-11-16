my_list1 = [20,30,40]
my_list2 = list()

my_list1.append(10)
print(my_list1)
my_list1.extend([50,60])
print(my_list1)
my_list1.insert(0,10)
print(my_list1)

#set
my_set = set(my_list1)
print(my_set)

my_tuple = (10,20,30)
my_tuple1 = tuple()
print(type(my_tuple))
print(my_tuple)

def swap(a,b):
    return (b,a)

n1, n2 = swap(10,20)
print(n1)
print(n2)

#문자열 타입 List 선언
cat_list = list('cat')
print(cat_list)

birth_day = "2021/11/16"
birth_list = birth_day.split("/")
print(birth_list)
print('2021' in birth_list)
print('2021' not in birth_list)

if '2020' not in birth_list :
    print('not found')


