# bibliotēkas tkinter pysimpleS

from tkinter import *

mansLogs=Tk()
mansLogs.title("Kalkulatoriņš")
mansLogs.geometry("300x300")
#ir jāpaliek attēls logam - ico



#jādefinē pogas
e=Entry(mansLogs, width=30, font=("Arial"))

btn1=Button(mansLogs, text='1', padx='30', pady='20')
btn2=Button(mansLogs, text='2', padx='30', pady='20')
btn3=Button(mansLogs, text='3', padx='30', pady='20')

btn4=Button(mansLogs, text='4', padx='30', pady='20')
btn5=Button(mansLogs, text='5', padx='30', pady='20')
btn6=Button(mansLogs, text='6', padx='30', pady='20')

btn7=Button(mansLogs, text='7', padx='30', pady='20')
btn8=Button(mansLogs, text='8', padx='30', pady='20')
btn9=Button(mansLogs, text='9', padx='30', pady='20')

btn0=Button(mansLogs, text='0', padx='30', pady='20')
plus=Button(mansLogs, text='+', padx='30', pady='20')
minus=Button(mansLogs, text='-', padx='30', pady='20')

rezultats=Button(mansLogs, text='=', padx='20', pady='120')

logs=Entry(mansLogs, text='0')

#katra poga jānoliek logā

logs.grid(row=0, columnspan=4)

rezultats.grid(rowspan=4, column=4)

btn1.grid(row=3, column=0)
btn2.grid(row=3, column=1)
btn3.grid(row=3, column=2)

btn4.grid(row=2, column=0)
btn5.grid(row=2, column=1)
btn6.grid(row=2, column=2)

btn7.grid(row=1, column=0)
btn8.grid(row=1, column=1)
btn9.grid(row=1, column=2)

btn0.grid(row=4, column=0)
plus.grid(row=4, column=1)
minus.grid(row=4, column=2)


mansLogs.mainloop()