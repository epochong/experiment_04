print("请输入ax2 + bx + c 的参数a,b,c:")
a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))
det = b ** 2 - 4 * a * c
if det < 0:
    print("无实根")
else:
    if det == 0:
        print("有一个根：")
        print("x1 = x2 = ",(-b + (det) * (1 / 2)) / (2 * a))
    else:
        print("有两个根：")
        print("x1 = ",(-b + (det) * (1 / 2)) / (2 * a), "x2 = ",(-b - (det) * (1 / 2)) / (2 * a))

