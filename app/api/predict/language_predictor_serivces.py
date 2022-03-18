import os
import pickle
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer

class LanguagePredictorServices:
    model_filename = 'predict_language_unigram_model2.pkl'
    model_filepath = os.path.join(os.path.dirname(__file__), model_filename)
    vectorizer_filename = 'predict_language_unigram_vectorizer2.pkl'
    vectorizer_filepath = os.path.join(os.path.dirname(__file__), vectorizer_filename)
    
    def __init__(self) -> None:
        print('Loading model...')
        self.load_vectorizer(self.vectorizer_filepath)
        self.load_model(self.model_filepath)
        print('Model loaded.')
    
    def predict(self, paragraph):
        if self.__class__.model is None:
            print('Model is not loaded')
            return None
        lower_paragraph = paragraph.lower()
        cleaned_paragraph = lower_paragraph.replace('.', '')
        X = self.__class__.vectorizer.transform([ cleaned_paragraph ])
        return self.__class__.model.predict(X)

    @classmethod
    def load_model(cls, model_filepath) -> MultinomialNB:
        try:
            cls.model = pickle.load(open(model_filepath, 'rb'))
            print('Model is loaded')
            return cls.model
        except Exception as e:
            print(e)
            print('Failed to load model')
    
    @classmethod            
    def load_vectorizer(cls, vectorizer_filepath) -> CountVectorizer:
      try:
        cls.vectorizer: CountVectorizer = pickle.load(open(vectorizer_filepath, 'rb'))
        print('Vectorizer is loaded')
        return cls.vectorizer
      except Exception as e:
        print(e)
        print('Failed to load vectorizer')
