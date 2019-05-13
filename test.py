from pyrsistent import inc, freeze, thaw, rex, ny, discard
news_paper = freeze({'articles': [{'author': 'Sara', 'content': 'A short article'},{'author': 'Steve', 'content': 'A slightly longer article'}],'weather': {'temperature': '11C', 'wind': '5m/s'}})
short_news = news_paper.transform(['articles', ny, 'content'], lambda c: c[:25] + '...' if len(c) > 25 else c)
very_short_news = news_paper.transform(['articles', ny, 'content'], lambda c: c[:15] + '...' if len(c) > 15 else c)
print(very_short_news.articles[0].content)
print(very_short_news.articles[1].content)
print(short_news is news_paper)
print(very_short_news is news_paper)
print(very_short_news.articles[0] is news_paper.articles[0])