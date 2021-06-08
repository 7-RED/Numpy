import load_mnist as lm
import matplotlib.pyplot as plt
dataset=lm.load_mnist()
#print(dataset['x_train'][0])
x_train=dataset['x_train']
y_train=dataset['y_train']
x_test=dataset['x_test']
y_test=dataset['y_test']
#print(x_test)
#plt.imshow(dataset['x_test'][1].reshape(28,28),cmap="gray")
for i in range(9):
    plt.imshow(dataset['x_test'][i].reshape(28,28),cmap="gray")
    plt.show()