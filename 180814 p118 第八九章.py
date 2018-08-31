
#第八章　モジュール

import math
math.pow(2,3)

import random
random.randint(0,100)

import statistics
nums=[1,5,33,12,46,33,2]
statistics.mean(nums)
statistics.median(nums)
statistics.mode(nums)

import keyword
keyword.iskeyword("for")
keyword.iskeyword("football")


#第九章　ファイル

import os
os.path.join("Users", "bob", "st.text")

st = open("st.txt","w")
st.write("Hi from Python!")
st.close()

with.open("st.txt","w") as f:
    f.write("Hi from Python!")

with.open("st.txt", "r")af f:
    print(f.read())

my_list[]
with.open("st.txt","r")af f:
    my_list.append(f.read())
print(my_list)


import csv
with.open("st.csv", "w", newline=)as f:
    w=csv.writer(f, delimiter=",")
    w.writerow(["one", "two", "three"])
    w.writerow(["four", "five", "six"])

