from collections import Counter
from os import path
import jieba

jieba.load_userdir(path.join(path.dirname(__file__),'userdict//userdict.txt'))

def word_segment(text):
    '''
    用来把中文分成词
    '''

    jieba_word = jieba.cut(text, cut_all = False)
    data = []
    for word in jieba_word:
        data.append(word)
    dataDict = Counter(data)
    with open('sth.txt', 'w') as fw:
        for k,v in dataDict.items():
            fw.write('%s,%d\n' % (k,v))

    jieba_word = jieba.cut(text, cut_all = False)
    seg_list = ' '.join(jieba_word)
    return seg_list