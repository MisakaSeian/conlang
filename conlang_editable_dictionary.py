import tkinter as tk
from tkinter import *
from tkinter import filedialog
import tkinter.messagebox as mbox
import xlrd
################
'''窗口'''
MainBox = tk.Tk()
MainBox.title('Conlang Editable Dictionary')
MainBox.geometry("1000x675+300+100")
# 打开词典文档
def upload_action(event = None):
    global Wordlist
    global root
    global LangVar
    listName = filedialog.askopenfilename(title='请选择一个文件', filetypes=[('Excel', '.xls')])
    Wordlist = xlrd.open_workbook(listName)
    if(Wordlist):
        mainlabelshow.set('Opened dict file %s'%listName)
    
# language switch buttons
LangList = ["English", "Chinese", "French", "Celthoneg", "Gwenedeg"]
LangVar = tk.IntVar()
LangVar.set(0)
for l in LangList:
    tk.Radiobutton(MainBox, value = LangList.index(l), variable = LangVar, text = l, width = 8).grid(row = 0, column = LangList.index(l))


def clean_search():
    WordEntry.delete(0,END)

def word_out():
    follows = ''
    if word_search() != '':
        wordtitleshow.set(outarray[3])
        outs = "Etymology:\r\n%s\r\nPart of speech & Plural: %s"% (outarray[5],outarray[6])
        mainlabelshow.set(outs)
        for i in (range(0,9) if len(followwords) > 10 else range(0,len(followwords))):
            follows += "%s\r\n"% followwords[i]
        wordfollowshow.set(follows)
    else:
        wordtitleshow.set('')
        mainlabelshow.set('')
        wordfollowshow.set('')
        mbox.showerror('ATTENTION','No such word in this dictionary.\r\nPlease check your input.')

def word_search():
    global outarray, followwords
    #if(nofileflag == 0):
    #    mbox.showerror('ATTENTION','No dictionary file opened.\r\nPlease open a dictionary file.')
    lexiquesheet = Wordlist.sheets()[0] #表格
    sumrow = lexiquesheet.nrows #总行(词条)数
    searchenword = WordEntry.get() #被搜索单词
    langcol = LangVar.get() #第几列(什么语言)
    for i in range(1,sumrow):
        if(fuzzysch.get()):
            if searchenword in lexiquesheet.col_values(langcol)[i]:
                outarray = lexiquesheet.row_values(i)
                followwords = lexiquesheet.col_values(langcol)[i:(10 if (sumrow - i)>10 else sumrow)]
                return searchenword
        else:
            if lexiquesheet.col_values(langcol)[i] == searchenword:
                outarray = lexiquesheet.row_values(i)
                followwords = lexiquesheet.col_values(langcol)[i:(10 if (sumrow - i)>10 else sumrow)]
                return searchenword
    return ''
       
#########################################

WordEntry = tk.Entry(MainBox, width = 16)
WordEntry.grid(row = 1, column = 0, sticky = tk.W, columnspan = 2, padx = 6)

DictOpenButton = tk.Button(MainBox, text = 'OPEN DICT FILE', command = lambda: upload_action())
DictOpenButton.grid(row = 0, column=5, padx = 470, sticky = tk.E)

SearchButton = tk.Button(MainBox, text = '🔍', command = lambda: word_out(), width = 3, relief = 'raised')
SearchButton.grid(row = 1, column = 1, padx = 2, sticky= tk.E)

CleanButton = tk.Button(MainBox, text = 'clear', command = lambda: clean_search(), width = 5, relief = 'raised')
CleanButton.grid(row = 1, column = 2, sticky= tk.W)

fuzzysch = IntVar()
FuzzyButton = Checkbutton(MainBox, text = 'fuzzy search', variable = fuzzysch, width = 9).grid(row = 2, column = 0)

wordtitleshow = tk.StringVar()
WordTitle = tk.Label(MainBox, textvariable = wordtitleshow, fg = "#FFF", bg="#048", font=('黑体', 18), width=64, height=1, anchor='center', justify='center')
WordTitle.place(x=220, y=32)

mainlabelshow = tk.StringVar()
MainLabel = tk.Label(MainBox, textvariable = mainlabelshow, bg="#CCC", font=('Arial', 10), width=96, height=36, anchor='nw', justify='left')
MainLabel.place(x=220, y=75)

wordfollowshow = tk.StringVar()
WordFollowLabel = tk.Label(MainBox, textvariable = wordfollowshow, bg="#888", font=('Arial', 10), width=23, height=36, anchor='nw', justify='left')
WordFollowLabel.place(x=12, y=85)


MainBox.bind("<Return>", lambda event: SearchButton.invoke())
MainBox.mainloop()