import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
import tkinter.messagebox as messagebox
################
'''窗口'''
rc = tk.Tk()
rc.title('词根屈折器')
rc.geometry("300x150+605+320")

txt1 = Label(rc, text = '词根：')
txt1.grid(row = 0, column = 0, sticky = tk.W)

# entry box
entry = Entry(rc, width = 15)
entry.grid(row = 0, column = 1, sticky = tk.W, padx = 2)

# conjugate type select
values = ['名词','形容词','动词']
conjtypselect=ttk.Combobox(rc, height = 4, width = 12, state = 'readonly', values = values)
conjtypselect.current(0)
conjtypselect.grid(row = 1, column = 1, sticky = tk.W, padx = 2)

valuesn = ['基本名词','地点名词','结果名词','善者名词','程度名词','宏大名词','工具名词','工具地点名词','特征人名词']
conjtypselectn=ttk.Combobox(rc, height = 4, width = 12, state = 'readonly', values = valuesn)
conjtypselectn.current(0)

valuesadj = ['最高级','自动转义形容词','他动转义形容词','易于...的','难于...的','令人...的','善于...的','工具形容词']
conjtypselectadj=ttk.Combobox(rc, height = 4, width = 12, state = 'readonly', values = valuesadj)
conjtypselectadj.current(0)

valuesv = ['一般使役','一般被动','一般使役被动','敬语使役','敬语被动','敬语使役被动','能力形','能力使役','能力被动','能力使役被动','能力形否定','能力使役否定','能力被动否定','能力使役被动否定','中止体','濒临体','经历体','自动变化','他动变化']
conjtypselectv=ttk.Combobox(rc, height = 6, width = 12, state = 'readonly', values = valuesv)
conjtypselectv.current(0)

varnounpl = IntVar()
plcheck=Checkbutton(rc,text = '复数',variable = varnounpl)
################
'''词根输入'''
illigal=[' ','i','u','e','o','q','x','Q','W','E','R','Y','U','I','O','P','A','F','G','H','K','L','X','V','B','N','M']

def rootinput():
    global r1,r2,r3,r4,r5,lrt,rootentry
    rootentry = entry.get()
    lrt=len(rootentry)
    if lrt==0:
        messagebox.showinfo('错误','请输入词根。')
    elif lrt>0 and lrt<3 or lrt>5:
        messagebox.showinfo('错误','根母必须是3~5个，请输入完整词根。')
    else:
        if ((rootentry[0] or rootentry[1] or rootentry[2])in illigal):
            messagebox.showinfo('错误','请输入正确词根。')
        else:
            r1=rootentry[0]
            r2=rootentry[1]
            r3=rootentry[2]
            if lrt==4:
                r4=rootentry[3]
            elif lrt==5:
                r4=rootentry[3]
                r5=rootentry[4]
################
'''选择变化模式'''
def conjtyp():
    typ=conjtypselect.get()
    if typ=='名词':
        conjtypselectadj.grid_forget()
        conjtypselectv.grid_forget()
        conjtypselectn.grid(row = 2, column = 1, sticky = tk.W)
        plcheck.grid(row = 2,column = 2)
        typn=conjtypselectn.get()
        if typn=='基本名词':
            conjed = basicnoun() if varnounpl.get()==0 else nounpl(basicnoun())
        elif typn=='地点名词':
            conjed = placenoun() if varnounpl.get()==0 else nounpl(placenoun())
        elif typn=='结果名词':
            conjed = finalnoun() if varnounpl.get()==0 else nounpl(finalnoun())
        elif typn=='程度名词':
            conjed = degnoun() if varnounpl.get()==0 else nounpl(degnoun())
        elif typn=='宏大名词':
            conjed = hugenoun() if varnounpl.get()==0 else nounpl(hugenoun())
        elif typn=='工具名词':
            conjed = instrnoun() if varnounpl.get()==0 else nounpl(instrnoun())
        elif typn=='工具地点名词':
            conjed = instrplacenoun() if varnounpl.get()==0 else nounpl(instrplacenoun())
        elif typn=='特征人名词':
            conjed = tratenoun() if varnounpl.get()==0 else nounpl(tratenoun())
        elif typn=='善者名词':
            conjed = gdfnoun() if varnounpl.get()==0 else nounpl(gdfnoun())
    elif(typ=='形容词'):
        conjtypselectn.grid_forget()
        conjtypselectv.grid_forget()
        conjtypselectadj.grid(row = 2, column = 1)
        plcheck.grid_forget()
        typadj=conjtypselectadj.get()
        if typadj=='最高级':
            conjed = superadj()
        elif typadj=='自动转义形容词':
            conjed = intransadj()
        elif typadj=='他动转义形容词':
            conjed = transadj()
        elif typadj=='易于...的':
            conjed = easyadj()
        elif typadj=='难于...的':
            conjed = dfcltadj()
        elif typadj=='令人...的':
            conjed = ingadj()
        elif typadj=='善于...的':
            conjed = gdfadj()
        elif typadj=='工具形容词':
            conjed = instradj()
    elif(typ=='动词'):
        conjtypselectadj.grid_forget()
        conjtypselectn.grid_forget()
        conjtypselectv.grid(row = 2, column = 1)
        plcheck.grid_forget()
        typv=conjtypselectv.get()
        if typv=='一般使役':
            conjed = causeverb()
        elif typv=='一般被动':
            conjed = passverb()
        elif typv=='一般使役被动':
            conjed = causepassverb()
        elif typv=='敬语使役':
            conjed = rspctcauseverb()
        elif typv=='敬语被动':
            conjed = rspctpassverb()
        elif typv=='敬语使役被动':
            conjed = rspctcausepassverb()
        elif typv=='能力形':
            conjed = ableverb()
        elif typv=='能力使役':
            conjed = ablecauseverb()
        elif typv=='能力被动':
            conjed = ablepassverb()
        elif typv=='能力使役被动':
            conjed = ablecausepassverb()
        elif typv=='能力形否定':
            conjed = nableverb()
        elif typv=='能力使役否定':
            conjed = nablecauseverb()
        elif typv=='能力被动否定':
            conjed = nablepassverb()
        elif typv=='能力使役被动否定':
            conjed = nablecausepassverb()
        elif typv=='中止体':
            conjed = middlestop()
        elif typv=='濒临体':
            conjed = verge()
        elif typv=='经历体':
            conjed = experi()
        elif typv=='自动变化':
            conjed = intransbcm()
        elif typv=='他动变化':
            conjed = transbcm()
    return conjed

def confirmin():
    rootinput()
    conjtyp()
    varconjoutputLabel.set(conjtyp())

def clear():
    entry.delete(0, END)

inputokbut = Button(rc, text = '变!', width=5, command = confirmin, relief = 'raised')
inputokbut.grid(row = 0, rowspan = 2, column = 2)

clearbut = Button(rc, text = '清除', width=5, command = clear, relief = 'raised')
clearbut.grid(row = 0, rowspan = 2, column = 4)


# result
txt2 = Label(rc, text = '屈折结果：')
txt2.grid(row = 3, column = 1)

varconjoutputLabel = tk.StringVar()
conjoutput = tk.Label(rc, textvariable = varconjoutputLabel, font = ('Arial',14))
conjoutput.grid(row = 4, column = 1)
################
'''元音音变'''
def midvphoch(r,m):
    if(((r==('y' or 'c' or 'j')) and (m==('i' or 'y'))) or ((r==('w' or 'f' or 'v')) and (m==('u' or 'w')))):
        m = 'a' #yi->ya wu->wa
    elif((r==('y' or 'i' or 'a')) and (m=='w')):
        m = 'u' #yw/iw->yu, aw->au
    elif((r==('w' or 'u' or 'a')) and (m=='y')):
        m = 'i' #wy/uy->wi, ay->ai
    else: m = m
    return m

'''辅音音变'''
def midcphoch(r):
        if r=='k': r='h'
        elif r=='g': r='a'
        elif r=='p': r='f'
        elif r=='b': r='v'
        elif r=='v': r='w'
        elif r=='c': r='T'
        elif r=='j': r='D'
        elif r=='t': r='C'
        elif r=='d': r='J'
        elif r=='C': r='T'
        elif r=='J': r='D'
        elif r=='s': r='S'
        elif r=='z': r='Z'
        elif r=='r': r='Z'
        elif r=='a': r='ah'
        elif r=='y': r='ih'
        elif r=='w': r='uh'
        else: r=r
        return r

def ra(r):
    rb= "'a" if r=='a' else r
    return rb

def r3a(r3):
    r3 = ra(r3)
    if r3=='y':
        r3 = "'i"
    elif r3=='w':
        r3 = "'u"
    else: r3 = r3
    return r3
################
'''名词'''
# 名词复数
def nounpl(sg):
    if sg[-1] == 'u' or sg[-1] == 'a' or sg[-1] == 'i':
        pn = sg + 'm'
    else:
        pn = sg + 'u'
    return pn

# 基本名词
def basicnoun():
    m1 = 'i'
    m2 = 'u'
    if lrt==3:
        r2m = ra(r2)
        r3m = r3a(r3)
        m1 = midvphoch(r1,m1)
        m2 = midvphoch(r2,m2)
        conjres = '%s%s%s%s%s'%(r1,m1,r2m,m2,r3m)
    elif lrt==4 or 5:
        if r2=='y':
            r2m = 'i'
        elif r2=='w':
            r2m = 'u'
            m1 = 'y'
        elif r2=='a':
            r2m = "'a" 
        else: r2m = r2
        m1 = midvphoch(r1,m1)
        m2 = midvphoch(r3,m2)
        if lrt==4: 
            r4m = r3a(r4)
            conjres = '%s%s%s%s%s%s'%(r1,m1,r2m,r3,m2,r4m)
        elif lrt==5:
            if r5=='w':r5m='u'
            elif r5=='y':r5m='i'
            else: r5m=r5
            conjres = '%s%s%s%s%s%sa%s'%(r1,m1,r2m,r3,m2,r4,r5m)
    return conjres

# 地点/结果名词
def cjn():
    m1 = 'i'
    m2 = 'u'
    if lrt==3:
        r2m = ra(r2)
        r3m = ra(r3)
        m1 = midvphoch(r1,m1)
        m2 = midvphoch(r2,m2)
        conjres = '%s%s%s%s%s'%(r1,m1,r2m,m2,r3m)
    elif lrt==4 or 5:
        if r2=='y':
            r2m = 'i'
        elif r2=='w':
            r2m = 'u'
            m1 = 'y'
        elif r2=='a':
            r2m = r2
            m1 = 'y' 
        else: r2m = r2
        r4m = ra(r4)
        m1 = midvphoch(r1,m1)
        m2 = midvphoch(r3,m2)
        if lrt==4:conjres = '%s%s%s%s%s%s'%(r1,m1,r2m,r3,m2,r4m)
        elif lrt==5:conjres = '%s%s%s%s%s%s%s'%(r1,m1,r2m,r3,m2,r4m,r5)
    return conjres

# 地点名词
def placenoun():
    conjres = cjn()
    if rootentry[-1]=='w':
        conjres = conjres+'aj'
    else:
        conjres = conjres+'uj'
    return conjres

# 结果名词
def finalnoun():
    conjres = cjn()+'ab'
    return conjres

# 工具名词
def instrnoun():
    m1 = 'u'
    m1 = midvphoch(r1,m1)
    if lrt==3:
        r2m = ra(r2)
        r3m = ra(r3)
        conjres = '%s%s%sa%siz'%(r1,m1,r2m,r3m)
    elif lrt==4:
        if r2=='y':
            r2m = 'i'
            m1 = 'w'
        elif r2=='w':
            r2m = 'u'
            m1 = 'w'
        elif r2=='a':
            r2m = r2
            m1 = 'w'
        else: r2m=r2
        r3m = ra(r3)
        r4m = ra(r4)
        conjres = '%s%s%s%sa%siz'%(r1,m1,r2m,r3m,r4m)
    elif lrt==5:
        if r2=='y':
            r2m = 'i'
            m1 = 'w'
        elif r2=='w':
            r2m = 'u'
            m1 = 'w'
        elif r2=='a':
            r2m = r2
            m1 = 'w'
        else: r2m=r2
        r3m = ra(r3)
        r5m = ra(r5)
        conjres = '%s%s%s%sa%s%siz'%(r1,m1,r2m,r3m,r4,r5m)
    
    return conjres

# 工具地点名词
def instrplacenoun():
    conjres = instrnoun()+'uj'
    return conjres

# 特征人名词
def tratenoun():
    global r1,r2,r3
    m1 = 'i'
    m2 = 'i'
    r1m = midvphoch(m1,r1)
    m2 = midvphoch(r2,m2)
    if r1=='a' or 'w':
        m1 = 'y'
    elif r1=='y':
        r1m = r1 if r2=='a' else 'i'
    r2m = "a'" if r2=='a' else r2
    if r3=='a' or 'y' or 'w':
        if m2 == 'i':
            r3m = midvphoch(m2,r3)
            if r3=='w' or 'a':
                m2m = 'y'
            elif r3=='y':
                m2m = "'i"
                r3m = 'i'
            else: r3m = r3
            conjres = '%s%s%s%s%s%s'%(m1,r1m,r2m,m2,m2m,r3m)
        else:
            r3m = ra(r3)
            conjres = "%s%s%s%s%s%s"%(m1,r1m,r2m,m2,m2,r3m)
            if r3=='w':
                conjres = "%s%s%s%s'%su"%(m1,r1m,r2m,m2,m2)
            elif r3=='y':
                conjres = "%s%s%s%s'%si"%(m1,r1m,r2m,m2,m2)
    else:
        conjres = '%s%s%s%s%s%s'%(m1,r1m,r2m,m2,m2,r3)
    if lrt==4:
        mm=midvphoch(r3,'i')
        if r4=='a':
            conjres = conjres+'y%s'%(r4)
        elif r4=='w':
            r4m='u'
            conjres = conjres+'y%s'%(r4m)
        elif r4=='y':
            r4m='i'
            conjres = conjres+'%s%s'%(mm,r4m)
        else: conjres = conjres+'%s%s'%(mm,r4)
    elif lrt==5:
        m1m='a' if r4=='y' else m1
        r5m='i' if r5=='y' else r5
        conjres = conjres+'%s%s%s'%(r4,m1m,r5m)
    return conjres

# 程度名词
def degnoun():
    conjres = cjn()+'inzib'
    return conjres

# 善者名词
def gdfnoun():
    if(gdadj()[0]==('a' or 'i' or 'u')):
        conjres = "asu'"+gdadj()
    else:
        conjres = 'asu'+gdadj()

    return conjres

# 宏大名词
def hugenoun():
    if r1=='w':r1m='u'
    elif r1=='y':r1m='i' 
    else: r1m=r1
    if r2=='h':
        r1m=midcphoch(r1)
        conjres = 'ma%saa%s'%(r1m,r3)
    else: conjres = 'ma%s%saa%s'%(r1m,r2,r3)
    if r2=='a':
        conjres = 'ma%saa%s'%(r1m,r3)
    if r1=='a' and r2=='a':
        conjres = "ma'aa%s"%(r3)
    if lrt==4:
        if r4=='w':r4m='u'
        elif r4=='y':r4m='i'
        else: r4m=r4
        conjres = conjres+'a%s'%(r4m)
    elif lrt==5:
        if r5=='w':r5m='u'
        elif r5=='y':r5m='i'
        else: r5m=r5
        conjres = conjres+'%sa%s'%(r4,r5m)
    return conjres

'''动词'''
# 一般使役
def causeverb():
    m1 = 'w'
    m2 = 'a'
    m1 = midvphoch(r1,m1)
    if r2=='a' or r2=='y' or r2=='w':
        conjres = '%s%s-%s%s-%s<>'%(r1,m1,r2,m2,r3)
    else:
        conjres = '%s%s-%s%s%s-%s<>'%(r1,m1,r2,r2,m2,r3)
    return conjres

# 一般被动
def passverb():
    m1 = 'a'
    m2 = 'y'
    m2 = midvphoch(r2,m2)
    if r2=='a' or r2=='y' or r2=='w':
        conjres = '%s%s-%s%s-%s<>'%(r1,m1,r2,m2,r3)
    else:
        conjres = '%s%s-%s%s%s-%s<>'%(r1,m1,r2,r2,m2,r3)
    return conjres

# 一般使役被动
def causepassverb():
    m1 = 'w'
    m2 = 'y'
    m1 = midvphoch(r1,m1)
    m2 = midvphoch(r2,m2)
    if r2=='a' or r2=='y' or r2=='w':
        conjres = '%s%s-%s%s-%s<>'%(r1,m1,r2,m2,r3)
    else:
        conjres = '%s%s-%s%s%s-%s<>'%(r1,m1,r2,r2,m2,r3)
    return conjres

# 敬语使役
def rspctcauseverb():
    m1 = 'w'
    m2 = 'a'
    m1 = midvphoch(r1,m1)
    conjres = 'tyu%s%s%s-%s%s-%s<>'%(r1,r1,m1,r2,m2,r3)
    return conjres

# 敬语被动
def rspctpassverb():
    m1 = 'a'
    m2 = 'y'
    m2 = midvphoch(r2,m2)
    if r2=='a' or r2=='y' or r2=='w':
        conjres = 'tii%s%s-%s%s-%s<>'%(r1,m1,r2,m2,r3)
    else:
        conjres = 'tii%s%s-%s%s%s-%s<>'%(r1,m1,r2,r2,m2,r3)
    return conjres

#敬语使役被动
def rspctcausepassverb():
    m1 = 'w'
    m2 = 'y'
    m1 = midvphoch(r1,m1)
    m2 = midvphoch(r2,m2)
    conjres = 'tyu%s%s%s-%s%s-%s<>'%(r1,r1,m1,r2,m2,r3)
    return conjres

# 自动/能力
def tr_able():
    r1m = midcphoch(r1)
    r2m = ra(r2)
    r3m = ra(r3)
    conjres = '%si%sra%s'%(r1m,r2m,r3m)
    return conjres

# 能力使役中间
def ablecausevm():
    r1m = ra(midcphoch(r1))
    r2m = ra(r2)
    r3m = ra(r3)
    conjres = '%sw-%sra-%s<>'%(r1m,r2m,r3m)
    return conjres

# 能力被动中间
def ablepassvm():
    r1m = ra(midcphoch(r1))
    r2m = ra(r2)
    r3m = ra(r3)
    conjres = '%sa-%sry-%s<>'%(r1m,r2m,r3m)
    return conjres

# 能力形
def ableverb():
    conjres = 'bin'+tr_able()+'<>'
    return conjres

# 能力使役
def ablecauseverb():
    if r1=='a' or r1=='y' or r1=='w':
        conjres = "binu'"+ablecausevm()
    else:
        conjres = 'binu'+ablecausevm()
    return conjres

# 能力被动
def ablepassverb():
    if r1=='a' or r1=='y' or r1=='w':
        conjres = "binu'"+ablepassvm()
    else:
        conjres = 'binu'+ablepassvm()
    return conjres

# 能力使役被动
def ablecausepassverb():
    r1m = ra(midcphoch(r1))
    r2m = ra(r2)
    r3m = ra(r3)
    if r1=='a' or r1=='y' or r1=='w':
        conjres = "binu'%su-%sry-%s<>"%(r1m,r2m,r3m)
    else:
        conjres = 'binu%sw-%sry-%s<>'%(r1m,r2m,r3m)
    return conjres

# 能力形否定
def nableverb():
    if r1=='a' or r1=='y' or r1=='w' or r1=='g':
        conjres = 'byu\''+tr_able()+'<>'
    else:
        conjres = 'byu'+tr_able()+'<>'
    return conjres

# 能力使役否定
def nablecauseverb():
    if r1=='a' or r1=='y' or r1=='w':
        conjres = "byu'"+ablecausevm()
    else:
        conjres = 'byu'+ablecausevm()
    return conjres

# 能力被动否定
def nablepassverb():
    if r1=='a' or r1=='y' or r1=='w':
        conjres = "byu'"+ablepassvm()
    else:
        conjres = 'byu'+ablepassvm()
    return conjres

# 能力使役被动否定
def nablecausepassverb():
    r1m = ra(midcphoch(r1))
    r2m = ra(r2)
    r3m = ra(r3)
    if r1=='a' or r1=='y' or r1=='w':
        conjres = "byu'%su-%sry-%s<>"%(r1m,r2m,r3m)
    else:
        conjres = 'byu%sw-%sry-%s<>'%(r1m,r2m,r3m)
    return conjres

# 中止
def middlestop():
    m2 = 'w'
    m2 = midvphoch(r2,m2)
    r1m = midcphoch(r1)
    r2m = ra(r2)
    r3m = ra(r3)
    conjres = "%s-%s%s-%s<>"%(r1m,r2m,m2,r3m)
    return conjres

# 濒临
def verge():
    r2m = midcphoch(r2)
    if r2=='a' or r2=='y' or r2=='w':
        conjres = "%sl-'%s-%s<>"%(r1,r2m,r3)
    else:
        conjres = "%sl-%s-%s<>"%(r1,r2m,r3)
    return conjres

# 经历
def experi():
    r1m = midcphoch(r1)
    r3m = ra(r3)
    conjres = '%s-%sl-%su'%(r1m,r2,r3m)
    return conjres

# 自动变化
def intransbcm():
    r1m = midcphoch(r1)
    conjres = '%s-%sr-%s<>'%(r1m,r2,r3)
    return conjres

# 他动变化
def transbcm():
    if r1=='y':
        r1m = 'i'
    elif r1=='w':
        r1m = 'u'
    else:
        r1m = r1
    r2m = midcphoch(r2)
    if r2=='a' or r2=='y' or r2=='w':
        conjres = "%slw-'%sa-%s<>"%(r1m,r2m,r3)
    else:
        conjres = "%slw-%sa-%s<>"%(r1m,r2m,r3)
    return conjres

'''形容词'''
# 最高级
def superadj():
    global r2
    m1 = 'i'
    m1 = midvphoch(r1,m1)
    r3m = r3a(r3)
    if r2=='y':
        conjres = 'al%s%si%sa'%(r1,m1,r3)
    elif r2=='w':
        if m1=='a':
            conjres = 'al%s%su%sa'%(r1,m1,r3m)
        else:
            conjres = 'al%s%syu%sa'%(r1,m1,r3m)
    elif r2=='a':
        if m1=='a':
            conjres = 'al%s%s%sa'%(r1,m1,r3m)
        else:
            conjres = 'al%s%sya%sa'%(r1,m1,r3m)
    else:
        conjres = 'al%s%s%s%s%sa'%(r1,m1,m1,r2,r3)
    return conjres

# 他动
def transadj():
    m1 = 'i'
    m1 = midvphoch(r1,m1)
    r3m = ra(r3)
    if r2=='a':
        if m1 == 'i':
            m1 = 'y'
        conjres = '%s%sa%sa'%(r1,m1,r3m)
    elif r2=='y':
        conjres = '%s%si%sa'%(r1,m1,r3m)
    elif r2=='w':
        if m1 == 'i':
            m1 = 'y'
        conjres = '%s%su%sa'%(r1,m1,r3m)
    else:
        conjres = '%s%s%s%sa'%(r1,m1,r2,r3)
    return conjres

# 自动
def intransadj():
    conjres = tr_able()+'a'
    return conjres

# 易于/难于
def e_dadj():
    r1m = midcphoch(r1)
    r2m = ra(r2)
    r3m = r3a(r3)
    if r2=='r':
        conjres = '%si%su%s'%(r1m,r2,r3m)
    else:
        conjres = '%si%sru%s'%(r1m,r2m,r3m)
    return conjres

# 善于
def gdadj():
    r1m = midcphoch(r1)    
    if lrt==3:
        r2m = midvphoch('i',r2)
        r3m = r3a(r3)
        if r2=='r':
            conjres = '%si%sau%s'%(r1m,r2,r3m)
        elif r2=='w':
            conjres = '%syurau%s'%(r1m,r3m)
        elif r2=='a':
            conjres = '%syarau%s'%(r1m,r3m)
        elif r2=='y':
            conjres = '%siirau%s'%(r1m,r3m)
        else:
            conjres = '%si%srau%s'%(r1m,r2m,r3m)
    elif lrt==4:
        r3m = midvphoch('i',r3)
        r4m = r3a(r4)
        if r3=='r':
            conjres = '%si%s%sau%s'%(r1m,r2,r3,r4m)
        elif r3=='w':
            conjres = '%si%surau%s'%(r1m,r2,r4m)
        elif r3=='a':
            conjres = '%sy%sarau%s'%(r1m,r2,r4m)
        elif r3=='y':
            conjres = '%si%sirau%s'%(r1m,r2,r4m)
        else:
            conjres = '%si%s%srau%s'%(r1m,r2,r3m,r4m)
    elif lrt==5:
        r3m = midvphoch('i',r3)
        r4m = r3a(r4)
        if r3=='r':
            conjres = '%si%s%sau%sa%s'%(r1m,r2,r3,r4m,r5)
        elif r3=='w':
            conjres = '%si%surau%sa%s'%(r1m,r2,r4m,r5)
        elif r3=='a':
            conjres = '%sy%sarau%sa%s'%(r1m,r2,r4m,r5)
        elif r3=='y':
            conjres = '%si%sirau%sa%s'%(r1m,r2,r4m,r5)
        else:
            conjres = '%si%s%srau%sa%s'%(r1m,r2,r3m,r4m,r5)
    return conjres

# 易于
def easyadj():
    conjres = e_dadj()+'ya'
    return conjres

# 难于
def dfcltadj():
    conjres = e_dadj()+'wa'
    return conjres

# 善于
def gdfadj():
    conjres=gdadj()+'a'
    return conjres

# 令人
def ingadj():
    m2 = 'i'
    r1m = midcphoch(r1)
    if lrt==3:
        m2 = midvphoch(r2,m2)
        r2m = ra(r2)
        r3m = ra(r3)
        conjres = "%sa%s%s%sa"%(r1m,r2m,m2,r3m)
    elif lrt==4:
        m2 = midvphoch(r3,m2)
        r2m = 'i' if r2=='y' else r2
        r3m = ra(r3)
        r4m = ra(r4)
        conjres = "%sa%s%s%s%sa"%(r1m,r2m,r3m,m2,r4m)
    elif lrt==5:
        m2 = midvphoch(r3,m2)
        r2m = 'i' if r2=='y' else r2
        r3m = ra(r3)
        r4m = ra(r4)
        conjres = "%sa%s%s%s%s%sa"%(r1m,r2m,r3m,m2,r4m,r5)
    return conjres

# 工具形容词
def instradj():
    conjres = instrnoun()+'a'
    return conjres

rc.mainloop()
