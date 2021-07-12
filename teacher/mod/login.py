subject=['Chinese','math','english','history','politics',"Physics","Biology","Chemistry","Geography"]
user=[
{'name':'teacher1','username':'teacher2','password':'123456','status':'teacher','subject':subject[0]},
{'name':'teacher2','username':'teacher2','password':'123456','status':'teacher','subject':subject[0]}
]
def login(loginname,loginpassword):
    for u in user:
        if loginname == u['username'] and loginpassword == u['password']:
            return '登录成功'
    return "用户名/密码错误"
