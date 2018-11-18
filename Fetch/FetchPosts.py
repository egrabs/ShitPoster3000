import requests as rqs

from Fetch.RedditPostWrapper import RedditPostListWrapper

_validSorters = [
    'new',
    'hot',
    'controversial',
    'top',
    'rising'
]

_validPeriods = [
    'all',
    'day',
    'hour',
    'week',
    'month',
    'year',
]

def _validateParams(kwargs):
    params = kwargs.get('params')
    if params:
        period = params.get('t')
        if period and period not in _validPeriods:
            raise ValueError('{} is not a valid period!'.format(period))
    sort = kwargs.get('sort')
    if sort and sort not in _validSorters:
        raise ValueError('{} is not a valid sort!'.format(kwargs['sort']))

def buildPostList(subreddit, numSamples, **kwargs):
    _validateParams(kwargs)
    posts = getPostsFrom(subreddit, **kwargs)
    while posts.getPostCount() < numSamples:
        if 'params' in kwargs:
            kwargs['params']['after'] = posts.getAfter()
            kwargs['params']['count'] = posts.getPostCount()
        else:
            kwargs['params'] = {
                'after': posts.getAfter(),
                'count': posts.getPostCount()
            }
        posts += getPostsFrom(subreddit, **kwargs)
    return posts


def getPostsFrom(subreddit, params=None, sort='new', filterParams=None):
    finalParams = (params or {})
    finalParams.update({'raw_json': '1'})
    res = rqs.get(
        'http://www.reddit.com/r/{subreddit}/{sort}.json'.format(subreddit=subreddit, sort=sort),
        headers={
            'User-agent': 'ShitPoster3000',
        },
        params=finalParams
    )
    if res.status_code != 200:
        return RedditPostListWrapper({})
    postList = RedditPostListWrapper(res.json())
    postList.filter(**(filterParams or {}))
    return postList