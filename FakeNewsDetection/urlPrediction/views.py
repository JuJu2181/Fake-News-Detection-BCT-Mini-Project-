from asyncio.windows_events import NULL
from django.shortcuts import render
from django.http import HttpResponse
from . import scraping
# from tensorflow.keras.preprocessing.sequence import pad_sequences
# from tensorflow.keras.models import Sequential
# from sklearn.feature_extraction.text import TfidfVectorizer
# tfidf_vectorizer=TfidfVectorizer(stop_words='english')
# data=tfidf_vectorizer.fit_transform(data) 
# X_test=tfidf_vectorizer.transform(X_test)
# tokenized_test = tokenizer.texts_to_sequences(data)
# li = sequence.pad_sequences(tokenized_test, maxlen=max_len)

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
    news = "Washington Sundar has been ruled out of the Twenty20 series against West Indies. The Chennai-based Indian spinner, who staged an international comeback in the recent ODI series against West Indies after a long jury-forced hiatus, will require a few weeks to recover, it is learned.  Washington Sundar suffered a left hamstring muscle strain during fielding in the third ODI, said a statement from BCCI. Kuldeep Yadav has been named as his replacement.Washington will have to report at the NCA on Tuesday (February 15) and is set to spend three weeks at the NCA.   The three Twenty20 Internationals against West Indies will start in Kolkata on February 16.   Sundar left the Indian camp that is currently in Kolkata. The Indian team had a net session at Eden Gardens in Kolkata on Monday (February 14) evening."
    scraping.printArticle(news)
    # tfidf_vectorizer=TfidfVectorizer(stop_words='english')
    # data=tfidf_vectorizer.fit_transform(data) 
    # X_test=tfidf_vectorizer.transform(X_test)
    # tokenized_test = tokenizer.texts_to_sequences(news)
    # li = sequence.pad_sequences(tokenized_test, maxlen=max_len)
    # with open('model1.pkl','rb') as md:
    #     lstmModel = pickle.load(md)
    
    # value = lstmModel.predict(news)
    # context={
    #         'values': value
    #     }
    # print(urlll)
    return render(request, 'index.html', context)