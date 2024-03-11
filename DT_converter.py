import tkinter as tk
from tkinter import *
import tkinter.messagebox as messagebox
import datetime
from cmath import nan
################
'''窗口'''
dtc = tk.Tk()
dtc.title('时间/进制转换器')
##dtc.iconbitmap("dtc.ico")
dtc.geometry("280x350+638+320")

dtnow = Label(dtc, text = '当前日期')
dtnow.grid(row = 0, columnspan = 6, column = 0)

tyearnow = Label(dtc, text ='年')
tyearnow.grid(row = 1, column = 1, padx = 2)

tmonthnow = Label(dtc, text ='月')
tmonthnow.grid(row = 1, column = 3, padx = 2)

tmonthnow = Label(dtc, text ='日')
tmonthnow.grid(row = 1, column = 5, padx = 2)

tfebid = Label(dtc, text = '初雪日期')
tfebid.grid(row = 3, columnspan = 6, column = 0)

tfebid = Label(dtc, text = '瓦其夫日期')
tfebid.grid(row = 5, columnspan = 6, column = 0)

tnow = Label(dtc, text = '当前时间')
tnow.grid(row = 7, columnspan = 6, column = 0)

thournow = Label(dtc, text ='时')
thournow.grid(row = 9, column = 1, padx = 2)

tminnow = Label(dtc, text ='分')
tminnow.grid(row = 9, column = 3, padx = 2)

tsecnow = Label(dtc, text ='秒')
tsecnow.grid(row = 9, column = 5, padx = 2)

tnow = Label(dtc, text = '瓦其夫时间')
tnow.grid(row = 10, columnspan = 6, column = 0)

trans10_4 = Label(dtc, text = '10-4进制转换')
trans10_4.grid(row = 12, columnspan = 6, column = 0)

num10 = Label(dtc, text = '十进制:')
num10.grid(row = 13, column = 0)

num4 = Label(dtc, text = '四进制:')
num4.grid(row = 13, column = 3)

numbalstz = Label(dtc, text = '传统音节表示：')
numbalstz.grid(row = 14, columnspan = 2, column = 0)

# entry box
yearnow = Entry(dtc, width = 5, justify = CENTER)
yearnow.grid(row = 1, column = 0, sticky = tk.E, padx = 2)

monthnow = Entry(dtc, width = 5, justify = CENTER)
monthnow.grid(row = 1, column = 2, sticky = tk.E, padx = 2)

datenow = Entry(dtc, width = 5, justify = CENTER)
datenow.grid(row = 1, column = 4, sticky = tk.E, padx = 2)

hournow = Entry(dtc, width = 5, justify = CENTER)
hournow.grid(row = 9, column = 0, sticky = tk.E, padx = 2)

minnow = Entry(dtc, width = 5, justify = CENTER)
minnow.grid(row = 9, column = 2, sticky = tk.E, padx = 2)

secnow = Entry(dtc, width = 5, justify = CENTER)
secnow.grid(row = 9, column = 4, sticky = tk.E, padx = 2)

# out trans
febidoutputLabel = tk.StringVar()
febidoutput = tk.Label(dtc, textvariable = febidoutputLabel, font = ('Arial',10))
febidoutput.grid(row = 4, columnspan = 6, column = 0)

wagifuroutputLabel = tk.StringVar()
wagifuroutput = tk.Label(dtc, textvariable = wagifuroutputLabel, font = ('Arial',10))
wagifuroutput.grid(row = 6, columnspan = 6, column = 0)

timeoutputLabel = tk.StringVar()
timeoutput = tk.Label(dtc, textvariable = timeoutputLabel, font = ('Arial',10))
timeoutput.grid(row = 11, columnspan = 6, column = 0)

num10EL = tk.StringVar()
num10bx = Entry(dtc, textvariable = num10EL, width = 8, justify = RIGHT)
num10bx.grid(row = 13, column = 1, columnspan = 2, sticky = tk.E)

num4EL = tk.StringVar()
num4bx = Entry(dtc, textvariable = num4EL, width = 8, justify = RIGHT)
num4bx.grid(row = 13, column = 4, columnspan = 2, sticky = tk.E)

balstzopLabel = tk.StringVar()
balstzop = tk.Label(dtc, textvariable = balstzopLabel, font = ('Pinaaz',14))
balstzop.grid(row = 14, column = 3, columnspan = 3, sticky = tk.E)

# 10/20 trans
#h1020 = tk.StringVar()
#h1020.set('10')

#h1020.h10 = Radiobutton(dtc, text='10小时制')
#h1020.h20 = Radiobutton(dtc, text='20小时制') 


def transdate():
    days()
    febidoutputLabel.set('%d年%d月%d日'%(febidyear(),febidmonth(),febiddate()))
    wagifuroutputLabel.set('%d年%s月%d日'%(wayear(),wamonth(),wadate()))

def transtime():
    timeswitch()
    timeoutputLabel.set('%d时%d分%d秒'%(wahr(),wamin(),wasec()))

def deldate():
    yearnow.delete(0,END)
    monthnow.delete(0,END)
    datenow.delete(0,END)

def deltime():
    hournow.delete(0,END)
    minnow.delete(0,END)
    secnow.delete(0,END)

def transnum():
    if num10EL.get():
        if int(num10EL.get())>262143:
           messagebox.showinfo('错误','太大了！\n需要小于262143') 
        else:
            num4EL.set(dec2quat(num10EL.get()))
            balstzopLabel.set(balstz(dec2quat(num10EL.get())))
    elif num4EL.get():
        if int(num4EL.get())>333333333:
            messagebox.showinfo('错误','太大了！\n需要小于333333333')
        elif ('4' or '5 'or '6' or '7' or '8' or '9') in num4EL.get():
            messagebox.showinfo('错误','请输入正确的四进制数字。')
        else:
            num10EL.set(quat2dec(num4EL.get()))
            balstzopLabel.set(balstz(num4EL.get()))

def delnum():
    num10bx.delete(0,END)
    num4bx.delete(0,END)

inputbut1 = Button(dtc, text = '转换', command = transdate, relief = 'raised')
inputbut1.grid(row = 1, rowspan = 2, column = 6)

clearbut1 = Button(dtc, text = '清除', command = deldate, relief = 'raised')
clearbut1.grid(row = 3, rowspan = 2, column = 6)

inputbut2 = Button(dtc, text = '转换', command = transtime, relief = 'raised')
inputbut2.grid(row = 8, rowspan = 2, column = 6)

clearbut2 = Button(dtc, text = '清除', command = deltime, relief = 'raised')
clearbut2.grid(row = 10, rowspan = 2, column = 6)

inputbut3 = Button(dtc, text = '转换', command = transnum, relief = 'raised')
inputbut3.grid(row = 15, column = 2)

clearbut3 = Button(dtc, text = '清除', command = delnum, relief = 'raised')
clearbut3.grid(row = 15, column = 4)

############
'''获得时间'''
def days():
    global nowyear,nowmonth, nowdate
    nowyear = int(yearnow.get()) if yearnow.get() else 0
    nowmonth = int(monthnow.get()) if monthnow.get() else 0
    nowdate = int(datenow.get()) if datenow.get() else 0
    if nowyear == 0 or nowmonth == 0 or nowdate == 0:
        messagebox.showinfo('错误','请输入日期。')
    elif nowyear < 1970 or nowyear >9999:
        messagebox.showinfo('错误','太久远了！')
    elif nowmonth > 12 or wrongdate() == 1:
        messagebox.showinfo('错误','请输入正确的日期。')
    else:
        tnldate = datetime.datetime(nowyear,nowmonth,nowdate)
        datefrst = datetime.datetime(1985, 1, 1)
        #这样2013.12.19就是91年2月1日#
        daysdelta = (tnldate - datefrst).days
    return daysdelta

'''日期转换'''
def febidyear():
    fy = days()//320+2263
    return fy

def febidmonth():
    fm = (days()%320)//32+1
    return fm

def febiddate():
    fd = days() - (febidmonth()-1)*32 - (febidyear()-2263)*320+1
    return fd

def wayear():
    wy = days()//320+58
    return wy

def wamonth():
    wam = (days()-(febidyear()-2263)*320)//20+1
    if wam == 1: wm = '神圣(1)'
    elif wam == 2:wm = '泉水(2)'
    elif wam == 3:wm = '种植(3)'
    elif wam == 4:wm = '香料(4)'
    elif wam == 5:wm = '休息(5)'
    elif wam == 6:wm = '炎热(6)'
    elif wam == 7:wm = '降雨(7)'
    elif wam == 8:wm = '月亮(8)'
    elif wam == 9:wm = '中间(9)'
    elif wam == 10:wm = '登山(10)'
    elif wam == 11:wm = '收获(11)'
    elif wam == 12:wm = '出行(12)'
    elif wam == 13:wm = '大风(13)'
    elif wam == 14:wm = '大雪(14)'
    elif wam == 15:wm = '征服(15)'
    elif wam == 16:wm = '朝拜(16)'
    return wm

def wadate():
    wd = (days()-(febidyear()-2263)*320)%20+1
    return wd

def runnian():
    if (nowyear % 4) == 0:
        if (nowyear % 100) == 0:
            if (nowyear % 400) == 0:
                run = 1
            else:
                run = 0
        else:
            run = 1
    else:
        run = 0
    return run

def wrongdate():
    if ((nowmonth == 1) or (nowmonth == 3) or (nowmonth == 5) or (nowmonth == 7) or (nowmonth == 8) or (nowmonth == 10) or (nowmonth == 12)) and nowdate > 31:
        wrong = 1
    elif ((nowmonth == 4) or (nowmonth == 6) or (nowmonth == 9) or (nowmonth == 11)) and nowdate > 30:
        wrong = 1
    elif nowmonth == 2:
        if runnian()==0 and nowdate > 28:
            wrong = 1
        elif runnian()==1 and nowdate > 29:
            wrong = 1
        else: wrong = 0
    else: wrong = 0
    return wrong

'''十进制与四进制间转换'''
def dec2quat(d):
    dec=int(d)
    s=[]
    quatstr=''
    while dec>0:
        s.append(dec%4)
        dec//=4
    while len(s)>0:
        quatstr+=str(s.pop())
    if quatstr=='':quatstr='0'
    return quatstr

def quat2dec(quat):
    dec=0
    for x in range(len(quat)):
        dec+=int(quat[len(quat)-1-x])*4**x
    return dec

'''传统音节数字表示法'''
def balstz(numany):
    num=int(numany)
    i=0
    l=0
    z=0
    res = []
    s=['k','','t','','C','','c','','s','','S','','T','','f','','n','']
    #1, 10, 100, 1000, 1 0000, 10 0000, 100 0000, 1000 0000, 1 0000 0000
    stz=''
    while num:
        res.append(tostz(num % 10))
        num //= 10
        l+=1
    #~~逆序，按正常的顺序返回~~
    #**从低位到高位表示，不需要reverse(即使是倒序也不需要reverse方法，只需[::-1]即可)**
    #res.reverse()
    while i<l and i>=0:
        s[2*i+1] = res[i]
        i+=1
    stz=''.join(s[0:l*2])
    return stz

def tostz(numin):
    if numin == 0: return '';
    elif numin == 1: return 'a';
    elif numin == 2: return 'i';
    elif numin == 3: return 'u';
    else: return 'o'

'''时分秒转换'''
def timeswitch():
    global allmin, nowsec
    nowhr = int(hournow.get()) if hournow.get() else 0
    nowmin = int(minnow.get()) if minnow.get() else 0
    nowsec = int(secnow.get()) if secnow.get() else 0
    if nowhr > 23 or nowmin > 59 or nowsec > 59:
        messagebox.showinfo('错误','请输入正确的时间。')
        nowhr = nan
        nowmin = nan
        nowsec = nan
    else:
        allmin = nowhr*60+nowmin
        return allmin

def wahr():
    swhr = allmin//72
    return swhr

def wamin():
    swmin = allmin%72
    return swmin

def wasec():
    swsec = nowsec//5*6
    return swsec

dtc.mainloop()
