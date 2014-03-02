from django import template
import requests
from bs4 import BeautifulSoup

register = template.Library()

BLOG_URL = 'http://feeds.feedburner.com/agroguia'
def blog_post_brief(index):
    r = requests.get(BLOG_URL)
    rss = BeautifulSoup(r.content, "xml")
    item = rss.find_all('item')[index]
    return {
        'title': item.find('title').get_text(),
        'description': item.find('description').get_text() ,
        'link': item.find('link').get_text() ,
        'creator': item.find('creator').get_text() 
    }


register.inclusion_tag('_blog_post.html')(blog_post_brief)
