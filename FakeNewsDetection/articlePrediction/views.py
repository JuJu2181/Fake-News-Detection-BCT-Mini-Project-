import pickle
from django.shortcuts import render
from django.http import HttpResponse
from . import scraping
from keras.preprocessing import text,sequence
import tensorflow as tf
from tensorflow import keras
from . import svm, process

from keras.preprocessing.sequence import pad_sequences
from sklearn.feature_extraction.text import TfidfVectorizer


# Create your views here.
def home(request):
    context = {}

    #Article Prediction part
    articleDiv = request.POST.get('article') if request.POST.get('article') != None else ''
    scraping.printArticle(articleDiv)

    #Url Prediction  part
    urlll = request.POST.get('url-article') if request.POST.get('url-article') != None else ''
    if urlll != '':
        contentsReceived = scraping.getUrl(urlll)
        value = scraping.parse(contentsReceived)
        context={
            'values': value
        }
        print(context)




    # with open('E:\RB\Fake-News-Detection-BCT-Mini-Project-\FakeNewsDetection\model.pkl','rb') as md:
    #     lstmModel = pickle.load(md)

    # lstmModel = tf.keras.models.load_model('E:\RB\Fake-News-Detection-BCT-Mini-Project-\saved_model\lstmModel')

    # news = "Washington Sundar has been ruled out of the Twenty20 series against West Indies. The Chennai-based Indian spinner, who staged an international comeback in the recent ODI series against West Indies after a long jury-forced hiatus, will require a few weeks to recover, it is learned.  Washington Sundar suffered a left hamstring muscle strain during fielding in the third ODI, said a statement from BCCI. Kuldeep Yadav has been named as his replacement.Washington will have to report at the NCA on Tuesday (February 15) and is set to spend three weeks at the NCA.   The three Twenty20 Internationals against West Indies will start in Kolkata on February 16.   Sundar left the Indian camp that is currently in Kolkata. The Indian team had a net session at Eden Gardens in Kolkata on Monday (February 14) evening."
    # # scraping.printArticle(news)

    # max_features = 10000
    # max_len = 300

    # tokenizer = text.Tokenizer(num_words=max_features)

    # tokenized_test = tokenizer.texts_to_sequences(news)
    # news = sequence.pad_sequences(tokenized_test, maxlen=max_len)
    
    # tfidf_vectorizer=TfidfVectorizer(stop_words='english')
    # news = tfidf_vectorizer.transform(news)
    
    # value = lstmModel.predict(news)
    # context={
    #         'values': value
    #     }
    # # print(urlll)
    # return render(request, 'index.html', context)

def index(request):
    context = {}
    #Article Prediction part
    articleDiv = request.POST.get('article') if request.POST.get('article') != None else ''


    articleDiv = process.cleanWord(articleDiv)
    value = svm.Svm(articleDiv)
    context={
            'values': value
        }
    return render(request, 'index2.html', context)