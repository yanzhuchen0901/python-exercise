# Name: Xing Ziyi
# ID: 202010701580011
# Date:  2021/9/11
print("My name's \"Sam\" \\ and I am 20 years old\n")
print("{0:<15}{1:>5}{2:>10}".format("Welcome", "to", "Python\n"))
apple = 1.69234
orange = 2.1612561
print("{0:<12}{1:>12}".format("Apple", "Orange"))
print("{0:<12.2f}{1:>12.4f}".format(apple, orange))

'''
这个地方，普及一下花括号中的语法结构：
{0:<12.2f}：0表示第一个参数，<表示左对齐，12表示占12个字符宽度，.2f表示保留两位小数的浮点数。
{1:>12.4f}：1表示第二个参数，>表示右对齐，12表示占12个字符宽度，.4f表示保留四位小数的浮点数。
利用好相关的语法，就能使输出有列表一样的效果
'''