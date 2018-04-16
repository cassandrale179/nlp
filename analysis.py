import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

with open('C:\\Users\\lem1\\Desktop\\aws\\nlp\\lyrics.txt') as file:
    content = file.readlines()
lyrics = [x.strip() for x in content]

sid = SentimentIntensityAnalyzer()
for sentence in lyrics:
     print(sentence)
     ss = sid.polarity_scores(sentence)
     for k in ss:
         print('{0}: {1}, '.format(k, ss[k]), end='')
