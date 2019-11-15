from gensim.models.keyedvectors import KeyedVectors
from gsitk.features.word2vec import Word2VecFeatures
import numpy
from . import TextStatistics as stats
from .styleTokenizer import styleTokenizer

def coherenceMeasure(text, lang, extractor, punct = True, contract = True, stopWords = False):
	"""Returns the cocherence of a text.
    
	This function measures the coherence of a text.
	First, a Word Embeddings model is loaded. Then, the text is tokenized in sentences.
	The sentences are tokenized too. Finally, the cosine similarity of the sentences
	is measured and the final result is the average of these measures.

	The available Word Embeddings formats are .bin for English texts and .txt for Spanish texts.
    
	"""

	#from gensim.models.keyedvectors import KeyedVectors
	#from gsitk.features.word2vec import Word2VecFeatures
	#w2v_extractor = Word2VecFeatures(w2v_model_path="path", w2v_format='google_"..."', convolution=[1,0,0])
    
	sentList = styleTokenizer(text, lang, token='sent', punct = punct, contract = contract)
	sentListAux = []
	
	for sent in sentList:
		sentListAux. append(styleTokenizer(sent, lang, token='word', punct = punct, contract = contract))

	sentListAux = [x for x in sentListAux if x]
    
	transformSents = extractor.transform(sentListAux)
	transformSents = transformSents[~numpy.all(transformSents == 0, axis=1)]
    
	sum = 0

	for sent in range(len(transformSents)-1):
		sims = extractor.model.cosine_similarities(transformSents[sent], transformSents)
		sum += sims[sent + 1]
        
	return sum/len(transformSents)