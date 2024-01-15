# function to remove all urls
from tqdm import tqdm
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')
stop_words = set(stopwords.words('english'))

class Text_cleaning:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()

    def remove_urls(self, text):
        try:
            new_text = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", text).split())
            return new_text
        except:
            return text

    # make all text lowercase
    def text_lowercase(self, text):
        try:
            return text.lower()
        except:
            return text

    # remove numbers
    def remove_numbers(self, text):
        try:
            result = re.sub(r'\d+', '', text)
            return result
        except:
            return text

    # remove punctuation
    def remove_punctuation(self, text):
        try:
            translator = str.maketrans('', '', string.punctuation)
            return text.translate(translator)
        except:
            return text

    # tokenize
    def tokenize(self, text):
        try:
            text = word_tokenize(text)
            return text
        except:
            return text

    # remove stopwords

    def remove_stopwords(self, text):
        try:
            text = [i for i in text if not i in self.stop_words]
            return text
        except:
            return text

    # lemmatize Words

    def lemmatize(self, text):
        try:
            text = [self.lemmatizer.lemmatize(token) for token in text]
            return text
        except:
            return text

    # Creating one function so that all functions can be applied at once
    def preprocessing(self, data, columns=None, text=None):
        if text is None:
            for i in tqdm(range(data.shape[0])):
                text = data.iloc[i][columns]
                text = self.remove_urls(text)
                text = self.remove_numbers(text)
                text = self.text_lowercase(text)
                text = self.remove_punctuation(text)
                text = self.tokenize(text)
                text = self.remove_stopwords(text)
                text = self.lemmatize(text)
                text = ' '.join(text)
                text = text.replace('\n', ' ')
                data.iloc[i][columns] = text
            data[columns] = data[columns].apply(str)
            return data
        else:
            text = self.remove_urls(text)
            text = self.remove_numbers(text)
            text = self.text_lowercase(text)
            text = self.remove_punctuation(text)
            text = self.tokenize(text)
            text = self.remove_stopwords(text)
            text = self.lemmatize(text)
            text = ' '.join(text)
            text = text.replace('\n', ' ')
            return text
