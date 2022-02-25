import json


class PredictNextWordServices:
		def __init__(self):
				pass
  
		def predict_next_word_dict(self, last_word):
			vocab_dict = self.load_vocab_dict('app/api/predict/vocab_dict.json')
			last_word =	last_word.lower()
			last_word =	last_word.replace('.', '')
			return list(vocab_dict[last_word].keys())[:10]
			
			
		def load_vocab_dict(self, path):
				with open(path) as f:
						vocab_dict = json.load(f)
				return vocab_dict
