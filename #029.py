import numpy as np
import sys
sys.path.append("..\\..\\OneDrive\\바탕 화면\\Download_Data_Sample\\deep-learning-from-scratch-2-master")
# from common.util import preprocess

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

text = 'You say goodbye and I say hello.'
corpus, word_to_id, id_to_word = preprocess(text)

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

def cos_similarity(x, y, eps=1e-8):
    nx = x / (np.sqrt(np.sum(x**2))+eps)
    ny = y / (np.sqrt(np.sum(y**2))+eps)
    # print('nx: ', nx)
    # print('ny: ', ny)
    return np.dot(nx, ny)

vocab_size = len(word_to_id)
C = create_co_matrix(corpus, vocab_size)
# print('C: ', C)
vector_you = C[word_to_id['you']]
vector_i = C[word_to_id['i']]
print('cos_similarity(vector_you, vector_i): ', cos_similarity(vector_you, vector_i)) # 0.7071067691154799

def most_similar(query, word_to_id, id_to_word, word_matrix, top=3):
    if query not in word_to_id:
        print("%s(을)를 찾을 수 없습니다." %query)
        return
    print('[query]', query)
    query_id = word_to_id[query]
    query_vec = word_matrix[query_id]
    vocab_size = len(word_to_id)
    similarity = np.zeros(vocab_size)
    for i in range(vocab_size):
        similarity[i] = cos_similarity(word_matrix[i], query_vec)
        # print('similarity: ', similarity[i])
    count = 0
    for i in (-1 * similarity).argsort():
        # print((-1*similarity).argsort())
        if id_to_word[i] == query:
            continue
        print('%s: %s' %(id_to_word[i], similarity[i]))
        count += 1
        if count >= top:
            return

print(most_similar('you', word_to_id, id_to_word, C))

def ppmi(C, verbose=False, eps=1e-8):
    M = np.zeros_like(C, dtype=np.float32)
    N = np.sum(C)
    S = np.sum(C, axis=0)
    total = C.shape[0] * C.shape[1]
    cnt=0
    for i in range(C.shape[0]):
        for j in range(C.shape[1]):
            pmi = np.log2(C[i, j] * N / (S[i]*S[j]) + eps)
            M[i, j] = max(0, pmi)
            if verbose:
                cnt += 1
                if cnt % ((total)//100) == 0:
                    print('%.1f%% 완료' %(100*cnt/total))
    return M

W = ppmi(C)
print(W)