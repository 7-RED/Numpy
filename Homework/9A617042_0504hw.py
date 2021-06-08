import numpy as np
#輸入
x_0 = np.arange(-1.0, 1.0, 0.1) 
x_1 = np.arange(-1.0, 1.0, 0.1) 
Z=np.zeros((400,2))

#權重
w_im = np.array([[1.0,2.0],
[2.0,3.0]])
w_mo = np.array([[-1.0,1.0],
[1.0,-1.0]])
w_mo_2 = np.array([[-1.0,1.0],
[1.0,-1.0]])

#偏差
b_im = np.array([0.3,-0.3]) 
b_mo = np.array([0.4, 0.1])
b_mo_2 = np.array([0.4, 0.1])

#定義函數皆為sigmoid
def middle_layer(x, w, b): 
    u = np.dot(x, w) + b 
    return 1/(1+np.exp(-u))
def output_layer(x, w, b):
    u = np.dot(x, w) + b
    return 1/(1+np.exp(-u))
def output_layer_2(x, w, b):
    u = np.dot(x, w) + b
    return np.exp(u)/np.sum(np.exp(u))

#run
for i in range(20):
    for j in range(20):
        inp = np.array([x_0[i], x_1[j]])
        mid = middle_layer(inp, w_im, b_im) 
        out = output_layer(mid, w_mo, b_mo) 
        out_2 = output_layer_2(out, w_mo_2, b_mo_2)
        Z[i*20 + j] = out_2
print(Z)

#畫圖用
plus_x = [] 
plus_y = [] 
circle_x = [] 
circle_y = []
for i in range(20): 
    for j in range(20):
        if Z[i*20 +j][0] > Z[i*20 +j][1]: 
            plus_x.append(x_0[i]) 
            plus_y.append(x_1[j])
        else: 
            circle_x.append(x_0[i]) 
            circle_y.append(x_1[j])
import matplotlib.pyplot as plt 
plt.scatter(plus_x, plus_y, marker="+") 
plt.scatter(circle_x, circle_y, marker="o") 
plt.show()
