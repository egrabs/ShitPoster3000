from flask import Flask, request, jsonify

from .ShitPoster3000 import train

app = Flask(__name__)

@app.route('/', methods=['GET'])
def mimickSubreddit():
    params = request.args
    subreddit = params.get('subreddit', 'worldnews')
    sort = params.get('sort', 'controversial')
    period = params.get('period', 'all')
    samples = params.get('samples', 500)
    sentenceCount = int(params.get('sentenceCount', 1))
    useTitles = params.get('useTitles', True)
    if sort != 'top' and sort != 'controversial':
        model = train(subreddit, useTitles=useTitles, sort=sort, numSamples=samples)
    else:
        model = train(subreddit, useTitles=useTitles, sort=sort, params={'t': period}, numamples=samples)
    return jsonify([model.make_sentence(tries=100) for _ in range(sentenceCount)])
