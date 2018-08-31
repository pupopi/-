
""" line one
    line two
    line three
"""

author="Kafka"
author[0]
author[1]
author[2]
author[3]
author[4]

author="Kafka"
author[5]

author="Kafka"
author[-1]

author="Kafka"
author[-2]
author[-3]


#文字列はイミュータブル

ff="F. Fitzgerald"
ff="F. Scott Fitzgerald"
ff

#文字列の足し算

"cat"+" in"+" hat"

"cat"+" in"+" the"+" hat"

#文字列の掛け算

"Sawyer"*3

#分割

"水たまりを飛び越えたんだ。3メートルもあったんだぜ！".split("。")

#結合

first_three="abc"
result="+".join(first_three)
result

words=["The", "fox", "jumped", "over", "the","fence","."]
one="".join(words)
one

one=" ".join(words)
one

#空白除去

s="   The   "
s=s.strip()
s

#置換

equ= "All animars are equall."
equ=equ.replace("a","@")
print(equ)

#文字を探す

"animals".index("m")

"animals".index("z")

try:
    "animals".index("z")
except:
    print("Not found.")

#包含

"Cat" in "Cat in the hat."

"Bat" in "Cat in the hat."

"Potter" not in "Harry"

#エスケープ文字

"彼女は"そうだね"と言った。"

"彼女は\"そうだね\"と言った。"

"彼女は\'そうだね\'と言った。"

"彼女は'そうだね'と言った。"

'彼女は"そうだね"と言った。'

#改行

print("line1\nline2\nline3")

#スライス

fict=["トルストイ", "カミュ", "オーウェル", "ハクスリー", "オースティン"]
fict[0:3]

ivan="死の代わりにひとつの光があった。"
ivan[0:6]
ivan[6:16]

ivan[:6]
ivan[6:]

ivan[:]