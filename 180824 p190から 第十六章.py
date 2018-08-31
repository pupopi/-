#第十六章 Bash

#p207

import re

l = "Beautiful is better than ugly."
matches = re.findall("Beautiful", l)

print(matches)


import re

l = "Beautiful is better than ugly."
matches = re.findall("beautiful", l, re.IGNORECASE)

print(matches)


#209

import re

zen = """Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

m = re.findall("^If", zen, re.MULTILINE)
print(m)


import re

string = "Two too."
m = re.findall("t[ow]o", string, re.IGNORECASE)
print(m)



#211

import re

line = "123 hi 34 hello."
m = re.findall("\d", line, re.IGNORECASE)
print(m)


#212

import re

t = "_one_ _two_ _three_"
found = re.findall("_.*?_", t)
for match in found:
    print(match)



import re
text = """キリンは大昔から __複数名詞__ の興味の対象でした。
キリンは __複数名詞__ の中で一番背が高いですが、科学者たちはそのような長い __体の一部__ をどうやって獲得したのか説明できません。
キリンの身長は __数値__ __単位__ 近くあり、その高さのほとんどは脚と __体の一部__ によるものです。
"""

def mad_libs(self):
    """

    :param mls: 文字列で、ユーザーに入力してもらいたい単語(=ヒント)の部分は、後を2つのアンダースコアで挟んでください。
    ヒントの単語にはアンダースコアを含めないでください。__hint_hint__はだめです。__hint__はOKです。
    """
    hints = re.findall("__.*?__", mls)
    if hints is not None:
        for word in hints:
            q = "{} を入力:".format(word)
            new = input(q)
            mls = mls.replace(word, new, l)
        print('\n')
        mls = mls.replace("/n", "")
        print(mls)
    else:
        print("引数mlsが無効です")

mad_libs(text)


#214

import re
line = "I love $"
m = re.findall("\\$", line, re.IGNORECASE)
print(m)




#チャレンジ十六章

#16-1

zop = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

matches = re.findall("Dutch", zop)
print(matches)


#16-2 Linuxコード

#tanabe@DESKTOP-4HJE9GD:/mnt/c/users/tanabe/Desktop/独学プログラマー$ echo Arizona 479, 501 870. California 209, 213, 650. | grep [[:digit:]]
#結果：　Arizona 479, 501 870. California 209, 213, 650.　(数字だけ赤文字に)


#16-3 Python reモジュール

import re

ghost = "The ghost that says boo haunts the loo."
found = re.findall(".oo", ghost)
print(found)


#第十八章

#p218

from flask import Flask

app = Flask(__name__)
@app.route('/')
def index():
    return "Hello, World!"

app.run(port=8000)



#第十九章