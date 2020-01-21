import contractions
import nltk
nltk.download('punkt')
nltk.download("popular")
import re
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords

def styleTokenizer(text, lang='es', token='word', lowercase = True, punct = True, contract = True, stopWords = True):
    """Splits in words a text.
   
    This function removes undesirable characters and extends English contractions.
    Then it appends each word to a list.
    Returns that list of words.
    Options:
        token: Default = 'word'
            If 'word', tokenize the text in words.
            If 'sent' or 'sentence', tokenize the text in sentences.
        lowercase: Defalut = True
            If True, the words are lower.
            If False, the words are not lower.
        punct (Only required if token='word'): Default = True
            If True: remove punctuation signs
            If False: no remove them
        contract(Only important if the text is in English): Default = True
            If True: expand english contractions
            If False: Does not expand them
        stopWords: Defalut = False
            If False: don't remove stopwords
            If True: remove stopwords   
    """
    #Lemmatizacion
    
    
    if lowercase:
        text = text.lower()
        
    text = re.sub(r'[/\\|#·@$~%&¬]', r'', text)
    text = re.sub(r'(?<=[.,?!;\–¿¡])(?=[^\s])', r' ', text)
    text = re.sub(r'[\W_]+ ,.\-\)\(><!?¡¿:;\]\[', '', text)
    text = re.sub(r'([\-–])', r'', text)
    text = re.sub(r'uf[0-9][0-9][0-9a-z]', r'', text)
    if contract and lang == 'en':
        text = contractions.fix(text)
        text = re.sub(r' \' ', r' ', text)
         
    text = re.sub('\s+', ' ', text).strip()
    text = re.sub(r' \'', r' ', text)

    if token == 'word':
        
        tokens = wTokenizer(text, lang, lowercase, punct, contract, stopWords)

    elif token == 'sent' or token == 'sentence':
        
        tokens = []

        if lang == "en":
            sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
       
        elif lang == "es":
            sent_detector = nltk.data.load('tokenizers/punkt/spanish.pickle')
        
        senTokens = sent_detector.tokenize(text.strip())
        senTokens = [x for x in senTokens if x]
        
        for sent in senTokens:
            aTokens = wTokenizer(sent, lang, lowercase, punct, contract, stopWords)
            tokens.append(' '.join(aTokens))
    
    return tokens

def removeStopWords(tokens, lang):
    """
    Removes the stop words in English or Spanish languages
    
    """
    if lang == "en":
        stopWords = set(stopwords.words("english"))
    elif lang == "es":
        stopWords = set(stopwords.words("spanish"))
    wordsFiltered = []

    for token in tokens:
        if token.lower() not in stopWords:
            wordsFiltered.append(token)
 
    return wordsFiltered

def wTokenizer(text, lang, lowercase, punct, contract, stopWords):
    
    if (contract and lang == 'en') or lang == 'es':
        tokens = nltk.word_tokenize(text)
    else:
        tknzr = TweetTokenizer()
        tokens = tknzr.tokenize(text)
    if punct:
        tokens = ([token for token in tokens if any(c.isalpha() or c is '+' for c in token)])
    if stopWords:
        tokens = removeStopWords(tokens, lang)
    
    return tokens