import json


class PredictNextWordServices:
    def __init__(self):
        pass

    def predict_next_word_dict(self, last_word):
        vocab_dict = self.load_vocab_dict('app/api/predict/vocab_dict.json')
        last_word = last_word.lower()
        last_word = last_word.replace('.', '')
        return list(vocab_dict[last_word].keys())[:10]

    def get_word_in_dict(self, substart_word):
        vocab_dict = self.load_vocab_txt('app/api/predict/dictionary.txt')
        # if word start with word then add to list
        word_list = []
        for word in vocab_dict:
            if word.startswith(substart_word):
                word_list.append(word)
                if len(word_list) == 10:
                    break 
        return word_list
      
    def load_vocab_txt(self, path):
        with open(path) as f:
            vocab_dict = f.read().splitlines()
        return vocab_dict

    def load_vocab_dict(self, path):
        with open(path) as f:
            vocab_dict = json.load(f)
        return vocab_dict