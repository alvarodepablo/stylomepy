import nltk
from nltk.tag import StanfordPOSTagger
from nltk import FreqDist
#import wordfreq
from .styleTokenizer import styleTokenizer

def wordsCount(text = '', lang = 'en', contract = True):
    """
    Calculates the number of words in the text.
    
    """

    wordsNo = len(styleTokenizer(text, lang, contract = contract))
    
    return wordsNo

def sentencesCount(text = '', lang = 'en'):
    """
    Calculates the number of sentences in the text.

    """
    
    sentsNo = len(styleTokenizer(text, lang, token='sent'))

    return sentsNo


def charactersPerSentence(text = '', lang = 'en', punct = True, contract = False, blank = False):
    """
    Calculates an average of the number of characters per sentence.
    if blank: blankspace are counted as a character
    
    """
    charPerSent = 0
    sentsNo = sentencesCount(text,lang)
    sents = styleTokenizer(text, lang, token='sent', punct = punct, contract = contract)
    if punct:
        sentsAux = []
        puncts=[',', '.', ':', ';', '?', '¿', '¡','!', '-', '\"', '\'']
        for sent in sents:
            for c in puncts :
                if c in sent :
                    sent = sent.replace(c, '')
            sentsAux.append(sent)
        sents = sentsAux
    if blank:
        b = " "
    else: 
        b = ""
    for sent in sents:
        charPerSent += len(sent.replace(" ", b))
        
    charPerSent /= sentsNo
    
    return charPerSent

def charactersPerWord(text = '', lang = 'en', contract = False, punct = True):
    """Calculates an average of the number of characters per word.
    
    The function returns an average of the number of characters per word.
    
    """
    charPerWord = 0
    tokens = styleTokenizer(text, lang, contract = contract, punct = punct)
    
    wordsNo = len(tokens)
    
    for token in tokens:
        charPerWord += len(token)
        
    charPerWord /= wordsNo
    
    return charPerWord


def differentWords(text, lang, lowercase = True, contract = True, punct = True, stopWords = False):
    """Identifies the different words within the text.
    
    Returns the number of different words and a list with them.
    The function replaces uppercase with lowercase.
    
    """
    
    diffWordsList = []
    tokens = styleTokenizer(text, lang, lowercase = lowercase, contract = contract, punct = punct, stopWords = stopWords)
    tokens.sort()

    i = 0
    for token in tokens:
        if i+1 < len(tokens):
            if token != tokens[i + 1]:
                diffWordsList.append(token)
        else:
            diffWordsList.append(token)
        i += 1
    
    return len(diffWordsList), diffWordsList

def wordClass(text, lang, lowercase = True, contract = True, punct = True, stopWords = False):
    """It searchs the different types of words in the text
    
    It tokenizes the text in tagged words. Then, and thanks to the tags,
    it classifies the words by class and save the words in different lists.
    It returns the number of conjunctions, adjectives, verbs, nouns, adverbs, prepositions,
    determiners, pronouns and interjections..
    
    """

    tokens = styleTokenizer(text, lang, lowercase = lowercase, contract = contract, punct = punct, stopWords = stopWords)
    nouns = []
    verbs = []
    adjectives = []
    adverbs = []
    conjunctions = []
    prepositions = []
    determiners = []
    pronouns = []
    interjections =[]
    
    if lang == "en":
        
        taggedTokens = nltk.pos_tag(tokens)
        
        for tupla in taggedTokens:
            if tupla[1] == "CC":
                conjunctions.append(tupla[0])
            elif tupla[1][0] == "J":
                adjectives.append(tupla[0])
            elif tupla[1][0] == "V":
                verbs.append(tupla[0])
            elif tupla[1][0] == "N":
                nouns.append(tupla[0])
            elif tupla[1][0] == "R" or tupla[1] == "WRB":
                adverbs.append(tupla[0])
            elif tupla[1] == "TO" or tupla[1] == "IN":
                prepositions.append(tupla[0])
            elif tupla[1] == "WDT" or tupla[1] == "PDT" or tupla[1] == "DT":
                determiners.append(tupla[0])
            elif tupla[1] == "PRP" or tupla[1] == "PRP$" or tupla[1] == "WP" or tupla[1] == "WP$":
                pronouns.append(tupla[0])
            elif tupla[1] == "UH":
                interjections.append(tupla[0])
            
        result = [len(conjunctions), len(adjectives), len(verbs), len(nouns), len(adverbs), len(prepositions),
                  len(determiners), len(pronouns), len(interjections)]
            
            
    elif lang == "es":
        
        tagger = r"./stanfordPosTagger/models/spanish.tagger"
        jar = r"./stanfordPosTagger/stanford-postagger.jar"
        taggedTokens = StanfordPOSTagger(tagger,jar).tag(tokens)

        for tupla in taggedTokens:
            if tupla[1][0] == "c":
                conjunctions.append(tupla[0])
            elif tupla[1][0] == "a":
                adjectives.append(tupla[0])
            elif tupla[1][0] == "v":
                verbs.append(tupla[0])
            elif tupla[1][0] == "n":
                nouns.append(tupla[0])
            elif tupla[1][0] == "r":
                adverbs.append(tupla[0])
            elif tupla[1][0] == "s":
                prepositions.append(tupla[0])
            elif tupla[1][0] == "d":
                determiners.append(tupla[0])
            elif tupla[1][0] == "p":
                pronouns.append(tupla[0])
            elif tupla[1][0] == "i":
                interjections.append(tupla[0])
        
        result = [len(conjunctions), len(adjectives), len(verbs), len(nouns), len(adverbs), len(prepositions),
                  len(determiners), len(pronouns), len(interjections)]
    
    
    return result


def wordsPerSentence(text, lang, contract = False):
    """Calculates an average of the words per sentence.
    
    Return the average of words per sentence.
    
    """    
    sents = sentencesCount(text, lang)
    tokens = wordsCount(text, lang, contract = contract)

    wordsPerSent = tokens/sents
    
    return wordsPerSent

def shortWords(text, lang, contract = True, stopWords = False):
    """It counts the number of short words within the text.
    
    It returns the number of words with 3 characters or less (Short Words).
    
    """
    tokens = styleTokenizer(text, lang, contract = contract, stopWords = stopWords)

    shortWords = 0
    for token in tokens:
        if len(token) <= 3:
            shortWords += 1
            
    return shortWords

def commonUncommonWords(text, lang, lowercase = True, contract = True, punct = True, stopWords = False):
    """ Analyzes a text searching for common and uncommon words.
    
    It uses wordfreq library for searching common and uncommon words
    in English or Spanish languages.
    
    Returns the number of common and uncommon words.
    
    """
    diffWords = differentWords(text, lang, lowercase = lowercase, contract = contract, punct = punct, stopWords = stopWords)[1]
    commonWords = 0
    uncommonWords = 0
    
    for token in diffWords:
        if wordfreq.zipf_frequency(token, lang) > 2:
            commonWords += 1
        else:
            uncommonWords += 1
            
    return commonWords, uncommonWords

def freqWords(text, lang, lowercase = True, punct = True, contract = True, stopWords = False):
    """Calculates the frequency of each word within a text
    
    Returns de most common words.
    
    """
    tokens = styleTokenizer(text, lang, lowercase = lowercase, punct = punct, contract = contract, stopWords = stopWords)

    fdist = FreqDist(tokens)

    return fdist.most_common()