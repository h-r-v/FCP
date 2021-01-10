import os
import numpy as np
import math

#d=50 for loading 50-dimension word embbeding model
d = 50
model = f'glove.6B.{d}d.txt'
file_path = os.path.abspath(os.path.join(os.path.join(os.getcwd(),'word embedding'),model))

#dict with keys as the word and values as the word embbeding
vocab_encoder = {}

with open(file_path) as f:
    for i in f:
        data = i.split()
        vocab_encoder[data[0]] = np.array(data[1::], dtype='float32')

#convert word to 50d word embedding
#Input:"Potato" Output: 50-d vector
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

#method 1 to check the distance between 2 words
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

#method 2 to check the distance between 2 words
def dist(emb1,emb2):
    if sum(emb1)==0 or sum(emb2)==0:
        return -1
    return np.sum((emb1-emb2)**2)

#method to find n-nearest words to a word
def nn(word,n=5):
    word = word.lower()
    return sorted(vocab_encoder.keys(), key= lambda x: dist(vocab_encoder[word],vocab_encoder[x]))[0:n+1]


if __name__ == '__main__':
    print(vec('Harsh raj verma'))











    



