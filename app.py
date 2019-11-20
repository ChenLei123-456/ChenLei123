from  reportlab.graphics.shapes import Drawing, String, colors
from reportlab.graphics import renderPDF
from reportlab.pdfbase.ttfonts import *

'''--- 添加中文支持 ---'''
pdfmetrics.registerFont(TTFont('mysh', 'C:\WINDOWS\FONTS\ARIAL.TTF'))  # 注册要使用的字体
pdfmetrics.registerFont(TTFont('g', 'C:\WINDOWS\FONTS\ARIAL.TTF'))

'''--- 创建画布 ---'''
d = Drawing(300, 200)  # 创建画布并设置画布尺寸

'''--- 创建文本内容并设置样式与位置 ---'''
s1 = String(150, 100, '这一行使用字体的字体是微软雅黑！')  # 创建字符串并设置坐标、内容
s1.fontName = 'mysh'  # 设置字体
s1.fontSize = 14 # 设置字号
s1.fillColor = colors.red  # 设置字体颜色
s1.textAnchor = 'middle'  # 设置锚点为中心（即位置坐标为文本中心点坐标）

s2 = String(150, 120, '陈磊你是最帅的！', fontName='g', fontSize=100, fillColor=colors.yellow, textAnchor='middle')
# 另一种设置方式

'''--- 添加内容到画布并生成PDF文件 ---'''
d.add(s1)  # 将字符串添加到画布
d.add(s2)

renderPDF.drawToFile(d, 'myPDF.pdf', '我的第一个PDF文件。')  # 生成PDF文件并设置文件名称与文档描述
