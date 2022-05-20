# help-your-turtle
用python库帮你海龟绘图 turtle   
使用了python的tkinter 和 turtle   
只有单独一个文件，可以放到任何你想放到文件夹双击运行即可(需要你的计算机安装了python)。

![capture_20220520203302295](https://user-images.githubusercontent.com/99422473/169529092-00968933-8919-4110-8e4f-6fa6c62efae0.jpeg)

具体使用方法：   
  
由于turtle填充形状时需要在开始绘制前设置好线条颜色与填充形状  

所以第一步是设置好线条颜色与填充颜色，为colorstring 指定的 Tk 颜色描述字符串 如'red','yellow','blue','black'等--------这两个默认为黑色 black

然后设置所需的线条步长，因为线条步长决定了每次对'上下左右'操作时的位移量--------这个默认值为 5

最后设置你的线条宽度就是turtle中的penisze()--------默认值为turtle的默认值 1
  
然后就可以点击'开始'，这个button指向了begin_fill()   
   
每次绘制结束后请点击'结束'，这和button 指向 end_fill()   
  
  




可以导出你的具体操作，名为 “海龟绘图操作导出.txt”。
复制进Pycharm、Spyder中可直接运行
   
支持画笔抬起penup()、落下pendown()  
  
支持对海龟的可见性控制，showturtle()、hideturtle()  
  
支持左转右转指定角度，right(),left()  
  
支持设置线条宽度,pensize()  
  
支持设置线条颜色，字符串和RGB皆可 pencolor()、fillcolor()  
  
支持移动到指定位置（x,y）移动过程中不会留下画迹  
  
支持画圆，画弧，circle(value),circle(value,extent)
  
支持到指定位置画圆
  
  
  
后续代办  
  
1、加入文字功能 wirte()  
  
2、加入多边形绘制功能 cricle(x,steps)  
  
3、优化页面显示
  


感谢 莫烦python 录制的tkinter教程
