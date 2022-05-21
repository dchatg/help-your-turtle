# -*- coding: utf-8 -*-
"""
Created on Thu May 19 18:55:47 2022

@author: dchatg
"""

import turtle as t
import tkinter as tk

'''设置页面格式'''
fre=tk.Tk()
fre.title('turtle绘图')
fre.geometry('500x600')
tk_operate=[]


'''定义按键所需函数'''
def t_start():#开始
    global tk_operate
    t.begin_fill()
    t.setheading(90)#初始需要旋转90度将箭头向上
    tk_operate.append('t.begin_fill()\n')
    tk_operate.append(f't.setheading({90})\n')
def t_end():#结束
    global tk_operate
    t.end_fill()
    tk_operate.append('t.end_fill()\n')
    
def undo():#撤销
    global tk_operate
    t.undo()
    try:
        tk_operate.pop()
    except IndexError:
        tk.messagebox.showinfo(title='错误',message='无法继续撤销')
def rest():#重置
    global tk_operate
    tk_operate=[]
    t.reset()
    
def t_yes():#海龟箭头可见
    global tk_operate
    t.hideturtle()
    tk_operate.append('t.hideturtle()\n')

def t_no():#箭头不可见
    global tk_operate
    t.showturtle()
    tk_operate.append('t.showturtle()\n')
'''定义开始、结束、撤销、重置等操作按钮'''
s1 = tk.Button(fre,text='开始',width = 5,height = 2,command = t_start)
s1.place(x=10,y=10)

s2 = tk.Button(fre,text = '结束',width = 5,height = 2,command = t_end)
s2.place(x = 10,y = 60)

s3 = tk.Button(fre,text = '撤销',width = 5,height = 2,command = undo)
s3.place(x = 10,y = 110)

s4 = tk.Button(fre,text = '重置',width = 5,height = 2,command = rest)
s4.place(x = 10,y = 200)

s5 = tk.Button(fre,text = '海龟可见',width = 9,height = 2,command = t_no)
s5.place(x = 10,y = 280)

s6 = tk.Button(fre,text = '海龟不可见',width = 9,height = 2,command = t_yes)
s6.place(x = 10,y = 330) 

'''定义(上下左右)四个按键及指向的操作'''
def t_up():#上
    global tk_operate
    val1,val2=t.position()
    val1,val2=int(val1),int(val2)
    t.goto(val1,val2+line_b)
    tk_operate.append(f't.goto({val1},{val2+line_b})\n')
def t_down():#下
    global tk_operate
    val1,val2=t.position()
    val1,val2=int(val1),int(val2)
    t.goto(val1,val2-line_b)
    tk_operate.append(f't.goto({val1},{val2-line_b})\n')
def t_right():#左
    global tk_operate
    val1,val2=t.position()
    val1,val2=int(val1),int(val2)
    t.goto(val1-line_b,val2)
    tk_operate.append(f't.goto({val1-line_b},{val2})\n')
def t_left():#右
    global tk_operate
    val1,val2=t.position()
    val1,val2=int(val1),int(val2)
    t.goto(val1+line_b,val2)
    tk_operate.append(f't.goto({val1+line_b},{val2})\n')

b1=tk.Button(fre,text='上',width=5,height=2,command=t_up)
b1.place(x=160,y=10)

b2=tk.Button(fre,text='下',width=5,height=2,command=t_down)
b2.place(x=160,y=110)

b3=tk.Button(fre,text='左',width=5,height=2,command=t_right)
b3.place(x=110,y=60)

b4=tk.Button(fre,text='右',width=5,height=2,command=t_left)
b4.place(x=210,y=60)

'''直行、左右转、画笔抬起、落下'''
eg=tk.Entry(fre,width=9)#设置直行
eg.place(x=140,y=180)

e_turn=tk.Entry(fre,width=5)#设置转向
e_turn.place(x=163,y=250)

def t_go():#直行指定距离
    global tk_operate
    var=eg.get()
    try:
        var=int(var)
    except ValueError:
        tk.messagebox.showinfo(title='错误',message='错误输入')
    else:
        t.forward(var)
        tk_operate.append(f't.forward({var})\n')
        
def turn_right():#左转指定角度
    global tk_operate
    var=e_turn.get()
    try:
        var=int(var)
    except ValueError:
        tk.messagebox.showinfo(title='错误',message='错误输入')
    else:
        t.right(var)
        tk_operate.append(f't.right({var})\n')
        
def turn_left():#右转指定角度
    global tk_operate
    var=e_turn.get()
    try:
        var=int(var)
    except ValueError:
        tk.messagebox.showinfo(title='错误',message='错误输入')
    else:
        t.left(var)
        tk_operate.append(f't.left({var})\n')
        
def t_penup():#抬起
    global tk_operate
    t.penup()
    tk_operate.append('t.penup()\n')
    
def t_pendown():#落下
    global tk_operate
    t.pendown()
    tk_operate.append('t.pendown()\n')
    
b5=tk.Button(fre,text='直行',width=5,height=2,command=t_go)
b5.place(x=210,y=170)

b6=tk.Button(fre,text='左转',width=5,height=2,command=turn_left)
b6.place(x=110,y=235)

b7=tk.Button(fre,text='右转',width=5,height=2,command=turn_right)
b7.place(x=210,y=235)

b8=tk.Button(fre,text='抬起',width=5,height=2,command=t_penup)
b8.place(x=110,y=10)

b9=tk.Button(fre,text='落下',width=5,height=2,command=t_pendown)
b9.place(x=210,y=10)

'''设置画笔移动到指定位置'''
go_x=tk.Entry(fre,width=6)#x
go_x.place(x=130,y=310)
go_y=tk.Entry(fre,width=6)#y
go_y.place(x=210,y=310)

def to_go():#移动到指定位置
    x,y=go_x.get(),go_y.get()
    try:
        x,y=int(x),int()
    except ValueError:
        tk.messagebox.showinfo(title='错误',message='x,y位置错误输入')
    else:
        t.penup()
        t.goto(x,y)
        t.pendown()
        tk_operate.append('t.penup()\n')
        tk_operate.append(f't.goto({x},{y})\n')
        tk_operate.append('t.pendown()')
        
b_go=tk.Button(fre,text='移动到指定位置',width=14,height=2,command=to_go)
b_go.place(x=140,y=335)
#设置提示按钮
b_gox=tk.Button(fre,text='x',width=2,height=1)
b_gox.place(x=105,y=305)
b_goy=tk.Button(fre,text='y',width=2,height=1)
b_goy.place(x=185,y=305)
'''设置海龟绘图线条和填充'''
e1=tk.Entry(fre,width=5)#设置线条宽度
e1.place(x=330,y=25)

e_b=tk.Entry(fre,width=5)#设置线条步长
e_b.place(x=330,y=85)

e2=tk.Entry(fre)#设置线条颜色
e2.place(x=330,y=130)

e3=tk.Entry(fre)#设置填充
e3.place(x=330,y=220)

def k_d():#turtle线条宽度
    global tk_operate
    var=e1.get()
    try:
        var=int(var)
    except ValueError:
        tk.messagebox.showinfo(title='错误',message='线条宽度错误输入')
    else:
        t.pensize(var)
        tk_operate.append(f't.pensize({var})\n')
        
        
line_b = 5#默认步长
def b_c():#设置线条步长
    global tk_operate
    global line_b
    var=e_b.get()
    try:
        var=int(var)
    except ValueError:
        tk.messagebox.showinfo(title='错误',message='线条步长错误输入')
    else:
        line_b=var

        
def y_s():#turtle线条颜色
    global tk_operate
    var=e2.get()
    try:
        t.pencolor(var)
    except t.TurtleGraphicsError:
        tk.messagebox.showinfo(title='错误',message='线条颜色错误输入')
    else:
        tk_operate.append(f"t.pencolor('{var}')\n")

def t_s():#turtle填充颜色
    global tk_operate
    var=e3.get()
    try:
        t.fillcolor(var)
    except t.TurtleGraphicsError:
        tk.messagebox.showinfo(title='错误',message='填充颜色错误输入')
    else:
        tk_operate.append(f"t.fillcolor('{var}')\n")

x1=tk.Button(fre,text='设置线条宽度',width=11,height=2,command=k_d)
x1.place(x=380,y=15)

x_b=tk.Button(fre,text='设置线条步长',width=11,height=2,command=b_c)
x_b.place(x=380,y=65)

x2=tk.Button(fre,text='设置线条颜色',width=11,height=2,command=y_s)
x2.place(x=355,y=155)

x3=tk.Button(fre,text='设置填充颜色',width=11,height=2,command=t_s)
x3.place(x=355,y=240)

'''设置颜色RGB输入'''

#RGB线条颜色设置
r_entry1=tk.Entry(fre,width=4)
r_entry1.place(x=330,y=310)

g_entry1=tk.Entry(fre,width=4)
g_entry1.place(x=380,y=310)

b_entry1=tk.Entry(fre,width=4)
b_entry1.place(x=430,y=310)

def rgb_l():#线条设置函数
    global tk_operate
    t.colormode(255)
    R,G,B=r_entry1.get(),g_entry1.get(),b_entry1.get()
    try:
        R,G,B=int(R),int(G),int(B)
    except ValueError:
        tk.messagebox.showinfo(title='错误',message='线条颜色错误输入')
    else:
        try:
            t.pencolor(R,G,B)
        except t.TurtleGraphicsError:
            tk.messagebox.showinfo(title='错误',message='数值不在0~255范围内')
        else:
            tk_operate.append('t.colormode(255)\n')
            tk_operate.append(f't.pencolor({R},{G},{B})\n')
#定义按钮
rgb_button1=tk.Button(fre,text='设置线条颜色RGB值',
                      width=16,height=2,command=rgb_l)

rgb_button1.place(x=335,y=340)

#RGB填充颜色设置
def rgb_t():#线条
    global tk_operate
    t.colormode(255)
    R,G,B=r_entry2.get(), g_entry2.get(), b_entry2.get()
    try:
        R,G,B=int(R),int(G),int(B)
    except ValueError:
        tk.messagebox.showinfo(title='错误',message='填充颜色错误输入')
    else:
        try:
            t.fillcolor(R,G,B)
        except t.TurtleGraphicsError:
            tk.messagebox.showinfo(title='错误',message='数值不在0~255范围内')
        else:
            tk_operate.append('t.colormode(255)\n')
            tk_operate.append(f't.fillcolor({R},{G},{B})\n')
            
r_entry2=tk.Entry(fre,width=4)
r_entry2.place(x=330,y=410)

g_entry2=tk.Entry(fre,width=4)
g_entry2.place(x=380,y=410)

b_entry2=tk.Entry(fre,width=4)
b_entry2.place(x=430,y=410)

rgb_button2=tk.Button(fre,text='设置填充颜色RGB值',
                      width=16,height=2,command=rgb_t)

rgb_button2.place(x=335,y=440)

'''画圆与多边形'''
#指定半径画圆 or 半圆
y_entry1=tk.Entry(fre,width=8)
y_entry1.place(x=110,y=405)
y_entry2=tk.Entry(fre,width=8)
y_entry2.place(x=110,y=435)

#提示用按钮
roundx=tk.Button(fre,text='半径',width=4,height=1)
roundx.place(x=60,y=400)
roundy=tk.Button(fre,text='角度',width=4,height=1)
roundy.place(x=60,y=430)


def r_round():#用于绘制圆和圆弧
    global tk_operate
    var1=y_entry1.get()
    var2=y_entry2.get()
    try:
        var1=float(var1)
    except ValueError:
        tk.messagebox.showinfo(title='错误',message='半径输入错误')
    else:
        if var2 != '':
            try:
                var2=float(var2)
            except ValueError:
                tk.messagebox.showinfo(title='错误',message='角度输入错误')
            else:
                t.circle(var1,extent=var2)
                tk_operate.append(f't.circle({var1},extent={var2})\n')
        else:
            t.circle(var1)
            tk_operate.append(f't.circle({var1})\n')
            
b_round=tk.Button(fre,text='画圆',width=6,height=2,command=r_round)
b_round.place(x=180,y=407)

#指定圆心画圆
y_entry3x=tk.Entry(fre,width=5)#x输入
y_entry3x.place(x=85,y=490)
y_entry3y=tk.Entry(fre,width=5)#y输入
y_entry3y.place(x=155,y=490)
y_entry3l=tk.Entry(fre,width=5)#半径输入
y_entry3l.place(x=240,y=490)

def xy_round():#用于到指定位置绘制圆
    global tk_operate
    x,y=y_entry3x.get(),y_entry3y.get()
    var1=y_entry3l.get()
    try:
        x,y=float(x),float(y)
        var1=float(var1)
    except ValueError:
        tk.messagebox.showinfo(title='错误',message='位置或半径输入错误')
    else:
        t.penup()
        t.setheading(90)
        t.goto(x+var1,y)
        t.pendown()
        t.circle(var1)
        tk_operate.append('t.penup()\n')
        tk_operate.append('t.setheading(90)\n')
        tk_operate.append(f't.circle({var1})\n')
        tk_operate.append('t.pendown()')
        tk_operate.append(f't.circle({var1})\n')
        
#round_x_y
b_rxy=tk.Button(fre,text='指定位置画圆',
                width=15,height=2,
                command=xy_round)
b_rxy.place(x=115,y=520)

#提示用按钮
bx=tk.Button(fre,text='x',width=2,height=1)
bx.place(x=60,y=485)
by=tk.Button(fre,text='y',width=2,height=1)
by.place(x=130,y=485)
btext=tk.Button(fre,text='半径',width=4,height=1)
btext.place(x=200,y=485)

'''设置导出具体操作'''
def tk_export():
    global tk_operate
    with open('海龟绘图操作导出.txt','w') as tul:#创建导出文件
        tul.write('import turtle as t\n')
        for i in tk_operate:
            tul.write(i)
        tul.write('t.exitonclick()')
            
export=tk.Button(fre,text='导出操作文件',width=11,height=2,command=tk_export)
export.place(x=400,y=540)


if __name__ == "__main__":
    fre.mainloop()
    t.exitonclick()




















