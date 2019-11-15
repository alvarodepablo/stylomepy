from __future__ import unicode_literals
import nltk
from . import TextStatistics as stats
import math
from .Silabizator import spanishSilabizer
from .styleTokenizer import styleTokenizer

def INFLESZ(text):
    """Calculates the INFLESZ Index of a Spanish text.
    
    The function returns the INFLESZ Readability Index value of a
    text written in Spanish.
    
    """

    tokens = styleTokenizer(text, lang = 'es')
    sentenceNumber = stats.sentencesCount(text,lang = 'es')
    wordsNumber = len(tokens)
    s = spanishSilabizer()
    syllablesNumber = 0

    for token in tokens:
        syllablesNumber += len(s(token))
    
    inflesz = 206.835 - ((62.3*syllablesNumber)/wordsNumber)-(wordsNumber/sentenceNumber)
    
    return inflesz

def muReadability(text):
    """Calculates the mu Readability Index of a Spanish text.
    
    The function returns the mu Readbility Index of a text written
    in Spanish.
    
    """

    tokens = styleTokenizer(text, lang = 'es', punct = True)
    charsPerWord = stats.charactersPerWord(text, lang = 'es', punct = True)
    wordsNumber = len(tokens)
    variance = 0
    
    for token in tokens:
        variance += ((len(token)-charsPerWord)**2)
        
    variance /= wordsNumber
    
    mu = ((wordsNumber/(wordsNumber - 1)) * (charsPerWord/variance)) * 100
        
    return mu   