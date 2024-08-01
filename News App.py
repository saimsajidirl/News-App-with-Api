# its a news app that will show you the top 10 latest news from us

import requests

apikey="1c3d661bb65e48d38165d75873835580"

def getnews():
    
    newsurl="https://newsapi.org/v2/top-headlines?country=us&apiKey="+apikey
    news=requests.get(newsurl).json()

    articles=news["articles"]
  
    newarticle=[]
    for arti in articles:
        newarticle.append(arti["title"])
    
    for i in range(10):
  
      print(f"The News No {i+1} is:\n\n",newarticle[i])

getnews()


