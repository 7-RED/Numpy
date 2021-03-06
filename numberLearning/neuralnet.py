import numpy as np

def make_params(shape_list):
    w_list=[]
    b_list=[]
    for i in range(len(shape_list)-1):
        weight=np.random.randn(shape_list[i],shape_list[i+1])
        bias=np.ones(shape_list[i+1])/10.0
        w_list.append(weight)
        b_list.append(bias)
        
    return w_list,b_list

def sigmoid(x):
    return 1/(1+np.exp(-x))

def inner_product(x_train,w,b):
    return np.dot(x_train,w)+b

def activation(x_train,w,b):
    return sigmoid(inner_product(x_train, w, b))

def calculate(x_train,w_list,b_list):
    val_dict={}
    u_1=inner_product(x_train, w_list[0], b_list[0])
    y_1=sigmoid(u_1)
    
    u_2=inner_product(y_1, w_list[1], b_list[1])
    y_2=sigmoid(u_2)
    
    val_dict['y_1']=y_1
    val_dict['y_2']=y_2
    
    return val_dict

def update(x_train,w_list,b_list,y_train,eta):
    val_dict={}
    val_dict=calculate(x_train, w_list, b_list)
    y_1=val_dict['y_1']
    y_2=val_dict['y_2']
    
    d12_d11=1.0
    d11_d9=(1/x_train.shape[0])*(y_2-y_train)
    d9_d8=y_2*(1.0-y_2)
    d8_d7=1.0
    #d8_d6=np.transpose(y_1)
    #d8_d5=np.transpose(w_list[1])
    d8_d6=y_1.T
    d8_d5=w_list[1].T
    d5_d4=y_1*(1.0-y_1)
    d4_d3=1.0
    #d4_d2=np.transpose(x_train)
    d4_d2=x_train.T

    d12_d8=d12_d11*d11_d9*d9_d8
    b_list[1]-=eta*np.sum(d12_d8*d8_d7,axis=0)
    w_list[1]-=eta*np.dot(d8_d6,d12_d8)
    
    d12_d8=d12_d11*d11_d9*d9_d8
    d12_d5=np.dot(d12_d8,d8_d5)
    d12_d4=d12_d5*d5_d4
    b_list[0]-=eta*np.sum(d12_d4*d4_d3,axis=0)
    w_list[0]-=eta*np.dot(d4_d2,d12_d4)
        
    return w_list,b_list