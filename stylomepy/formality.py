from . import TextStatistics as stats
from .styleTokenizer import styleTokenizer

def wfFormIndex(text, lang, lowercase = True, contract = True, stopWords = False):
    """Returns the Formality Score of a text.
    
    This function returns a value based on the weight that each kind of word
    (adjective, noun, pronoun, etc.) has within the text.
    
    """

    diffWords = stats.wordClass(text, lang, lowercase = lowercase, contract = contract, stopWords = stopWords)
    tokens = styleTokenizer(text, lang, lowercase = lowercase, contract = contract, stopWords = stopWords)
    wordsNumber = len(tokens)
    
    formalityIndex = ((diffWords[3] + diffWords[1] + diffWords[5] + diffWords[6] - diffWords[7] - diffWords[2]
                        - diffWords[4] - diffWords[8])/wordsNumber*100  +100)/2
    
    return formalityIndex
    

def adjScore(text, lang, lowercase = True, contract = True, stopWords = False):
    """Returns the Adjective Score of a text.
    
    This function returns the Adjective Score of a text, which is a formality
    measure of a text.
    
    """
    diffWords = stats.wordClass(text, lang, lowercase = lowercase, contract = contract, stopWords = stopWords)
    wordsNumber = stats.wordsCount(text, lang, contract = contract)
    
    adf = diffWords[1]/wordsNumber * 100
    
    return adf