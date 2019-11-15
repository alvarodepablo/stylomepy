from . import TextStatistics as stats
from . import englishRIAlgorithms as riEn
from . import spanishRIAlgorithms as riEs
from . import VocabularyRichness as vr
from . import formality as form
from . import coherenceMetrics as coh

class StyleMetrics():

	def _setReadabilityIndex(self, text, lang, contract):


		if lang == "en":
			readabilityIndexes = {'ARI': riEn.ARI(text, contract), 
							'FleschRI': riEn.fleschRI(text, contract),
							'FogCount': riEn.fogCount(text, contract)
							}
		else:
			readabilityIndexes = {'INFLESZ': riEs.INFLESZ(text),
							'Mu': riEs.muReadability(text)
							}

		return readabilityIndexes

	def _setTextStatistics(self, text, lang, lowercase, punct, contract, stopWords, blank):

		diffWords = stats.differentWords(text, lang, lowercase, contract, punct, stopWords)
		#commonUncommonWords = stats.commonUncommonWords2(text, lang, lowercase, contract, punct, stopWords)
		wordsClasses = stats.wordClass(text, lang, lowercase, contract, punct, stopWords)

		statistics = {'sentencesCount': stats.sentencesCount(text, lang),
							'charPerSent': stats.charactersPerSentence(text, lang, punct, contract, blank),
							'charPerWord': stats.charactersPerWord(text, lang, contract, punct),
							'wordsPerSent': stats.wordsPerSentence(text, lang, contract),
							'diffWords': diffWords[0],
							'conjunctions': wordsClasses[0],
							'adjectives': wordsClasses[1],
							'verbs': wordsClasses[2],
							'nouns': wordsClasses[3],
							'adverbs': wordsClasses[4],
							'prepositions': wordsClasses[5],
							'determiners': wordsClasses[6],
							'pronouns': wordsClasses[7],
							'interjections': wordsClasses[8],
							'shortWords': stats.shortWords(text, lang, contract, stopWords),
							#'commonWords': commonUncommonWords[0],
							#'uncommonWords': commonUncommonWords[1],
							}

		return statistics

	def __init__(self, text, lang = 'en', lowercase = True, punct = True, contract = True, stopWords = False, blank = False,
	 window = 500, limit = 0.72, segment = 100, coherence = False, extractor = None,):
		if coherence:
			self._cIndex = coh.coherenceMeasure(text, lang, extractor, punct, contract, stopWords)
		else:
			self._cIndex = 0
		self._fIndex = form.wfFormIndex(text, lang, lowercase, contract, stopWords)
		self._adjScore = form.adjScore(text, lang, lowercase, contract, stopWords)
		self._vIndex = {'TTR': vr.TTR(text, lang, lowercase, punct, contract, stopWords),
		 				'MSTTR': vr.MSTTR(text, lang, segment, lowercase, punct, contract, stopWords), 
		 				'MATTR': vr.MATTR(text, window, lang, lowercase, punct, contract, stopWords),
						'MTLD': vr.MTLD(text, limit, lang, lowercase, punct, contract, stopWords),
						'HDD': vr.HDD(text, lang, lowercase, punct, contract, stopWords)
						}
		self._rIndex = self._setReadabilityIndex(text, lang, contract)
		self._textStats = self._setTextStatistics(text, lang, lowercase, punct, contract, stopWords, blank)
		
		
		


	def getCoherenceIndex(self):
		return self._cIndex

	def getFormalityIndex(self):
		return self._fIndex

	def getAdjScore(self):
		return self._adjScore

	def getReadabilityIndex(self, index = ''):

		result = ''

		if index in self._rIndex:
			result = self._rIndex[index]
		elif index == '':
			result = self._rIndex
		else:
			result = 'ERROR: Bad Index'

		return result

	def getVocabularyIndex(self, index = ''):

		result = ''

		if index in self._vIndex:
			result = self._vIndex[index]
		elif index == '':
			result = self._vIndex
		else:
			result = 'ERROR: Bad Index'

		return result

	def getTextStatistics(self, index = ''):

		result = ''

		if index in self._textStats:
			result = self._textStats[index]
		elif index == '':
			result = self._textStats
		else:
			result = 'ERROR: Bad Index'

		return result
