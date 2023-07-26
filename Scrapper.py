from bs4 import BeautifulSoup
import tweepy
import requests

def scrape():
    page = requests.get("http://dev.to")
    soup = BeautifulSoup(page.content, "html.parser")
    home = soup.find(class_="articles-list crayons-layout__content")
    posts = home.find_all(class_="crayons-story__indention")
    top_post = posts[0].find("h2", class_="crayons-story__title").text.strip()


    tweet(top_post)

def tweet(top_post):
    consumer_key = "#"
    consumer_secret = "#"
    access_token = "#"
    access_token_secret = "#"
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    api.update_status(top_post)

scrape()
