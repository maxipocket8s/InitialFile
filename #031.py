import sys
sys.path.append("..\\..\\OneDrive\\바탕 화면\\Download_Data_Sample\\deep-learning-from-scratch-2-master")
import numpy as np
from common.optimizer import SGD
from common.trainer import Trainer
from dataset import spiral
import matplotlib.pyplot as plt
from ch01.two_layer_net import TwoLayerNet

max_epoch = 300
batch_size = 30
hidden_size = 10
learning_rate = 1.0

x, t = spiral.load_data()
model = TwoLayerNet(input_size = 2, hidden_size=hidden_size, output_size = 3)
optimizer = SGD(lr=learning_rate)
data_size = len(x)
max_iters = data_size // batch_size
total_loss = 0
loss_count = 0
loss_list = []

for epoch in range(max_epoch):
    idx = np.random.permutation(data_size)
    x = x[idx]
    t = t[idx]
    for iters in range(max_iters):
        batch_x = x[iters*batch_size:(iters+1)*batch_size]
        batch_t = t[iters*batch_size:(iters+1)*batch_size]
        loss = model.forward(batch_x, batch_t)
        model.backward()
        optimizer.update(model.params, model.grads)
        total_loss += loss
        loss_count += 1
        if (iters+1) % 10 == 0:
            avg_loss = total_loss / loss_count
            print("| 에폭 %d | 반복 %d / %d | 손실 %.2f" %(epoch+1, iters+1, max_iters, avg_loss))
            loss_list.append(avg_loss)
            total_loss, loss_count = 0, 0
# trainer = Trainer(model, optimizer)
# trainer.fit(x, t, max_epoch, batch_size, eval_interval=10)
# trainer.plot()

x = np.arange(len(loss_list))
plt.plot(x, loss_list, label='train')
plt.xlabel('반복 (x' + str(max_iters) + ')')
plt.ylabel('손실')
plt.show()