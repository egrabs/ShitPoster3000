from copy import deepcopy

from TextAnalysis.TextRejectors import buildRejectionPipeline
from TextAnalysis.TextFilters import buildFilterPipeline

class RedditPostListWrapper:
    def __init__(self, json):
        self.json = json
        self.data = json.get('data', {})
        self.kind = json.get('kind', '')
        self.rawPosts = self.data.get('children', [])
        self.posts = [RedditPostWrapper(rawPost) for rawPost in self.rawPosts]

    def getPostCount(self):
        return len(self.posts)

    def getAfter(self):
        return self.data.get('after')

    def getBefore(self):
        return self.data.get('before')

    def filter(self, **kwargs):
        def predicate(post):
            pipeline = buildRejectionPipeline(**kwargs)
            for rejector in pipeline:
                if rejector(post.getText()):
                    return False
            return True
        return list(filter(predicate, self.posts))

    def getPostTexts(self):
        return map(lambda post: post.getText(), self.posts)

    def getNormalizedPostTexts(self, **kwargs):
        return map(lambda post: post.getNormalizedText(**kwargs), self.posts)

    def getPostById(self, name):
        for post in self.posts:
            if post.getId() == name:
                return post
        return None

    def __add__(self, other):
        if type(other) != RedditPostListWrapper:
            raise ValueError('Cannot add RedditPostListWrapper to type {}.'.format(type(other)))
        if self.kind != other.kind:
            raise ValueError('Cannot add RedditPostListWrapper of kind {} to kind {}.'.format(self.kind, other.kind))
        after = other.getAfter() if self.getBefore() is None else self.getAfter()
        newChildren = self.rawPosts + other.rawPosts
        json = deepcopy(self.json)
        json['data']['children'] = newChildren
        json['data']['after'] = after
        return RedditPostListWrapper(json)


class RedditPostWrapper:
    def __init__(self, json):
        self.json = json
        self.data = json.get('data', {})
        self.kind = json.get('kind', '')

    def getId(self, post):
        return self.data.get('name', '')

    def getText(self):
        return self.data.get('selftext', '')

    def getNormalizedText(self, **kwargs):
        txt = self.getText()
        for textFilter in buildFilterPipeline(**kwargs):
            txt = textFilter(txt)
        return txt

    def getTitle(self):
        return self.data.get('title', '')
