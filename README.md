# Stylomepy

*Stylomepy* is a **Python** library for measuring the style of a text. It is available in Spanish and Engish languages.
It can be used in the analysis of the **statistics** of a text, the **readability index** of it, the **vocabulary richness**, **formality** and **coherence**.


# Installation

*Stylomepy* can be installed using *pip* and *Python 3.0* is needed:
```
pip3 install stylomepy
```

Another way is to clone this repository and then install it:
```
git clone https://github.com/alvarodepablo/stylomepy
cd stylomepy
python3 setup.py install
```

# Use of the library

When we have the text or texts we want to analyze, it is necessary to create a *StyleMetrics* object that will include the style features of that text:
```python
import stylomepy
style = stylomepy.StyleMetrics(text, lang = 'en', lowercase = True, punct = True, contract = True, stopWords = False, blank = False, window = 500, limit = 0.72, segment=100, coherence= False, extractor = None)
```
***text*** is the text to analyze<br/>
***lang*** is the language of that text. Only English ('en') and Spanish ('es') are available<br/>
***lowercase*** if True all words become lower<br/>
***punct*** if True punctuation signs are removed<br/>
***contract*** if True English contractions are expanded<br/>
***stopWords*** if True stopwords are removed<br/>
***blank*** if True some functions take blank spaces as characters<br/>
***window*** is the window size of the **MATTR algorithm** (usually **500** or **100**)<br/>
***limit*** is the limit of the **MTLD algorithm** (usually **0.72**)<br/>
***segment*** is the size of the **MSTTR algorithm** segment (usually 100)<br/>
***coherence*** if True the coherence of the text will be computed (*extractor* needed)<br/>
***extractor*** is a word2vec extractor instance<br/>


## TextStatistics

To analyze the statistics of the text:
```python
style.getTextStatistics(index='index')
```
The available indexes are *sentencesCount*, *charPerSent*, *charPerWord*, *wordsPerSent*, *diffWords*, *conjunctions*, *adjectives*, *verbs*,  *nouns*, *adverbs*, *prepositions*, *determiners*, *pronouns*, *interjections*, *shortWords*.

## Readability Index

To analyze the readability difficulty of a text:
```python
style.getReadabilityIndex(index='index')
```
The available spanish indexes are *INFLESZ* and *Mu*. The available english indexes are *ARI*, *FleschRI* and *FogCount*.

## Vocabulary Richness

To analyze the lexical diversity of a text:
```python
style.getVocabularyRichness(index='index')
```
The available indexes are *TTR*, *MSTTR*, *MATTR*, *MTLD* and *HDD*.

## Formality

To analyze the formality score of a text:
```python
style.getFormalityIndex()
```
To analyze the adjective score of a text:
```python
style.getAdjScore()
```

## Coherence
To analyze the coherence of a text, when the *StyleMetrics* object is created, *coherence* attribute needs to be ***True*** and a word2vec extractor instance has to be created.
```python
from gsitk.features.word2vec import Word2VecFeatures
w2v_extractor = Word2VecFeatures(w2v_model_path="path", w2v_format='"format"', convolution=[1,0,0])

style = stylomepy.StyleMetrics(text, coherence = True, extractor = w2v_extractor)
style.getCoherenceIndex()
```

## Another way of use
If you want to use the library analyzing a few statistics, you do not need to create a *StyleMetrics* object. You can use some of the developed functions separately. The next examples show this:
```python
import stylomepy

adverbs = stylomepy.TextStatistics.wordClass(text, lang = 'en', lowercase = True, contract = False, punct = True, stopWords = False)[4]
shortWords = stylomepy.TextStatistics.shortWords(text, lang ='es', contract = True, stopWords = True)
lexDiversity = stylomepy.VocabularyRichness.MATTR(text, window = 100, lang = 'es', lowercase = True, punct = True, contract = True, stopWords = False)
```

## Possible issues
When the library analyzes a Spanish text, an error could appear saying something like *NLTK was unable to find the java file!
Use software specific configuration paramaters or set the JAVAHOME environment variable.*. If it happens, run the next script and then use the library.
```python
import os
import nltk

java_path = "jdk_path"
os.environ['JAVAHOME'] = java_path

nltk.internals.config_java(java_path)

```
Where *jdk_path* is the **Java JDK** path in your system.

