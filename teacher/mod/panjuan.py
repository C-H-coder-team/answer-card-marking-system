import os
subject=['Chinese','Math','English','History','Politics',"Physics","Biology","Chemistry","Geography"]
class panjuan(object):
    def __init__(self):
        pass
    def __call__(self):
        pass
    #num指总数
    def panjuan(username,s,sub,numstart,numstop,total):
        for i in range(numstart,numstop+1):
            print("用户名：",username,'/n科目：',sub,'/n第',s,'题/n第',i-numstart,'份，共',numstop-numstart+1,'份')
            print("本题总分：",total)
            defen=float(input('/n本份得分：'))
            os.system('cls')
            #导出部分
            try:
                os.mkdir('mark')
            except BaseException:
                pass
            file=os.open(i+'.log',os.O_RDWR|os.O_CREAT)
            os.write(file,bytes("用户名："+username+'/n科目：'+sub+'/n第'+(i-numstart)+'份，共'+(numstop-numstart+1)+'份'+'/n总分：'+total+'得分：'+defen,'UTF-8'))
            os.close(file)
            file=os.open(i+'.mark',os.O_RDWR|os.O_CREAT)
            os.write(file,bytes(username+'/n'+s+'/n'+sub+'/n'+i+'/n'+defen))
            os.close(file)
        print("您已判完%d份卷",(numstop-numstart+1))