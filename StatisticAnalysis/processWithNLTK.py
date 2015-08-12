'''
Created on 2015年7月30日

@author: hainan
'''

import nltk


if __name__ == '__main__':
    raw = open('OccupationData.txt', encoding="utf-8").read()
    tokens = nltk.word_tokenize(raw)
    wf = nltk.FreqDist(word.lower() for word in tokens)
    occuptaion_t = wf.hapaxes()
    print(tokens)
    
    raw_cause = open('CauseData.txt', encoding="utf-8").read()
    cause_tokens = nltk.word_tokenize(raw_cause)
    wf_cause = nltk.FreqDist(word.lower() for word in cause_tokens)
    cause_t = wf_cause.hapaxes()
    print(cause_tokens)
    
    raw_fat_cause = open('FatCauseData.txt', encoding="utf-8").read()
    tokens_fat = nltk.word_tokenize(raw_fat_cause)
    wf_fat = nltk.FreqDist(word.lower() for word in tokens_fat)
    fat_cause_t = wf_fat.hapaxes()
    print(tokens_fat)
    
    print("Occupation Classification")
    print(occuptaion_t)
    print("Cause Classification")
    print(cause_t)
    print("FatCause Classification")
    print(fat_cause_t)
    
#     occupation_fre = {}
#     for occuptation_item in occuptaion_t:
#         print(occuptation_item)
#         occupation_fre[occuptation_item] = wf.freq(occuptation_item)
#     
#     sorted_freq = sorted(occupation_fre.items(), key=lambda occupation_fre:occupation_fre[1])
#     print(sorted_freq)