import matplotlib.pyplot as plt

#绘制简单的折线图
x_squares = [1, 2, 3, 4, 5]
y_squares = [1, 4, 9, 16, 25]
x = [1,2,3,4,5]
y = [1,8,27,64,125]

#
plt.plot(x_squares, y_squares, linewidth=2)
plt.plot(x, y, linewidth=2)
# 设置标题，x轴标签，y轴标签
plt.title('shaohua_title', fontsize=18)
plt.xlabel('shaohua_xlabel', fontsize=10)
plt.ylabel('shaohua_ylabel', fontsize=10)
# 设置刻度标记大小axis='both,x,y'
plt.tick_params(axis='both', labelsize=10)
plt.show()
