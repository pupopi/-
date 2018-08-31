#第十二章

#手続き型プログラミング

x=2
y=4
z=8
xyz=x+y+z
xyz


pop=[] #洋楽ポップソングを保存するリスト
jpop=[] #JPopソングを保存するリスト

def collect_songs():
    song="曲名を入力してください:"
    ask="ｐかｊかのどちらかを入力してください。ｑで終わります。:"

    while True:
        genre=input(ask)
        if genre=="q":
            break

        if genre=="p":
            p=input(song)
            pop.append(p)

        elif genre=="j":
            j=input(song)
            jpop.append(j)

        else:
            print("不正な値です。")

    print("pop songs: ", pop)
    print("jpop songs: ", jpop)

collect_songs()

#関数型プログラミング

a=0
def increment():
    global a
    a+=1

def increment(a):
    return a+1


#オブジェクト指向プログラミング

class Orange:
    def _init_(self):
        print("Created!")

class Orange:
    def _init_(self, w, c):
        self.weight = w
        self.color = c
        print("Created!")

class Orange:
    def _init_(self, w, c):
        self.weight = w
        self.color = c
        print("Created!")
or1 = Orange(10, "dark orange")
print(or1)

class Orange:
    def _init_(self, w, c):
        self.weight = w
        self.color = c
        print("Created!")
or1=Orange(10, "dark orange")
print(or1.weight)
print(or1.color)


class Orange:
    def _init_(self, w, c):
        self.weight=w
        self.color=c
        print("Created!")

or1 = Orange(10, "dark orange")
or1.weight = 100
or1.color = "light orange"

print(or1.weight)
print(or1,color)


class Orange:
    def _init_(self, w, c):
        """weight(重さ)はグラム"""
        self.weight = w
        self.color = c
        self.mold = 0
        print("Created!")

    def rot(self, days, temp):
        """temp(温度)は摂氏"""
        self.mold=days*temp

orange = Orange(200, "orange")
print(orange.mold)
orange.rot(10, 37)
print(orange.mold)



class Rectangle:
    def __ini__(self, w, l):
        self.width = w
        self.lrn = 1

    def area(self):
        return self.width * self.len

    def change_size(self, w, l):
        self.width = w
        self.len = l

rectangle = Rectangle(10, 20)
print(rectangle.area())
rectangle.change_size(20, 40)
print(rectangle.area())



#第十三章　オブジェクト指向プログラミングの４大要素

#カプセル化

class Rectangle:
    def __init__(self, w, l):
        self.width = w
        self.len = 1

    def area(self):
        return self.width * self.len


class Data:
    def __init__(self):
        self.nums = [1, 2, 3, 4, 5]

    def change_data(self, index, n):
        self.nums[index] = n


class Data:
    def __init__(self):
        self.nums = [1, 2, 3, 4, 5]

    def change_data(self, index, n):
        self.nums[index] = n

data_one = Data()
data_one.nums[0] = 100
print(data_one.nums)

data_two = Data()
data_two.change_data(0, 100)
print(data_two.nums)


class PublicPrivateExample:
    def __init__(self):
        self.public = "safe"
        self.unsafe = "unsafe"

    def public_method(self):
        # client が使ってもよい
        pass # pass文は、文が必須な構文で何もしない場合に使う

    def _unsafe_method(self):
        # client は使うべきじゃない
        pass # pass文は、文が必須な構文でも何もしない場合に使う


print("Hello, World!")
print(200)
print(200.1)


type("Hello, World!")
type(200)
type(200.1)


#継承

class Shape:
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def print_size(self):
        print("{} by {}".format(self.width, self.len))

my_shape = Shape(20, 25)
my_shape.print_size()


class Shape:
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def print_size(self):
        print("{} by {}".format(self.width, self.len))

class Square(Shape):
    pass

a_square = Square(20, 20)
a_square.print_size()


class Shape:
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def print_size(self):
        print("{} by {}".format(self.width, self.len))

class Square(Shape):
    def area(self):
        return self.width * self.len

a_square = Square(20, 20)
print(a_square.area())


class Shape:
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def print_size(self):
        print("{} by {}".format(self.width, self.len))

class Square(Shape):
    def area(self):
        return self.width * self.len
    
    def print_size(self):
        print("I am {} by {}".format(self.width, self.len))

a_square = Square(20, 20)
a_square.print_size()


#コンポジション　p167

class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

class Person:
    def __init__(self, name):
        self.name = name

mick = Person("Mick Jagger")
stan = Dog("Stanley", "Bulldog", mick)
print(stan.owner.name)


#第十四章　もっとオブジェクト指向プログラミング

class Square:
    pass
print(Square)


class Rectangle:
    def __init__(self, w, l):
        self.width = w
        self.len = l
    
    def print_size(self):
        print("{} by {}".format(self.width, self.len))

my_rectangle = Rectangle(10, 24)
my_rectangle.print_size()


class Rectangle:
    recs = []

    def __init__(self, w, l):
        self.width = w
        self.len = l
        self.recs.append((self.width, self.len))

    def print_size(self):
        print("{} by {}".format(self.width, self.len))

r1 = Rectangle(10, 24)
r2 = Rectangle(20, 40)
r3 = Rectangle(100, 200)

print(Rectangle.recs)



#特殊メソッド

class Lion:
    def __init__(self, name):
        self.name = name

lion = Lion("Dilbert")
print(lion)



class Lion:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name
lion = Lion("Dilbert")
print(lion)



class AlwaysPositive:
    def __init__(self, number):
        self.n = number

    def __add__(self, other):
        return abs(self.n + other.n)

x = AlwaysPositive(-20)
y = AlwaysPositive(10)
print(x+y)



# is 

class Person:
    def __init__(self):
        self.name = 'Bob'

bob = Person()
same_bob = bob
print(bob is same_bob)

another_bob = Person()
print(bob is another_bob)


x = 10
if x is None:
    print("xはNone")
else:
    print("xはNoneじゃない")

x = None
if x is None:
    print("xはNone")
else:
    print("xはNoneじゃない :(")



#第十五章　知識を1つにまとめる

#card

class Card:
    suits = ["spades", "hearts", "diamonds", "clubs"]

    value = [None, None, "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    def __init__(self, v,s):
        """スート(マーク)も値も整数値です"""
        self.value = v
        self.suit = s

    def __lt__(self, c2):
        if self.value < c2.value:
            return True

        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False

    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False

    def __repr__(self):
        v = self.values[self.value] + " of " \
            + self.suits[self.suit]
        return v

card1 = Card(10, 2)
card2 = Card(11, 3)
print(card1 < card2)

card1 = Card(10, 2)
card2 = Card(11, 3)
print(card1 > card2)

card = Card(3, 2)
print(card)


#Deck

from random import shuffle

class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i, j))

    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()

deck = Deck()
for card in deck.cards:
    print(card)


#Player

class Player:
    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.name = name


#Game

class Game:
    def __init__(self):
        name1 = input("プレイヤー1の名前")
        name2 = input("プレイヤー2の名前")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def wins(self, winner):
        w = "このラウンドは{}が勝ちました"
        w = w.format(winner)
        print(w)

    def draw(self, p1n, p1c, p2n, p2c):
        d = "{} は  {}、 {} は {} を引きました"
        d = d.format(p1n, p1c, p2n, p2c)
        print(d)

    def play_game(self):
        cards = self.deck.cards
        print("戦争を始めます！")
        while len(cards) >= 2:
            m = "qで終了、それ以外のキーでPlay:"
            response = input(m)
            if response =="q":
                break
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n, p1c, p2n, p2c)
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)

        win = self.winner(self.p1, self.p2)
        print("ゲーム終了、{} の勝利です！".format(win))

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return pl.name
        if p1.wins < p2.wins:
            return p2.name
        return "引き分け！"

