#!ShitPoster3000/bin/python3
import sys

import markovify as mkv

from Fetch.FetchPosts import buildPostList

def train(subreddit, useTitles=True, sort='top', params=None, numSamples=500, nodes=2):
    postList = buildPostList(
        subreddit,
        numSamples,
        params=params or {},
        sort=sort
    )
    if useTitles:
        corpus = postList.getNormalizedPostTitles()
    else:
        corpus = postList.getNormalizedPostTexts()
    formattedCorpus = '\n'.join(corpus)
    return mkv.NewlineText(formattedCorpus, state_size=nodes)


if __name__ == '__main__':
    model = train('news', sort='controversial', params={'t': 'all'})
    if len(sys.argv) > 1:
        sentences = int(sys.argv[1])
    else:
        sentences = 1
    for _ in range(sentences):
        print(model.make_sentence(tries=100))




