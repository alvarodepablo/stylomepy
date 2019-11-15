from __future__ import unicode_literals
import nltk
from . import TextStatistics as stats
import math
from .Silabizator import englishSilabizer
from .styleTokenizer import styleTokenizer

def ARI(text, contract = True):
    """Calculates the Automated Readability Index of an English text.
    
    The function returns the two available ARI's metrics of the library.
    The first is the clasical ARI and the second is the optimized ARI.
    
    """

    tokens = styleTokenizer(text, lang='en', contract = contract)
    sentenceNumber = stats.sentencesCount(text,lang = 'en')
    wordsNumber = len(tokens)
    
    charNumber = 0
    for token in tokens:
        charNumber += len(token)

    avgCharPerWord = charNumber/wordsNumber
    avgWordsPerSentence = wordsNumber/sentenceNumber

    ari = math.ceil(5.84*(avgCharPerWord) + 0.37*(avgWordsPerSentence) - 26.01)
            
    return ari


def fleschRI(text, contract = True):
    """Calculates the Flesch Readability Index of an English text.
    
    This function returns the two available Flesch's metrics of the library.
    The first is the Flesch Reading Ease Index and the second is the
    Flesch-Kincaid Grade Level Index.
    
    """
    
    tokens = styleTokenizer(text, lang = 'en', contract = contract)
    sentenceNumber = stats.sentencesCount(text,lang = 'en')
    wordsNumber = len(tokens)

    syllablesNumber = 0
    s = englishSilabizer()
    for token in tokens:
        syllablesNumber += s(token)    

    avgSyllPerWord = syllablesNumber/wordsNumber
    avgWordsPerSentence = wordsNumber/sentenceNumber

    fleschKincaidGradeLevel = 0.39*(avgWordsPerSentence) + 11.8*(avgSyllPerWord) - 15.59
    
    return fleschKincaidGradeLevel

def fogCount(text, contract = True):
    """Calculates the Fog Count Index of an English text.
    
    The function returns the two available Fog Count's metrics of the library.
    The first is the clasical Fog Count and the second is the optimized Fog Count.
    
    """

    tokens = styleTokenizer(text, lang = 'en', contract = contract)
    sentenceNumber = stats.sentencesCount(text,lang = 'en')
    wordsNumber = len(tokens)
    newFogCount = 0
    easyWords = []
    hardWords = []
    s = englishSilabizer()

    for token in tokens:
        if s(token) > 2:
            hardWords.append(token)
        else:
            easyWords.append(token)

    avgFogCount = (len(easyWords) + 3 * len(hardWords))/sentenceNumber
    
    newFogCount = (avgFogCount - 3)/2
                
    return newFogCount