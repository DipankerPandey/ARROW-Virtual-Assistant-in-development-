import urllib.request
import wikipedia
import re, urllib.parse, urllib.request
import webbrowser

def check_internet_connection():
    try:
        urllib.request.urlopen('http://www.google.com')
        return True
    except:
        return False


def check_on_wiki(query):
    query = query.lower()
    query = query.replace("who is", " ")
    query = query.replace("what is", " ")
    query = query.replace("do you know", " ")
    query = query.replace("tell me", " ")
    query = query.replace("tell me about", " ")
    query = query.replace("what's", " ")
    query = query.replace("whats", " ")
    query = query.replace("who's", " ")
    query = query.replace("define", " ")
    query = query.replace("describe", " ")
    query.strip()
    try:
        data = wikipedia.summary(query, sentences=2, auto_suggest=False)
        return data
    except Exception as e:
        try:
            data = wikipedia.summary(query, sentences=2, auto_suggest=True)
            return data
        except:
            return ""

def search_google(query):
    query = query.lower()
    query = query.replace("search google ", "")
    query.strip()
    webbrowser.open('https://google.com/search?q='+''.join(query))

def youtube_search(query):
    query = query.lower()
    query = query.replace("search youtube ", "")
    query = query.replace("play music ", "")
    music_name = query
    query_string = urllib.parse.urlencode({"search_query": music_name})
    formatUrl = urllib.request.urlopen("https://www.youtube.com/results?" + query_string)
    search_results = re.findall(r"watch\?v=(\S{11})", formatUrl.read().decode())
    clip2 = "https://www.youtube.com/watch?v=" + "{}".format(search_results[0])
    webbrowser.open(clip2)