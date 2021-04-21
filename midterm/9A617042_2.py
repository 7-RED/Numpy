import numpy as np
import matplotlib.pyplot as plt 
std_schno='9A617042'

w_im=([0,0,0],[0,0,0])
j = 0
k = 0
for i in range(2,8,1):
    if i==5:
        j += 1
        k = 0
    w_im[j][k]=float(std_schno[i])
    k += 1
    if std_schno[i]==0:
        w_im[j][k]=0.55

arr=np.array([6,1,7,0,4,2])
arr_new=arr[0:7]/10
arr_new[3]=0.55


x_0 = np.arange(-1.0, 1.0, 0.2) 
x_1 = np.arange(-1.0, 1.0, 0.2) 
Z = np.zeros(100)
w_im = arr_new.reshape(2,3)
w_mo = np.array([[0.4],
                 [0.5],
                 [-0.3]])
b_im = np.array([0.6,0.3,-0.4]) 
b_mo = np.array([0.2])
def middle_layer(x, w, b): 
    u = np.dot(x, w) + b 
    return 1/(1+np.exp(-u))
def output_layer(x, w, b): 
    u = np.dot(x, w) + b 
    return u
for i in range(10): 
    for j in range(10):
        inp = np.array([x_0[i], x_1[j]])
        mid = middle_layer(inp, w_im, b_im) 
        out = output_layer(mid, w_mo, b_mo) 
        Z[i*10+j] = out[0]
plt.imshow(Z.reshape(10,10), "gray", vmin = 0.0, vmax = 1.0) 
plt.colorbar()
plt.show()



