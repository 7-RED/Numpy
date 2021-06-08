import numpy as np
import neuralnet as nl
import load_mnist as lm
#import matplotlib.pyplot as plt
dataset=lm.load_mnist()
#print(dataset['x_train'][0])
x_train=dataset['x_train']
y_train=dataset['y_train']
x_test=dataset['x_test']
y_test=dataset['y_test']
#print(x_test)
w_list,b_list=nl.make_params([784,100,10])
eta=2.0
for epoch in range(10):
    ra=np.random.randint(60000,size=60000)
    for i in range(60):
        x_batch=x_train[ra[i*1000:(i+1)*1000],:]
        y_batch=y_train[ra[i*1000:(i+1)*1000],:]
        w_list,b_list=nl.update(x_batch,w_list,b_list,y_batch,eta)

val_dict=nl.calculate(x_test,w_list,b_list)
print(val_dict['y_2'][0:10].round(2))
print(y_test[0:10])

#plt.imshow(dataset['x_test'][8].reshape(28,28),cmap="gray")