while(True):
    username = input("请输入用户名：")
    password = input("请输入密码：")
    if username == "zhangshan":
        if password == "Python123":
            print("Zhangshan先生，欢迎你！")
            break
        else:
            print("对不起，密码错误，无法登陆")
    else:
        print("用户名错误，请重新输入！")

