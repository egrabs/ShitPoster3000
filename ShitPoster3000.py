import sys

import markovify as mkv

from Fetch.FetchPosts import sorters, periods, buildPostList

def train(subreddit, useTitles=True, sort=sorters['top'], params=None, samples=500, nodes=2):
    postList = buildPostList(
        samples,
        subreddit,
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
    model = train('news', sort=sorters['controversial'], params={'t': periods['all']})
    if len(sys.argv) > 1:
        sentences = int(sys.argv[1])
    else:
        sentences = 1
    for _ in range(sentences):
        print(model.make_sentence(tries=100))




