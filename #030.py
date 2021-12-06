import numpy as np
import sys
sys.path.append('C:\\Users\\pjw20\\OneDrive\\바탕 화면\\Download_Data_Sample\\deep-learning-from-scratch-2-master')
from common.util import convert_one_hot
from common.layers import SoftmaxWithLoss
from common.trainer import Trainer
from common.optimizer import Adam

class MatMul:
    def __init__(self, W):
        self.params = [W]
        self.grads = [np.zeros_like(W)]
        self.x = None

    def forward(self, x):
        W, = self.params
        out = np.dot(x, W)
        self.x = x
        return out

    def backward(self, dout):
        W, = self.params
        dx = np.dot(dout, W.T)
        dW = np.dot(self.x.T, dout)
        self.grads[0][...] = dW
        return dx

def preprocess(text):
    text = text.lower()
    text = text.replace('.', ' .')
    # print(text)
    words = text.split(' ')
    # print(words)
    word_to_id = {}
    id_to_word = {}
    for word in words:
        if word not in word_to_id:
            new_id = len(word_to_id)
            word_to_id[word] = new_id
            id_to_word[new_id] = word
    # print('word_to_id: ', word_to_id)
    # print('id_to_word: ', id_to_word)
    corpus = np.array([word_to_id[w] for w in words])
    # print('corpus: ', corpus)
    return corpus, word_to_id, id_to_word

def create_co_matrix(corpus, vocab_size, window_size=1):
    corpus_size = len(corpus)
    co_matrix = np.zeros((vocab_size, vocab_size), dtype=np.int32)
    for idx, word_id in enumerate(corpus):
        left_idx = idx - 1
        right_idx = idx + 1
        if left_idx >= 0:
            left_word_id = corpus[left_idx]
            co_matrix[word_id, left_word_id] += 1
        if right_idx < corpus_size:
            right_word_id = corpus[right_idx]
            co_matrix[word_id, right_word_id] += 1
    return co_matrix

def create_contexts_target(corpus, window_size=1):
    target = corpus[window_size:-window_size]
    contexts = []
    for idx in range(window_size, len(corpus)-window_size):
        cs = []
        for t in range(-window_size, window_size+1):
            if t == 0:
                continue
            cs.append(corpus[idx+t])
        contexts.append(cs)
    return np.array(contexts), np.array(target)


text = 'You say goodbye and i say hello.'
corpus, word_to_id, id_to_word = preprocess(text)
contexts, target = create_contexts_target(corpus)


you_vec = np.array([[1, 0, 0, 0, 0, 0, 0]])
goodbye_vec = np.array([[0, 0, 1, 0, 0, 0, 0]])
W_in = np.random.randn(7, 3)
W_out = np.random.randn(3, 7)
in_layer_you = MatMul(W_in)
in_layer_goodbye = MatMul(W_in)
out_layer = MatMul(W_out)
h_you = in_layer_you.forward(you_vec)
h_goodbye = in_layer_goodbye.forward(goodbye_vec)
h = 0.5 * (h_you + h_goodbye)
s = out_layer.forward(h)
print(s)

vocab_size = len(word_to_id)
contexts = convert_one_hot(contexts, vocab_size)
target = convert_one_hot(target, vocab_size)

print('contexts: ', contexts)
print('target: ', target)

class SimpleCBOW:
    def __init__(self, vocab_size, hidden_size):
        V, H = vocab_size, hidden_size
        W_in = 0.01 * np.random.randn(V, H).astype('f')
        W_out = 0.01 * np.random.randn(H, V).astype('f')
        self.in_layerLeft = MatMul(W_in)
        self.in_layerRight = MatMul(W_in)
        self.out_layer = MatMul(W_out)
        self.loss_layer = SoftmaxWithLoss()
        layers = [self.in_layerLeft, self.in_layerRight, self.out_layer]
        self.params, self.grads = [], []
        for layer in layers:
            self.params += layer.params
            self.grads += layer.grads
        self.word_vecs = W_in
    def forward(self, contexts, target):
        hLeft = self.in_layerLeft.forward(contexts[:, 0])
        hRight = self.in_layerRight.forward(contexts[:, 1])
        h = 0.5 * (hLeft + hRight)
        score = self.out_layer.forward(h)
        loss = self.loss_layer.forward(score, target)
        return loss
    def backward(self, dout = 1):
        ds = self.loss_layer.backward(dout)
        da = self.out_layer.backward(ds)
        da *= 0.5
        self.in_layerLeft.backward(da)
        self.in_layerRight.backward(da)
        return None

print('contexts[:, 0]\n', contexts[:, 0])
print('contexts[:, 1]\n', contexts[:, 1])

window_size = 1
hidden_size = 5
batch_size = 3
max_epoch = 1000

text = 'You say goodbye and I say hello.'
corpus, word_to_id, id_to_word = preprocess(text)
vocab_size = len(word_to_id)
contexts, target = create_contexts_target(corpus, window_size)
contexts = convert_one_hot(contexts, vocab_size)
target = convert_one_hot(target, vocab_size)

model = SimpleCBOW(vocab_size, hidden_size)
optimizer = Adam()
trainer = Trainer(model, optimizer)

trainer.fit(contexts, target, max_epoch, batch_size)
trainer.plot()
word_vecs = model.word_vecs
for word_id, word in id_to_word.items():
    print(word, word_vecs[word_id])