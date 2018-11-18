from flask import Flask, request, jsonify

from .ShitPoster3000 import train
from .Fetch.FetchPosts import periods, sorters

app = Flask(__name__)

@app.route('/', methods=['GET'])
def mimickSubreddit():
    params = request.args
    subreddit = params.get('subreddit', 'worldnews')
    sort = params.get('sort', sorters['controversial'])
    period = params.get('period', periods['all'])
    samples = params.get('samples', 500)
    sentenceCount = int(params.get('sentenceCount', 1))
    useTitles = params.get('useTitles', True)
    if sort != sorters['top'] and sort != sorters['controversial']:
        model = train(subreddit, useTitles=useTitles, sort=sort, samples=samples)
    else:
        model = train(subreddit, useTitles=useTitles, sort=sort, params={'t': period}, samples=samples)
    return jsonify([model.make_sentence(tries=100) for _ in range(sentenceCount)])
