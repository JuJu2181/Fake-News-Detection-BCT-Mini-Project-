from bs4 import BeautifulSoup
import requests

# cnn
# url = 'https://edition.cnn.com/2022/02/10/politics/donald-trump-gop-incumbents-impeach-votes/index.html' 

# bbc
# url ='https://www.bbc.com/news/av/60334905'

#ratopati
# url ='https://www.ratopati.com/story/220582/2022/2/10/congress'

#kathmandu post ----> yesma error aayo
# url = 'https://kathmandupost.com/national/2022/02/10/will-people-from-kalapani-region-get-to-exercise-their-franchise'

#nepalnews -----> yesma paragraph lina sakena
# url = 'https://nepalnews.com.np/s/nation/mohp-records-1-369-new-covid-cases-12-deaths-on-thursday'

#online khabar
# url = 'https://www.onlinekhabar.com/2022/02/1077033'

#nytimes
# url = 'https://www.nytimes.com/2022/02/10/us/politics/jan-6-trump-calls.html'

#foxnews
# url = 'https://www.foxnews.com/politics/democrats-scramble-reverse-course-covid-restrictions-midterms'

#nbcnews ----> error occured
# url = 'https://www.nbcnews.com/news/world/u-s-intel-nine-probable-russian-routes-ukraine-full-scale-n1288922'

#gaurdians news
# url = 'https://www.theguardian.com/football/2022/feb/10/chelsea-braced-for-kepa-arrizabalaga-bids-and-open-to-summer-exit'

#abc news
url = 'https://abcnews.go.com/Politics/pressure-builds-biden-democrats-move-past-covid/story?id=82754983'

def getUrl(url):
    pageContent = requests.get(url)
    print(pageContent)
    return pageContent

def parse(pagecontent):
    coup = BeautifulSoup(pagecontent.content, 'html.parser')
    try:
        if coup.find('article') is not None:
            print('article')
            contentParse = coup.find('article')
        # elif coup.find('section') is not None:
        #     print('section')
            # contentParse = coup.find('section')
        elif coup.find('div') is not None:
            print("div")
            #searching for the right div is left here
            contentParses = coup.find_all('div')
            # print(len(contentParses))
            # print('xir2')
            flag = 0
            for contentParse in contentParses:
                if contentParse.find('h1') is not None:
                    # print('xir3')
                    headline = contentParse.find('h1').text
                    print(f'Title: {headline}')
                    break
                flag +=1
            count = 0
            newsArticles = contentParses[flag].find_all('p')
            for newsArticle in newsArticles:
                if count == 3:
                    break
                print(newsArticle.text, end=' ')
                count +=1
            return 1
        else:
            errormessage = 'No content found'
            print(errormessage)
        
        # print('teha gayana')
        # print(contentParse)

        headline = contentParse.find('h1').text
        print(f"Title: {headline}")

        newsArticles = contentParse.find_all('p')
    # print(len(newsArticles))

        for newsArticle in newsArticles:
            print(newsArticle.text, end=' ')
    
    except:
        print("Error Occured")



parse(getUrl(url))