import requests as rqs

from Fetch.RedditPostWrapper import RedditPostListWrapper

sorters = {
    'new': 'new',
    'hot': 'hot',
    'controversial': 'controversial',
    'top': 'top',
    'rising': 'rising'
}

periods = {
    'all': 'all',
    'day': 'day',
    'hour': 'hour',
    'week': 'week',
    'month': 'month',
    'year': 'year',
}

def buildPostList(samples, subreddit, **kwargs):
    posts = getPostsFrom(subreddit, **kwargs)
    while posts.getPostCount() < samples:
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