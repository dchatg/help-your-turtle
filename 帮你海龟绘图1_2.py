# -*- coding: utf-8 -*-
"""
Created on Sat May 21 15:16:12 2022

@author: dchatg
"""

import turtle as t
import tkinter as tk
from tkinter.ttk import Combobox

'''设置页面格式'''
fre = tk.Tk()
fre.title('turtle绘图')
fre.geometry('500x750')
tk_operate = []


'''定义按键所需函数'''
def t_start():#开始
    global tk_operate
    t.begin_fill()
    t.setheading(90)#初始需要旋转90度将箭头向上
    tk_operate.append('t.begin_fill()')
    tk_operate.append(f't.setheading({90})')
    
def t_end():#结束
    global tk_operate
    t.end_fill()
    tk_operate.append('t.end_fill()')
    
def undo():#撤销
    global tk_operate
    t.undo()
    try:
        tk_operate.pop()
    except IndexError:
        tk.messagebox.showinfo(title = '错误',message = '无法继续撤销')
def rest():#重置
    global tk_operate
    tk_operate = []
    t.reset()
    
def t_yes():#海龟箭头可见
    global tk_operate
    t.hideturtle()
    tk_operate.append('t.hideturtle()')

def t_no():#箭头不可见
    global tk_operate
    t.showturtle()
    tk_operate.append('t.showturtle()')
    
'''定义开始、结束、撤销、重置等操作按钮'''
s1 = tk.Button(fre,text ='开始',width = 5,height = 2,command = t_start)
s1.place(x = 10,y = 10)

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
    val1,val2 = t.position()
    val1,val2 = int(val1),int(val2)
    t.goto(val1,val2 + line_b)
    tk_operate.append(f't.goto({val1},{val2 + line_b})')
    
def t_down():#下
    global tk_operate
    val1,val2 = t.position()
    val1,val2 = int(val1),int(val2)
    t.goto(val1,val2 - line_b)
    tk_operate.append(f't.goto({val1},{val2 - line_b})')
    
def t_right():#左
    global tk_operate
    val1,val2 = t.position()
    val1,val2 = int(val1),int(val2)
    t.goto(val1 - line_b,val2)
    tk_operate.append(f't.goto({val1 - line_b},{val2})')
    
def t_left():#右
    global tk_operate
    val1,val2 = t.position()
    val1,val2 = int(val1),int(val2)
    t.goto(val1 + line_b,val2)
    tk_operate.append(f't.goto({val1 + line_b},{val2})')

b1 = tk.Button(fre,text = '上',width = 5,height = 2,command = t_up)
b1.place(x = 160,y = 10)

b2 = tk.Button(fre,text = '下',width = 5,height = 2,command = t_down)
b2.place(x=160,y=110)

b3 = tk.Button(fre,text = '左',width = 5,height = 2,command = t_right)
b3.place(x = 110,y = 60)

b4 = tk.Button(fre,text = '右',width = 5,height = 2,command = t_left)
b4.place(x = 210,y = 60)

'''直行、左右转、画笔抬起、落下'''
eg = tk.Entry(fre,width = 9)#设置直行
eg.place(x = 140,y = 180)

e_turn = tk.Entry(fre,width=5)#设置转向
e_turn.place(x = 163,y = 250)

def t_go():#直行指定距离
    global tk_operate
    var = eg.get()
    try:
        var = int(var)
    except ValueError:
        tk.messagebox.showinfo(title = '错误',message = '错误输入')
    else:
        t.forward(var)
        tk_operate.append(f't.forward({var})')
        
def turn_right():#左转指定角度
    global tk_operate
    var = e_turn.get()
    try:
        var = int(var)
    except ValueError:
        tk.messagebox.showinfo(title = '错误',message = '错误输入')
    else:
        t.right(var)
        tk_operate.append(f't.right({var})')
        
def turn_left():#右转指定角度
    global tk_operate
    var = e_turn.get()
    try:
        var = int(var)
    except ValueError:
        tk.messagebox.showinfo(title  = '错误',message = '错误输入')
    else:
        t.left(var)
        tk_operate.append(f't.left({var})')
        
def t_penup():#抬起
    global tk_operate
    t.penup()
    tk_operate.append('t.penup()')
    
def t_pendown():#落下
    global tk_operate
    t.pendown()
    tk_operate.append('t.pendown()')
    
b5 = tk.Button(fre,text = '直行',width = 5,height = 2,command = t_go)
b5.place(x = 210,y = 170)

b6 = tk.Button(fre,text = '左转',width = 5,height = 2,command = turn_left)
b6.place(x = 110,y = 235)

b7 = tk.Button(fre,text = '右转',width = 5,height = 2,command = turn_right)
b7.place(x = 210,y = 235)

b8 = tk.Button(fre,text = '抬起',width = 5,height = 2,command = t_penup)
b8.place(x = 110,y = 10)

b9 = tk.Button(fre,text = '落下',width = 5,height = 2,command = t_pendown)
b9.place(x = 210,y = 10)

'''设置画笔移动到指定位置'''
go_x = tk.Entry(fre,width = 6)#x
go_x.place(x = 130,y = 310)
go_y = tk.Entry(fre,width = 6)#y
go_y.place(x = 210,y = 310)

def to_go():#移动到指定位置
    x,y = go_x.get(),go_y.get()
    try:
        x,y = int(x),int()
    except ValueError:
        tk.messagebox.showinfo(title = '错误',message = 'x,y位置错误输入')
    else:
        t.penup()
        t.goto(x,y)
        t.pendown()
        tk_operate.append('t.penup()')
        tk_operate.append(f't.goto({x},{y})')
        tk_operate.append('t.pendown()')
        
b_go = tk.Button(fre,text = '移动到指定位置',width = 14,height = 2,command = to_go)
b_go.place(x = 140,y = 335)

#设置提示
b_gox = tk.Label(fre,text = 'x',width = 2,height = 1)
b_gox.place(x = 105,y = 305)

b_goy = tk.Label(fre,text = 'y',width = 2,height = 1)
b_goy.place(x = 185,y = 305)

'''设置海龟绘图线条和填充'''
e1 = tk.Entry(fre,width = 5)#设置线条宽度
e1.place(x = 330,y = 25)

e_b = tk.Entry(fre,width = 5)#设置线条步长
e_b.place(x = 330,y = 85)

e2 = tk.Entry(fre)#设置线条颜色
e2.place(x = 330,y = 130)

e3 = tk.Entry(fre)#设置填充
e3.place(x = 330,y = 220)

def k_d():#turtle线条宽度
    global tk_operate
    var = e1.get()
    try:
        var = int(var)
    except ValueError:
        tk.messagebox.showinfo(title ='错误',message = '线条宽度错误输入')
    else:
        t.pensize(var)
        tk_operate.append(f't.pensize({var})')
        
line_b = 5#默认步长
def b_c():#设置线条步长
    global tk_operate
    global line_b
    var = e_b.get()
    try:
        var = int(var)
    except ValueError:
        tk.messagebox.showinfo(title = '错误',message = '线条步长错误输入')
    else:
        line_b = var

def y_s():#turtle线条颜色
    global tk_operate
    var = e2.get()
    try:
        t.pencolor(var)
    except t.TurtleGraphicsError:
        tk.messagebox.showinfo(title = '错误',message = '线条颜色错误输入')
    else:
        tk_operate.append(f"t.pencolor('{var}')")

def t_s():#turtle填充颜色
    global tk_operate
    var = e3.get()
    try:
        t.fillcolor(var)
    except t.TurtleGraphicsError:
        tk.messagebox.showinfo(title = '错误',message = '填充颜色错误输入')
    else:
        tk_operate.append(f"t.fillcolor('{var}')")

x1 = tk.Button(fre,text = '设置线条宽度',width = 11,height = 2,command = k_d)
x1.place(x = 380,y = 15)

x_b = tk.Button(fre,text = '设置线条步长',width = 11,height = 2,command = b_c)
x_b.place(x = 380,y = 75)

x2 = tk.Button(fre,text = '设置线条颜色',width = 11,height = 2,command = y_s)
x2.place(x = 355,y = 155)

x3 = tk.Button(fre,text = '设置填充颜色',width = 11,height = 2,command = t_s)
x3.place(x = 355,y = 245)

'''设置颜色RGB输入'''

#RGB线条颜色设置
r_entry1 = tk.Entry(fre,width = 4)
r_entry1.place(x = 330,y = 310)

g_entry1 = tk.Entry(fre,width = 4)
g_entry1.place(x = 380,y = 310)

b_entry1 = tk.Entry(fre,width = 4)
b_entry1.place(x = 430,y = 310)

def rgb_l():#线条设置函数
    global tk_operate
    t.colormode(255)
    R,G,B = r_entry1.get(),g_entry1.get(),b_entry1.get()
    try:
        R,G,B = int(R),int(G),int(B)
    except ValueError:
        tk.messagebox.showinfo(title = '错误',message = '线条颜色错误输入')
    else:
        try:
            t.pencolor(R,G,B)
        except t.TurtleGraphicsError:
            tk.messagebox.showinfo(title = '错误',message = '数值不在0~255范围内')
        else:
            tk_operate.append('t.colormode(255)')
            tk_operate.append(f't.pencolor({R},{G},{B})')
#定义按钮
rgb_button1 = tk.Button(fre,text = '设置线条颜色RGB值',
                      width = 16,height = 2,command = rgb_l)

rgb_button1.place(x = 335,y = 340)

#RGB填充颜色设置
def rgb_t():#线条
    global tk_operate
    t.colormode(255)
    R,G,B = r_entry2.get(), g_entry2.get(), b_entry2.get()
    try:
        R,G,B = int(R),int(G),int(B)
    except ValueError:
        tk.messagebox.showinfo(title = '错误',message = '填充颜色错误输入')
    else:
        try:
            t.fillcolor(R,G,B)
        except t.TurtleGraphicsError:
            tk.messagebox.showinfo(title = '错误',message = '数值不在0~255范围内')
        else:
            tk_operate.append('t.colormode(255)')
            tk_operate.append(f't.fillcolor({R},{G},{B})')
            
r_entry2 = tk.Entry(fre,width = 4)
r_entry2.place(x = 330,y = 410)

g_entry2 = tk.Entry(fre,width = 4)
g_entry2.place(x = 380,y = 410)

b_entry2 = tk.Entry(fre,width = 4)
b_entry2.place(x = 430,y = 410)

rgb_button2 = tk.Button(fre,text = '设置填充颜色RGB值',
                      width = 16,height = 2,command = rgb_t)

rgb_button2.place(x = 335,y = 440)

#线条颜色/填充颜色帮助
turtle_color=['FFB6C1 LightPink 浅粉红', '#FFC0CB Pink 粉红', '#DC143C Crimson 深红/猩红', '#FFF0F5 LavenderBlush 淡紫红', 
 '#DB7093 PaleVioletRed 弱紫罗兰红', '#FF69B4 HotPink 热情的粉红', '#FF1493 DeepPink 深粉红', 
 '#C71585 MediumVioletRed 中紫罗兰红', '#DA70D6 Orchid 暗紫色/兰花紫', '#D8BFD8 Thistle 蓟色', 
 '#DDA0DD Plum 洋李色/李子紫', '#EE82EE Violet 紫罗兰', '#FF00FF Magenta 洋红/玫瑰红', 
 '#FF00FF Fuchsia 紫红/灯笼海棠', '#8B008B DarkMagenta 深洋红', '#800080 Purple 紫色', '#BA55D3 MediumOrchid 中兰花紫', 
 '#9400D3 DarkViolet 暗紫罗兰', '#9932CC DarkOrchid 暗兰花紫', '#4B0082 Indigo 靛青/紫兰色', '#8A2BE2 BlueViolet 蓝紫罗兰', 
 '#9370DB MediumPurple 中紫色', '#7B68EE MediumSlateBlue 中暗蓝色/中板岩蓝', '#6A5ACD SlateBlue 石蓝色/板岩蓝', 
 '#483D8B DarkSlateBlue 暗灰蓝色/暗板岩蓝', '#E6E6FA Lavender 淡紫色/熏衣草淡紫', '#F8F8FF GhostWhite 幽灵白', 
 '#0000FF Blue 纯蓝', '#0000CD MediumBlue 中蓝色', '#191970 MidnightBlue 午夜蓝', '#00008B DarkBlue 暗蓝色', 
 '#000080 Navy 海军蓝', '#4169E1 RoyalBlue 皇家蓝/宝蓝', '#6495ED CornflowerBlue 矢车菊蓝', 
 '#B0C4DE LightSteelBlue 亮钢蓝', '#778899 LightSlateGray 亮蓝灰/亮石板灰', '#708090 SlateGray 灰石色/石板灰', 
 '#1E90FF DodgerBlue 闪兰色/道奇蓝', '#F0F8FF AliceBlue 爱丽丝蓝', '#4682B4 SteelBlue 钢蓝/铁青', 
 '#87CEFA LightSkyBlue 亮天蓝色', '#87CEEB SkyBlue 天蓝色', '#00BFFF DeepSkyBlue 深天蓝', '#ADD8E6 LightBlue 亮蓝', 
 '#B0E0E6 PowderBlue 粉蓝色/火药青', '#5F9EA0 CadetBlue 军兰色/军服蓝', '#F0FFFF Azure 蔚蓝色', '#E0FFFF LightCyan 淡青色', 
 '#AFEEEE PaleTurquoise 弱绿宝石', '#00FFFF Cyan 青色', '#00FFFF Aqua 浅绿色/水色', '#00CED1 DarkTurquoise 暗绿宝石', 
 '#2F4F4F DarkSlateGray 暗瓦灰色/暗石板灰', '#008B8B DarkCyan 暗青色', '#008080 Teal 水鸭色', '#48D1CC MediumTurquoise 中绿宝石', 
 '#20B2AA LightSeaGreen 浅海洋绿', '#40E0D0 Turquoise 绿宝石', '#7FFFD4 Aquamarine 宝石碧绿', '#66CDAA MediumAquamarine 中宝石碧绿', 
 '#00FA9A MediumSpringGreen 中春绿色', '#F5FFFA MintCream 薄荷奶油', '#00FF7F SpringGreen 春绿色', 
 '#3CB371 MediumSeaGreen 中海洋绿', '#2E8B57 SeaGreen 海洋绿', '#F0FFF0 Honeydew 蜜色/蜜瓜色', '#90EE90 LightGreen 淡绿色', 
 '#98FB98 PaleGreen 弱绿色', '#8FBC8F DarkSeaGreen 暗海洋绿', '#32CD32 LimeGreen 闪光深绿', '#00FF00 Lime 闪光绿', 
 '#228B22 ForestGreen 森林绿', '#008000 Green 纯绿', '#006400 DarkGreen 暗绿色', '#7FFF00 Chartreuse 黄绿色/查特酒绿', 
 '#7CFC00 LawnGreen 草绿色/草坪绿', '#ADFF2F GreenYellow 绿黄色', '#556B2F DarkOliveGreen 暗橄榄绿', '#9ACD32 YellowGreen 黄绿色', 
 '#6B8E23 OliveDrab 橄榄褐色', '#F5F5DC Beige 米色/灰棕色', '#FAFAD2 LightGoldenrodYellow 亮菊黄', '#FFFFF0 Ivory 象牙色', 
 '#FFFFE0 LightYellow 浅黄色', '#FFFF00 Yellow 纯黄', '#808000 Olive 橄榄', '#BDB76B DarkKhaki 暗黄褐色/深卡叽布', 
 '#FFFACD LemonChiffon 柠檬绸', '#EEE8AA PaleGoldenrod 灰菊黄/苍麒麟色', '#F0E68C Khaki 黄褐色/卡叽布', 
 '#FFD700 Gold 金色', '#FFF8DC Cornsilk 玉米丝色', '#DAA520 Goldenrod 金菊黄', '#B8860B DarkGoldenrod 暗金菊黄', 
 '#FFFAF0 FloralWhite 花的白色', '#FDF5E6 OldLace 老花色/旧蕾丝', '#F5DEB3 Wheat 浅黄色/小麦色', 
 '#FFE4B5 Moccasin 鹿皮色/鹿皮靴', '#FFA500 Orange 橙色', '#FFEFD5 PapayaWhip 番木色/番木瓜', '#FFEBCD BlanchedAlmond 白杏色',
 '#FFDEAD NavajoWhite 纳瓦白/土著白', '#FAEBD7 AntiqueWhite 古董白', '#D2B48C Tan 茶色', '#DEB887 BurlyWood 硬木色', 
 '#FFE4C4 Bisque 陶坯黄', '#FF8C00 DarkOrange 深橙色', '#FAF0E6 Linen 亚麻布', '#CD853F Peru 秘鲁色', 
 '#FFDAB9 PeachPuff 桃肉色', '#F4A460 SandyBrown 沙棕色', '#D2691E Chocolate 巧克力色', '#8B4513 SaddleBrown 重褐色/马鞍棕色', 
 '#FFF5EE Seashell 海贝壳', '#A0522D Sienna 黄土赭色', '#FFA07A LightSalmon 浅鲑鱼肉色', '#FF7F50 Coral 珊瑚', 
 '#FF4500 OrangeRed 橙红色', '#E9967A DarkSalmon 深鲜肉/鲑鱼色', '#FF6347 Tomato 番茄红', '#FFE4E1 MistyRose 浅玫瑰色/薄雾玫瑰', 
 '#FA8072 Salmon 鲜肉/鲑鱼色', '#FFFAFA Snow 雪白色', '#F08080 LightCoral 淡珊瑚色', '#BC8F8F RosyBrown 玫瑰棕色', 
 '#CD5C5C IndianRed 印度红', '#FF0000 Red 纯红', '#A52A2A Brown 棕色', '#B22222 FireBrick 火砖色/耐火砖', 
 '#8B0000 DarkRed 深红色', '#800000 Maroon 栗色', '#FFFFFF White 纯白', '#F5F5F5 WhiteSmoke 白烟', '#DCDCDC Gainsboro 淡灰色', 
 '#D3D3D3 LightGrey 浅灰色', '#C0C0C0 Silver 银灰色', '#A9A9A9 DarkGray 深灰色', '#808080 Gray 灰色', '#696969 DimGray 暗淡灰', 
 '#000000 Black 纯黑']

def colorhelp():#这个函数会新开一个页面用于显示颜色字符串
    global turtle_color
    name_list = turtle_color
    color = tk.Tk()
    color.title('颜色帮助')
    color.geometry('330x400')
    
    color_s = tk.Scrollbar(color)
    color_s.pack(side = 'right',fill = 'y')

    color_list = tk.Listbox(color,width = 40,height = 60,yscrollcommand = color_s.set)
    for i in name_list:
        color_list.insert('end', i)
    color_list.pack(side = 'left',fill = 'both')
    color_s.config(command = color_list.yview)
    
    color.mainloop()

color_help = tk.Button(fre,
                       text = '填充颜色帮助',
                       width = 12,height = 2,
                       command = colorhelp)
color_help.place(x = 380,y = 530)

'''画圆与多边形'''
#指定半径画圆 or 半圆
y_entry1 = tk.Entry(fre,width = 8)
y_entry1.place(x = 110,y = 405)
y_entry2 = tk.Entry(fre,width = 8)
y_entry2.place(x = 110,y = 435)

#提示用按钮
roundx = tk.Label(fre,text = '半径:',width = 4,height = 1)
roundx.place(x = 70,y = 405)
roundy = tk.Label(fre,text = '角度:',width = 4,height = 1)
roundy.place(x = 70,y = 435)


def r_round():#用于绘制圆和圆弧
    global tk_operate
    var1 = y_entry1.get()
    var2 = y_entry2.get()
    try:
        var1 = float(var1)
    except ValueError:
        tk.messagebox.showinfo(title = '错误',message = '半径输入错误')
    else:
        if var2 != '':
            try:
                var2 = float(var2)
            except ValueError:
                tk.messagebox.showinfo(title = '错误',message = '角度输入错误')
            else:
                t.circle(var1,extent = var2)
                tk_operate.append(f't.circle({var1},extent = {var2})')
        else:
            t.circle(var1)
            tk_operate.append(f't.circle({var1})')
            
b_round = tk.Button(fre,text = '画圆/弧',width = 6,height = 2,command = r_round)
b_round.place(x = 180,y = 407)

#指定圆心画圆
y_entry3x = tk.Entry(fre,width = 5)#x输入
y_entry3x.place(x = 85,y = 490)
y_entry3y = tk.Entry(fre,width = 5)#y输入
y_entry3y.place(x = 155,y = 490)
y_entry3l = tk.Entry(fre,width = 5)#半径输入
y_entry3l.place(x = 240,y = 490)

def xy_round():#用于到指定位置绘制圆
    global tk_operate
    x,y = y_entry3x.get(),y_entry3y.get()
    var1 = y_entry3l.get()
    try:
        x,y = float(x),float(y)
        var1 = float(var1)
    except ValueError:
        tk.messagebox.showinfo(title = '错误',message = '位置或半径输入错误')
    else:
        t.penup()
        t.setheading(90)
        t.goto(x+var1,y)
        t.pendown()
        t.circle(var1)
        tk_operate.append('t.penup()')
        tk_operate.append('t.setheading(90)')
        tk_operate.append(f't.goto({x+var1},{y})')
        tk_operate.append('t.pendown()')
        tk_operate.append(f't.circle({var1})')
        
#button_round_x_y
b_rxy = tk.Button(fre,text = '指定位置画圆',
                width = 15,height = 2,
                command = xy_round)
b_rxy.place(x = 115,y = 520)

#提示用label
bx = tk.Label(fre,text = 'x',width = 2,height = 1)
bx.place(x = 60,y = 488)
by = tk.Label(fre,text = 'y',width = 2,height = 1)
by.place(x = 130,y = 488)
btext = tk.Label(fre,text = '半径',width = 4,height = 1)
btext.place(x = 200,y = 490)

'''文字写入功能'''
#用户文字输入框
world_write = tk.Entry(fre,width = 35)
world_write.place(x = 40,y = 620)

#字号设置
size_write = tk.Entry(fre,width = 5)
size_write.place(x = 80,y = 590)
sizewrite_b = tk.Label(fre,text = '字号',width = 4,height = 1)
sizewrite_b.place(x = 40,y = 590)
#字体设置
fontname_text = tk.StringVar()
font=['Arial','Helvetica','Lucida Family','Verdana','Tahoma','微软雅黑','华文细黑']
font_c = Combobox(fre,textvariable = fontname_text,width = 13,values = font,state = 'readonly')
font_c.current(1)
font_c.place(x = 160,y = 590)

fontname_L = tk.Label(fre,text = '字体',width = 4,height = 1)
fontname_L.place(x = 120,y = 590)

#左中右设置按钮
r_or_l = tk.StringVar()
r_or_l.set('center')
ro1 = tk.Radiobutton(fre,text = '左',variable = r_or_l,value = 'left')
ro1.place(x = 40,y = 640)
ro2 = tk.Radiobutton(fre,text = '中',variable = r_or_l,value = 'center')
ro2.place(x = 40,y = 660)
ro3 = tk.Radiobutton(fre,text = '右',variable = r_or_l,value = 'right')
ro3.place(x = 40,y = 680)

#字体绘制按钮

def text_write():
    global tk_operate
    arg = world_write.get()#写入的文字
    align = r_or_l.get()#写入的位置
    fontname = fontname_text.get()#写入的字体
    try:
        fontsize = int(size_write.get())#写入的字号
    except ValueError:
        tk.messagebox.showinfo(title = '错误',message = '字号输入错误')
    else:
        t.write(arg, False, align, font=(fontname, fontsize, 'normal'))
        tk_operate.append(f"t.write('{arg}', False, '{align}', font=('{fontname}', {fontsize}, 'normal'))")

text_b = tk.Button(fre,text = '写入',width = 6, height = 2 ,command = text_write)
text_b.place(x = 230,y = 650)


'''设置导出具体操作'''
def tk_export():
    global tk_operate
    with open('海龟绘图操作导出.txt','w') as tul:#创建导出文件
        tul.write('import turtle as t\n')
        for i in tk_operate:
            tul.write(i)
            tul.write('\n')
        tul.write('t.exitonclick()')
    #导出完成提示
    tk.messagebox.showinfo(title = '完成',message = "操作数据导出完成\n名为: 海龟绘图操作导出.txt \n位于同一文件中")
#文件导出按钮       
export = tk.Button(fre,text = '导出操作文件',width = 11,height = 2,command = tk_export)
export.place(x = 385,y = 640)


if __name__ == "__main__":
    fre.mainloop()
    t.exitonclick()
