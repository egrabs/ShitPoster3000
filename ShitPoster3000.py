import sys

import markovify as mkv

from Fetch.FetchPosts import buildCorpus, sorters, periods

def train(subreddit, samples=500, nodes=2):
    corpora = buildCorpus(
        samples,
        subreddit,
        params={
            't': periods['all']
        },
        sort=sorters['top']
    ).getNormalizedPostTexts()
    formattedCorpus = '\n'.join(corpora)
    return mkv.NewlineText(formattedCorpus, state_size=nodes)

if __name__ == '__main__':
    model = train('copypasta')
    if len(sys.argv) > 1:
        sentences = int(sys.argv[1])
    else:
        sentences = 1
    for _ in range(sentences):
        print(model.make_sentence(tries=100))