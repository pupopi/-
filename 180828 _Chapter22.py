
for i in range(1, 101):
    if i % 3 == 0 and i % 5 ==0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)


def ss(number_list, n):
    found = False
    for i in number_list:
        if i == n:
            found = True
            break
    return found

numbers = range(0, 100)
sl = ss(numbers, 2)
print(sl)
s2 = ss(numbers, 202)
print(s2)



def palindrome(word):
    word = word.lower()
    return word[::-1] == word

print(palindrome("Mother"))
print(palindrome("Mom"))



def anagram(w1,w2):
    w1 = w1.lower()
    w2 = w2.lower()
    return sorted(w1) == sorted(w2)

print(anagram("iceman", "cinema"))
print(anagram("leaf", "tree"))



def count_characters(string):
    count_dict = {}
    for c in string:
        if c in count_dict:
            count_dict[c] += 1
        else:
            count_dict[c] = 1

    print(count_dict)

count_characters("Dynasty")


#なぜか動かない

def bottles_of_beer(bob):
    """Prints Bottle of Beer on the Wall lyrics.

    :param bob: Must be positive integer.
    """

if bob < 1:
    print("""No more bottles of beer on the wall.
            No more bottles od beer.""")
        return

    tmp = bob
    bob -= 1
    print("""{} bottles of beer on the wall.
            {} bottles of beer.
            Take one down, pass it around,
            {} bottles of beer on the wall.""".format(tmp, tmp, bob))
    bottles_of_beer(bob)

bottles_of_beer(99)


#上の動かないのでURLからコピペ

def bottles_of_beer(bob):
    """ Prints 99 Bottle 
        of Beer on the
        Wall lyrics.
        :param bob: Must
        be a positive 
        integer.
    """
    if bob < 1:
        print("""No more 
                 bottles 
                 of beer 
                 on the wall. 
                 No more 
                 bottles of 
                 beer.""")
        return
    tmp = bob
    bob -= 1
    print("""{} bottles of 
             beer on the 
             wall. {} bottles
             of beer. Take one 
             down, pass it 
             around, {} bottles 
             of beer on the 
             wall.
          """.format(tmp, 
                     tmp, 
                     bob))
    bottles_of_beer(bob)


bottles_of_beer(99)




