# %%
import json
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.options import Options
import sqlite3
from ast import literal_eval

class EnglishWord:
    def __init__(self, word: str, dtype: str, pronunciation: str, definition: str):
        self.word = word
        self.dtype = dtype
        self.pronunciation = pronunciation
        self.definition = definition
        
    def serialize(self) -> dict:
        return {
            'word': self.word,
            'dtype': literal_eval(self.dtype),
            'pronunciation': literal_eval(self.pronunciation),
            'definition': literal_eval(self.definition)
        }

    def __repr__(self) -> str:
        return f'{self.word} {self.dtype} {self.pronunciation} {self.definition}'


class EnglishTranslator:
    url = "https://dictionary.cambridge.org/dictionary/english/"
    options = Options()
    options.add_argument("--headless")
    options.add_argument('--disable-gpu')
    executed_path = "C:\\Users\\Dai\\.wdm\\drivers\\chromedriver\\win32\\98.0.4758.102\\chromedriver.exe"
    if os.path.exists(executed_path):
        driver = webdriver.Chrome(executed_path, options=options)
    else:
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    dict_db_file = os.path.join(os.path.dirname(__file__), 'dictionary.sqlite')
    if not os.path.isfile(dict_db_file):
        conn = sqlite3.connect(dict_db_file)
        c = conn.cursor()
        c.execute('''CREATE TABLE dictionary
                     (word text, dtype text, pronunciation text, definition text)''')
        conn.commit()
        conn.close()

    @classmethod
    def translate(cls, word) -> dict:
        # query word in db sqlite
        conn = sqlite3.connect(cls.dict_db_file)
        c = conn.cursor()
        c.execute("SELECT * FROM dictionary WHERE word = ?", (word,))
        result = c.fetchone()
        if result:
            result_word = EnglishWord(result[0], result[1], result[2], result[3])
            return result_word.serialize()
        # query word in web
        result: EnglishWord = cls.crawl_word(word)
        cls.store_result_to_db(word, result)
        return result.serialize()
    
    @classmethod
    def store_result_to_db(cls, word: str, result: EnglishWord) -> None:
        conn = cls.get_db()
        c = conn.cursor()
        c.execute("INSERT INTO dictionary VALUES (?, ?, ?, ?)", 
                  (word, str(result.dtype), str(result.pronunciation), str(result.definition)))
        
        conn.commit()
        conn.close()
     
    @classmethod
    def get_db(cls) -> sqlite3.Connection:
        return sqlite3.connect(cls.dict_db_file)
        
    @classmethod
    def crawl_word(cls, word) -> EnglishWord:
        web_element = cls.get_element_after_wait(word, 'entry-body__el')
        result = {}
        dtype_list = [dtype.text for dtype in web_element.find_elements(By.CLASS_NAME, 'dpos')]
        ipa_el_list = web_element.find_elements(By.CLASS_NAME, 'ipa')
        pronunciation = {
            'uk': ipa_el_list[0].text,
            'us': ipa_el_list[1].text
        }
        ddef_block_list = web_element.find_elements(By.CLASS_NAME, 'ddef_block')
        definition = [ddef_block.text for ddef_block in ddef_block_list]
        # dpronunciation_sound_list:WebElement = web_element.find_elements(By.CLASS_NAME, 'c_aud')
        # result['pronunciation_sounds' = [dpronunciation_sound.text for dpronunciation_sound in dpronunciation_sound_list]    
        result = EnglishWord(word, str(dtype_list), str(pronunciation), str(definition))
        return result
    
    @classmethod
    def get_element_after_wait(self, word, element_id, timeout=1) -> WebElement:
        url_word = word.replace(' ', '_')
        url = self.url + url_word
        self.driver.get(url)
        delay = timeout
        try:
            web_element: WebElement = WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, element_id)))
            return web_element
        except Exception as e:
            print(e)
            
                


if __name__ == '__main__':
    translator = EnglishTranslator()
    word = 'hello'
    results = translator.translate(word)
    print(results)
# %%
    
