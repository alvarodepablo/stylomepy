from . import TextStatistics as stats
import math
from scipy.stats import hypergeom
from .styleTokenizer import styleTokenizer


def TTR(text, lang, lowercase = True, punct = True, contract = True, stopWords = False):

    tokens = styleTokenizer(text, lang, lowercase = lowercase, punct = punct, contract = contract, stopWords = stopWords)
    wordsNumber = len(tokens)
    diffWords = stats.differentWords(text, lang, lowercase = lowercase, contract = contract, punct = punct, stopWords = stopWords)[0]
    TTR = (diffWords/wordsNumber)
    return TTR*100

def MSTTR(text, lang, segment, lowercase = True, punct = True, contract = True, stopWords = False):
    
    tokens = styleTokenizer(text, lang, lowercase = lowercase, punct = punct, contract = contract, stopWords = stopWords)
    wordsNumber = len(tokens)
    MSTTR = 0
    i = 0
    auxList = []
    segmentsNumber = 0
    if len(tokens)/segment > 1:
        for token in tokens:
            if len(auxList) < segment:
                auxList.append(token)              
                i += 1
            else:
                MSTTR += TTR(' '.join(auxList), lang)
                auxList = []
                segmentsNumber += 1
                
                if wordsNumber - i >= segment:
                    continue
                else:
                    break
        auxList = []
        j = 0
        while len(auxList) < wordsNumber - i:
            auxList.append(tokens[::-1][j])
            j += 1
        MSTTR += TTR(' '.join(auxList), lang)
        segmentsNumber += 1
        result = MSTTR/segmentsNumber
    else:
        result = 0
                
    return result

def MATTR(text, window, lang, lowercase = True, punct = True, contract = True, stopWords = False):
    tokens = styleTokenizer(text, lang, lowercase = lowercase, punct = punct, contract = contract, stopWords = stopWords)
    wordsNumber = len(tokens)
    if window > wordsNumber:
        result = 0
    else:
        MATTR = 0
        auxList = []
        j = 0
        while j + window <= wordsNumber:
            for i in range(j, window + j):
                auxList.append(tokens[i])
            j += 1
            MATTR += TTR(' '.join(auxList), lang)
            auxList = []
        result = MATTR/(j)

    return result

def MTLD(text, limit, lang, lowercase = True, punct = True, contract = True, stopWords = False):
    tokens = styleTokenizer(text, lang, lowercase = lowercase, punct = punct, contract = contract, stopWords = stopWords)
    wordsNumber = len(tokens)
    def MTLDimplementation(usedTokens, limit):
        nSegm = 0
        segment = []

        for i in range(0, wordsNumber):
            segment.append(usedTokens[i])
            if TTR(' '.join(segment), lang)/100 < limit:
                nSegm += 1
                segment = []
            elif i == wordsNumber - 1 and TTR(' '.join(segment), lang)/100 > limit:
                rest = 1 - TTR(' '.join(segment), lang)/100
                nSegm += rest/(1 - limit)
        return wordsNumber/nSegm
    
    MTLD1 = MTLDimplementation(tokens, limit)
    MTLD2 = MTLDimplementation(tokens[::-1], limit)
    
    result = (MTLD1 + MTLD2)/2

    if result > 100:
        return 100
    else:
        return result

def HDD(text, lang, lowercase = True, punct = True, contract = True, stopWords = False):
    tokens = styleTokenizer(text, lang, lowercase = lowercase, punct = punct, contract = contract, stopWords = stopWords)
    wordsNumber = len(tokens)
    freqWords = stats.freqWords(text, lang, lowercase = lowercase, punct = punct, contract = contract, stopWords = stopWords)
    probSum = 0
    k = 1
    lista = []
    for i in range(0, len(freqWords)):
        [N, d, n] = [wordsNumber, freqWords[i][1], 42]
        probType = hypergeom.pmf(k, N, d, n)
        probSum += probType
        lista.append(probType)  
        
    return probSum/42 *100