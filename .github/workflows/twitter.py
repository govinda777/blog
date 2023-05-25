import requests
import tweepy

# Configuração da API do GitHub
GITHUB_API = "https://api.github.com"
REPO = "govinda777/blog"
USER = "seu_nome_de_usuario"

# Configuração da API do Twitter
CONSUMER_KEY = 'seu_consumer_key'
CONSUMER_SECRET = 'seu_consumer_secret'
ACCESS_TOKEN = 'seu_access_token'
ACCESS_TOKEN_SECRET = 'seu_access_token_secret'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

def get_latest_article(user, repo):
    url = f"{GITHUB_API}/repos/{user}/{repo}/commits"
    response = requests.get(url)
    commits = response.json()
    print(commits)
    latest_commit = commits[0]
    return latest_commit["commit"]["message"], latest_commit["html_url"]

def post_to_twitter(message, url):
    tweet = f"{message} {url}"
    api.update_status(tweet)

message, url = get_latest_article(USER, REPO)
post_to_twitter(message, url)
