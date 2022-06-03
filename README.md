# help-your-turtle
用python库帮你海龟绘图 turtle   
使用了python的tkinter 和 turtle   
一共两个文件  
帮你海龟绘图1_2.py  
海龟绘图支持颜色.txt   
这两个文件需放在同一文件夹,双击运行即可(需要你的计算机安装了python)。
![主页面](https://user-images.githubusercontent.com/99422473/171906875-dad817d5-76af-473e-894c-3cc425710367.jpeg)
  
--
具体使用方法：   
-- 
由于turtle填充形状时需要在开始绘制前设置线条颜色与填充形状  

所以第一步是设置好线条颜色与填充颜色，为colorstring 指定的 Tk 颜色描述字符串 如'red','yellow','blue','black'等--------这两个默认为黑色 black，写了try except，所以填入错误的字符串会提示
  
![capture_20220520203302295](https://user-images.githubusercontent.com/99422473/169559854-4e1b4dd8-b217-471e-84e2-6d8833b7bc88.jpeg)

然后设置所需的线条步长，因为线条步长决定了每次对'上下左右'操作时的位移量--------这个默认值为 5

最后设置你的线条宽度就是turtle中的penisze()--------默认值为turtle的默认值 1  
![capture_20220520203302296](https://user-images.githubusercontent.com/99422473/169560676-5dbf499b-dd14-48a2-84aa-d68f3750d198.jpeg)
  
 
然后就可以点击'开始'，这个button指向了begin_fill()   
![capture_20220520203302297](https://user-images.githubusercontent.com/99422473/169562313-1916074b-4d36-4176-9378-183162e50fd8.jpeg)  
每次绘制结束后请点击'结束'，这个button 指向 end_fill()   
'撤销'会撤销你的上一个操作，指向undo()

'重置'会删除所有绘图并恢复所有默认值，指向reset()  

导出操作文件可以导出你的具体操作，位于与下载的文件同一个文件夹，名为 “海龟绘图操作导出.txt”。  

另存为.py文件可直接运行,也可以选择复制进Pycharm、Spyder、Jupyter Notebook  

--
文字写入
--  
2022/6/4增加了对文字的写入，需要在绘图中设置字号，填入文字，选择写入位置，点击“写入”  
示例:  
![测试用例](https://user-images.githubusercontent.com/99422473/171907351-6f76c249-3c02-4629-9de7-e052fdc6f5de.jpeg)

-- 
操作导出
--
复制进py文件中可直接运行  
示例:  
![导出txt](https://user-images.githubusercontent.com/99422473/171907772-0edda284-45a5-4045-b212-44fa7832d643.jpeg)

--  
--  
--
支持操作
--
支持画笔抬起penup()、落下pendown()  
  
支持对海龟的可见性控制，showturtle()、hideturtle()  
  
支持左转右转角度，right(),left()  
  
支持设置线条宽度,pensize()  
  
支持设置线条颜色，字符串和RGB皆可 pencolor()、fillcolor()  
  
支持移动到指定位置（x,y),移动过程中不会留下画迹  
  
支持画圆，画弧，circle(value),circle(value,extent)  

支持写入文字，可指定文字字号、字体、写入位置  
  
支持到指定位置画圆，指定的位置为圆心

支持对画笔线条颜色、填充颜色以RGB设置
  
--
后续待办 
--

1、加入文字功能 write() (√) 已完成 
  
2、加入多边形绘制功能 cricle(x,steps)  
  
3、优化页面显示
  


--
非常感谢 莫烦python 大佬录制的tkinter教程 http://mofanpy.com
--
