from mod import login
from mod import panjuan
import os
subject=['Chinese','math','english','history','politics',"Physics","Biology","Chemistry","Geography"]
user=[
{'name':'teacher1','username':'teacher2','password':'123456','status':'teacher','subject':subject[0]},
{'name':'teacher2','username':'teacher2','password':'123456','status':'teacher','subject':subject[0]}
]
print("""
欢迎来到答题卡阅卷系统老师端！
登录系统：
""")
loginusername=input("用户名：")
loginpassword=input("密码：")
st=login.login(loginusername,loginpassword)
print(st)
if st == '登录成功':
    os.system("cls")
    set=int(input("""老师操作菜单：
        1.进入判卷（请一次判完）
        2.退出程序"""))
    if set==1:
        
        infos=[]
        i=0
        for line in open('teacher.config'):
            infos.insert(i,line)
            i+=1
        panjuan.panjuan.panjuan(infos[0],infos[1],infos[2],infos[3],infos[4],infos[5])