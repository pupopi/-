#第四章　関数

def f(x):
    return x*2
f(2)
result = f(2)
print(result)


def f(x):
    return x+1

z=f(4)

if z==5:
    print("z is 5")
else:
    print("z is not 5")


def f():
    return 1+1

result = f()
print(result)


def f(x,y,z):
    return x+y+z

result=f(1,2,3)
print(result)


def f():
    z=1+1

result=f()
print(result)


#組み込み関数　p54

len("Monty")
len("Python")

str(100)

int("1")

float(100)

int("110")
int(20.54)

float("16.4")
float(99)

int("Prince")


age = input("Enter your age:")
int_age = int(age)
if int_age < 21:
    print("You are young!")
else:
    print("You are old!")


#関数を再利用する　p57

def even_odd(x):
    if x%2==0:
        print("偶数")
    else:
        print("奇数")

even_odd(2)
even_odd(3)


n=input("type a number:")
n=int(n)
if n%2==0:
    print("n is even.")
else:
    print("n is odd.")

n=input("type a number:")
n=int(n)
if n%2==0:
    print("n is even.")
else:
    print("n is odd.")

n=input("type a number:")
n=int(n)
if n%2==0:
    print("n is even.")
else:
    print("n is odd.")


def even_odd():
    n=input("type a number:")
    n=int(n)
    if n%2==0:
        print("n is even.")
    else:
        print("n is odd.")

even_odd()
even_odd()
even_odd()


#必須引数とオプション引数

def f(x=2):
    return x**x

print(f())
print(f(4))


def add_it(x, y=10):
    return x+y
result=add_it(2)
print(result)


#スコープ　p60

x=1
y=2
z=3

def f():
    print(x)
    print(y)
    print(z)

f()

def f():
    x=1
    y=2
    z=3

print(x)
print(y)
print(z)


def f():
    x=1
    y=2
    z=3
    print(x)
    print(y)
    print(z)

f()


if x>100:
    print("x is > 100")


x=100

def f():
    global x
    x+=1
    print(x)

f()


#例外処理　p63

a=input("type a number:")
b=input("type another:")
a=int(a)
b=int(b)
print(a/b)


a=input("type a number:")
b=input("type another:")
a=int(a)
b=int(b)

try:
    print(a/b)
except ZeroDivisionError:
    print("b cannot be zero.")


try:
    a=input("type a number:")
    b=input("type another:")
    a=int(a)
    b=int(b)
    print(a/b)
except(ZeroDivisionError, ValueError):
    print("Invalid input.")


try:
    10/0
    c="I will never get defined."
except ZeroDivisionError:
    print(c)


#ドキュメンテーション文字列　p67

def add(x,y):
    """
    Returns x+y.
    :param x: int.
    :param y: int.
    :return: int sum of x and y.
    """
    return x+y


x=100
print(x)

print(100)



#五章　コンテナ　p70

"Hello".upper()
"Hello".replace("o","@")


#リスト　p71

fruit = list()
fruit

fruit = list[]
fruit

fruit = ["Apple","Orange","Pear"]
fruit

fruit = ["Apple", "Orange", "Pear"]
fruit.append("Banana")
fruit.append("Peach")
fruit

random = []
random.append(True)
random.append(100)
random.append(1.1)
random.append("Hello")
random

fruit = ["Apple", "Orange", "Pear"]
fruit[0]
fruit[1]
fruit[2]

colours = ["blue", "green", "yellow"]
colours[4]

colours = ["blue", "green", "yellow"]
colours
colours[2]="red"
colours

colours = ["blue", "green", "yellow"]
colours
item = colours.pop()
item
colours

colours1 = ["blue", "green", "yellow"]
colours2 = ["orange", "pink", "black"]
colours1+colours2

colours = ["blue", "green", "yellow"]
"green" in colours

colours = ["blue", "green", "yellow"]
"black" not in colours

colours = ["purple", "orange", "green"]
guess = input("何色でしょう？(入力してください):")
if guess in colours:
    print("当たり！")
else:
    print("ハズレ！また挑戦してね。")


#タプル　p76

my_tuple = tuple()
my_tuple

my_tuple = ()
my_tuple

rndm = ("M.Jackson", 1958, True)
rndm

#これはタプルです。
("self_taught",)

#これはタプルではなく数値演算に使うカッコです。
(9)+1

dys = ("1984", "Brave New World", "Fahrenheit 451")
dys[1]="Handmaid's Tale"

dys = ("1984", "Brave New World", "Fahrenheit 451")
dys[2]

dys = ("1984", "Brave New World", "Fahrenheit 451")
"1984" in dys

dys = ("1984", "Brave New World", "Fahrenheit 451")
"Handmaid's Tale" not in dys


#辞書　p78

my_dict = dict()
my_dict

my_dict = {}
my_dict

fruits = {"Apple":"Red","Banana":"Yellow"}
fruits

facts = dict()
#バリューを追加
facts["code"]="fun"
#キーで参照
facts["code"]

#バリューを追加
facts["Bill"]="Gates"
#キーで参照
facts["Bill"]

#バリューを追加
facts["founded"]=1776
#キーで参照
facts["founded"]

bill={"Bill Gates":"charitable"}
"Bill Gates" in bill

bill={"Bill Gates":"charitable"}
"Bill Doors" not in bill

books={"Dracula":"Stoker", "1984":"Orwell", "The Trial":"kafka"}
del books["The Trial"]
books

songs={"1":"fun","2":"blue","3":"me","4":"flooe","5":"live"}
n=input("数字を入力してください:")
if n in songs:
    song = songs[n]
    print(song)
else:
    print("見つかりません")


#コンテナの中のコンテナ　p83

lists =[]
rap = ["カニエ・ウェスト", "ジェイ・ｚ","エミネム","ナズ"]
rock = ["ボブ・ディラン", "ザ・ビートルズ", "レッド・ツェッペリン"]
djs = ["ゼッズ・デッド","ティエスト"]

lists.append(rap)
lists.append(rock)
lists.append(djs)

print(lists)

rap = lists[0]
print(rap)

rap = lists[0]
rap.append("ケンドリック・ラマー")
print(rap)
print(lists)


locations =[]
la = (34.0522, 188.2437)
chicago = (41.8781, 87.6298)

locations.append(la)
locations.append(chicago)

print(locations)


eights = ["Edgar Allan Poe","Charles Dickens"]
nines = ["Hemingway", "Fitzgerald", "Orwell"]

authors = (eights, nines)
print(authors)


bday = {"Hemingway":"7.21.1899", "Fitzgerald":"9.24.1896"}
my_list = [bday]
print(my_list)
my_tuple = (bday,)
print(my_tuple)


ny = {
    "座標": (40.7128, 74.0059),
    "セレブ": ["ウッディ・アレン", "ジェイ・ｚ", "ケヴィン・ベーコン",],
    "事実":{"州":"ニューヨーク", "国":"アメリカ"}
}