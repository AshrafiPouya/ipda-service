import re
import nltk
import heapq

from decorators.text_summarize_decorators import command_line
from decorators.general_decorators import del_and_collect

from core.file_handler import FileHandler

class TextSummarization:

    def __init__(self) -> None:
        nltk.download("punkt")
        nltk.download("stopwords")
    

    @command_line
    def summarize(self, text: str):

        article_text = text
        article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)
        article_text = re.sub(r'\s+', ' ', article_text)

        formatted_article_text = re.sub('[^a-zA-Z]', ' ', article_text )
        formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)
        sentence_list = nltk.sent_tokenize(article_text)
        stopwords = nltk.corpus.stopwords.words('english')

        word_frequencies = {}
        for word in nltk.word_tokenize(formatted_article_text):
            if word not in stopwords:
                if word not in word_frequencies.keys():
                    word_frequencies[word] = 1
                else:
                    word_frequencies[word] += 1
            maximum_frequncy = max(word_frequencies.values())
        for word in word_frequencies.keys():
            word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)
            sentence_scores = {}
        for sent in sentence_list:
            for word in nltk.word_tokenize(sent.lower()):
                if word in word_frequencies.keys():
                    if len(sent.split(' ')) < 30:
                        if sent not in sentence_scores.keys():
                            sentence_scores[sent] = word_frequencies[word]
                        else:
                            sentence_scores[sent] += word_frequencies[word]
        summary_sentences = heapq.nlargest(7, sentence_scores, key=sentence_scores.get)

        summary = ' '.join(summary_sentences)

        self.summary = summary
        
        return summary
    
    @del_and_collect('summary')
    def save_file(self):
        fh = FileHandler()
        fh.create_text_file(fname=f"{fh.get_file_name('exports')}_s", content=self.summary)
