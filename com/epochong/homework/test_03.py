a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))
d = {
     'a': a,
     'b': b,
     'c': c
}
d = sorted(d.items(),key=lambda item : item[1],reverse=True)

print("排序结果为：", d[0][0],">",d[1][0],">",d[2][0])

