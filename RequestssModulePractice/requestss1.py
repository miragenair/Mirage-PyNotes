import requests
import json
from win32com.client import Dispatch

'''
API-Key:    78fcbbb09dc347d3a64c59020a98987b
'''
api = '78fcbbb09dc347d3a64c59020a98987b'
url = "https://newsapi.org/v2/everything?q=tesla&from=2022-05-22&sortBy=publishedAt&apiKey=78fcbbb09dc347d3a64c59020a98987b"

r = requests.get(url, '78fcbbb09dc347d3a64c59020a98987b')

json_string = r.text

print(r.text)

data = json.loads(json_string)
print(type(data))
print(data)

articledict = (data['articles'])

print(type(articledict))
print(articledict)

for News in articledict:
    print(News)

def sandwich(n):
    return News[n]

titl = (News['title'])
des = (News['description'])
con = (News['content'])

newsread = (titl,des,con)

# def content():
#     return data




# ---------------------------------------------------TEXT TO VOICE------------------------------------------------------
speak = Dispatch("SAPI.SpVoice")
speak.Speak("this is the top tesla news in the world right now")
speak.Speak(f"the title of the news is {titl}, Description is, {des} and the content of the news is, {con} , published by {(News['author'])}")
# speak.Speak(newsread)
