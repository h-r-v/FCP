import os
import numpy as np
import math
import sklearn

d = 50
model = f'glove.6B.{d}d.txt'
file_path = os.path.join('AI Models', model)

vocab_encoder = {}

with open(file_path) as f:
    for i in f:
        data = i.split()
        vocab_encoder[data[0]] = np.array(data[1::], dtype='float32')

def vec(ip):

    if len(ip.split())==1:
        ip = ip.lower()
        if ip in vocab_encoder:
            return np.array(vocab_encoder[ip])
        else:
            return np.zeros(d)


    ans=[]
    for i in ip.lower().split():
        if i in vocab_encoder:
            ans.append(np.array(vocab_encoder[i]))
        else:
            ans.append(np.array([0]*d))
    return ans

def coss(v1,v2):
    if sum(v1)==0 or sum(v2)==0:
        return -1
    
    sumxx, sumxy, sumyy = 0, 0, 0
    for i in range(len(v1)):
        x = v1[i]; y = v2[i]
        sumxx += x*x
        sumyy += y*y
        sumxy += x*y
    return sumxy/(math.sqrt(sumxx)*math.sqrt(sumyy))

def dist(emb1,emb2):
    if sum(emb1)==0 or sum(emb2)==0:
        return -1
    return np.sum((emb1-emb2)**2)

def nn(word,n=5):
    word = word.lower()
    return sorted(vocab_encoder.keys(), key= lambda x: dist(vocab_encoder[word],vocab_encoder[x]))[0:n+1]

def rm_stopwords(x):
    ans = ''
    for i in x.lower().split():
        if i not in ['of', 'is', 'the']:
            ans+=i+' '

    return ans.lower()

def sentenceVecAvg(x):
    a = vec(x)
    return sum(a)/len(a)

def preprocess_sentence(x):
    x = rm_stopwords(x)
    x =  sentenceVecAvg(x)
    return x

def find_fn(clf, ip):
    a = preprocess_sentence(ip)
    ans = clf.predict(np.array(a).reshape((1,-1)))
    return ans

if __name__ == '__main__':
    print(vec('Harsh raj verma'))