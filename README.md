# ShitPoster3000

[Shitpost](https://www.urbandictionary.com/define.php?term=shitpost)

## Given a subreddit, train up a markov chain model on posts from that subreddit and start imitating posts

### [Inspired by](http://slatestarcodex.com/2018/10/30/sort-by-controversial/)

### runs on python3

1. `virtualenv -p python3 ShitPoster3000`
2. `source ShitPoster3000/bin/activate`
3. `pip install -r requirements.txt`
4. to run as CLI: `python3 ShitPoster3000 <optional number of sentences>`
5. as server: `./startServer.sh`

### If running as a server: URL Params (all optional)
#### `param` - description - `default`
* `subreddit` - which subreddit to pull posts from - `worldnews`
* `sort` - sort by new, top, controversial, etc - `controversial`
* `period` - day, week, month, year, all - `all`
* `samples` - number of post samples to train the markov chain model on - `500`
* `sentenceCount` - how many simulated sentences to generate - `1`
* `useTitles` - whether to use the titles of the posts as training data (uses the posts' body text if set to `false`) - `true`