a = int(input("输入边长a："))
b = int(input("输入边长b："))
c = int(input("输入边长c："))
s = []
s = set(s)
if a + b > c and a + c > b and b + c > a:
    s.add(a)
    s.add(b)
    s.add(c)
    s = set(s)
    s = list(s)
    if len(s) == 2:
        print("该三角形为等腰三角形")
    if len(s) == 1:
        print("该三角形为等边三角形")
    if len(s) == 3:
        print("该三角形为普通三角形")
else:
    print("该三条边不能组成三角形")