

#%%
# 01 한국 법률 말뭉치
from konlpy.corpus import kolaw
c=kolaw.open('constitution.txt').read()
print(c[:10])

#%%
from konlpy.corpus import kobill
d=kobill.open('1809890.txt').read()
print(d[:15])

#%%
# 사전
## 문장, 명사, 품사 태깅
from konlpy.tag import Kkma
from konlpy.utils import pprint
kkma=Kkma()

#%%
pprint(kkma.sentences('네 안녕하세요. 반갑습니다'))
pprint(kkma.nouns('질문이나 건의사항은 여기에 남겨주세요.'))
pprint(kkma.pos('우리는 데이터 과학자입니다. 멋진 과학자입니다.'))

#%%
# 02. 문서 탐색
from collections import Counter

from konlpy.corpus import kolaw
from konlpy.tag import Hannanum
from konlpy.utils import concordance, pprint
from matplotlib import pyplot

#%%
doc = kolaw.open('constitution.txt').read()
pos=Hannanum().pos(doc)
cnt=Counter(pos)

#%%
pos

#%%
print('nchars :', len(doc))
print('ntokens :', len(doc.split()))
print('nmorphs :', len(set(pos)))
print('\nTop 20 grequent morphemes:'); pprint(cnt.most_common(20))
print('\nLocations of "대한민국" in the document:')
concordance('u 대한민국', doc, show=True )

#%%
# 지프의 법칙 확인(Zipf's laws)
def draw_zipf(count_list, filename, color='blue', marker='o'):
    sorted_list = sorted(count_list, reverse=True)
    pyplot.plot(sorted_list, color=color, marker=marker)
    pyplot.xscale('log')
    pyplot.yscale('log')
    pyplot.savefig(filename)
    
draw_zipf(cnt.values(), 'zipf.png')

#%%
# 연어 찾기
from konlpy.tag import Kkma
from konlpy.corpus import kolaw
from konlpy.utils import pprint
from nltk import collocations

#%%
measures = collocations.BigramAssocMeasures()
doc=kolaw.open('constitution.txt').read()
doc[1:10]

#%%
# collocations 패키지 참조
print('\Collocations among tagged words:')
tagged_words = Kkma().pos(doc) # 품사 태깅
finder = collocations.BigramCollocationFinder.from_words(tagged_words)
finder

#%%
pprint(finder.nbest(measures.pmi, 10)) # top 5 n-grams with highest PMI

#%%
print('\nCollocations among words:')
words=[w for w, t in tagged_words]
ignored_words = [u'안녕']
finder = collocations.BigramCollocationFinder.from_words(words)
finder.apply_word_filter(lambda w: len(w) < 2 or w in ignored_words)
finder.apply_freq_filter(3) # only bigrams that appear 3+ times
pprint(finder.nbest(measures.pmi, 10))

#%%
print('\nCollocations among tags:')
tags = [t for w, t in tagged_words]
finder = collocations.BigramCollocationFinder.from_words(tags)
pprint(finder.nbest(measures.pmi, 5))

#%%
# 03. 구문 분석
import konlpy
import nltk

#%%
# POS tag a sentence
sentence = u'만 6세 이하의 초등학교 취학 전 자녀를 양육하기 위해서는'
words = konlpy.tag.Twitter().pos(sentence)

#%%
# Define a chunk grammar, or chunking rules, then chunk
grammar = """
NP: {<N.*>*<Suffix>?} # Noun phrase
VP: {<V.*>*} # Verb phrase
AP: {<A.*>*} # Adjective pharase
"""
parser = nltk.RegexpParser(grammar)
chunks = parser.parse(words)
print('# Print whole tree')
print(chunks.pprint())

#%%
print('\n# Print noun phrases only')
for subtree in chunks.subtrees():
    if subtree.label()=='NP':
        print(' '.join((e[0] for e in list(subtree))))
        print(subtree.pprint())
        
# Display the chunk tree
chunks.draw()

#%%
# 04. KoNlpy를 활용한 멀티 스레딩
from konlpy.tag import Kkma
from konlpy.corpus import kolaw
from threading import Thread
import jpype

#%%
def do_concurrent_tagging(start, end, lines, result):
    jpype.attachThreadToJVM()
    l=[k.pos(lines[i]) for i in rage(start, end)]
    result.append(l)
    return

#%%
if __name__=='__main__':
    import time
    
    print('Number of lines in document:')
    k=Kkma()
    lines=kolaw.open('constitution.txt').read().splitlines()
    nlines = len(lines)
    print(nlines)
    
    print('Batch tagging:')
    s=time.clock()
    result=[]
    l=[k.pos(line) for line in lines]
    result.append(l)
    t=time.clock()
    print(t-s)
    
    print('Concurrent tagging:')
    result =[]
    t1=Thread(target=do_concurrent_tagging, args=(0, int(nlines/2), lines, result))
    t2=Thread(target=do_concurrent_tagging, args=(int(nlines/2), nlines, lines, result))
    t1.start();  t2.start()
    t1.join(); t2.join()
    
    m= sum(result, []) # Merge results
    print(time.clock()-t)

#%% 
# 트리 그리기 by 상훈님
sentence = u'만 6세 이하의 초등학교 취학 전 자녀를 양육하기 위해서는'
words = konlpy.tag.Twitter().pos(sentence)
#%%
# Define a chunk grammar, or chunking rules, then chunk
grammar = """
NP: {<N.*>*<Suffix>?} # Noun phrase
VP: {<V.*>*} # Verb phrase
AP: {<A.*>*} # Adjective phrase
"""
parser = nltk.RegexpParser(grammar)
chunks = parser.parse(words)
print("# Print whole tree")
print(chunks.pprint())

#%%
print("\n# Print noun phrases only")
for subtree in chunks.subtrees():
 if subtree.label()=='NP':
     print(' '.join((e[0] for e in list(subtree))))
     print(subtree.pprint())
# Display the chunk tree
chunks.draw()    

