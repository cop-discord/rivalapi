import typing
from dataclasses import dataclass
import humanize
def format_integer(value:int):
    val=humanize.intword(value).replace(" thousand","k").replace(" million","m").replace(" billion","b")
    return val

class TikTokUser(object):
    def __init__(self,dict):
        self.dict = dict

    @property
    def username(self):
        return self.dict.get("username")

    @property
    def display(self):
        return self.dict.get("display")

    @property
    def followers(self):
        return self.dict.get("followers")
    
    @property
    def formatted_followers(self):
        try:
            return format_integer(self.dict.get("followers"))
        except:
            return None

    @property
    def following(self):
        return self.dict.get("following")
    
    @property
    def formatted_following(self):
        try:
            return format_integer(self.dict.get("following"))
        except:
            return None

    @property
    def likes(self):
        return self.dict.get("likes")
    
    @property
    def formatted_likes(self):
        try:
            return format_integer(self.dict.get("likes"))
        except:
            return None

    @property
    def verified(self):
        return self.dict.get("verified")

    @property
    def private(self):
        return self.dict.get("private")

    @property
    def bio(self):
        return self.dict.get("bio")

    @property
    def url(self):
        return self.dict.get("url")

    @property
    def avatar(self):
        return self.dict.get("avatar")

    @property
    def avatar_color(self):
        return int(self.dict.get("avatar_color"),16)

    @property
    def tiktok_logo(self):
        return self.dict.get("tiktok_logo")

    @property
    def tiktok_color(self):
        return self.dict.get("tiktok_color")

class WeHeartItUser(object):
    def __init__(self,dict):
        self.dict = dict

    @property
    def username(self):
        if self.dict.get("username"):
            return self.dict['username']

    @property
    def display(self):
        if self.dict.get("display"):
            return self.dict['display']

    @property
    def avatar(self):
        return self.dict.get("avatar")

    @property
    def posts(self):
        return self.dict.get("posts")
    
    @property
    def formatted_posts(self):
        try:
            return format_integer(self.dict.get('posts'))
        except:
            return None

    @property
    def hearts(self):
        return self.dict.get("hearts")

    @property
    def formatted_hearts(self):
        try:
            return format_integer(self.dict.get('hearts'))
        except:
            return None

    @property
    def link(self):
        return self.dict.get("link")

    @property
    def location(self):
        return self.dict.get("location")

    @property
    def collections(self):
        return self.dict.get("collections")
    
    @property
    def formatted_collections(self):
        try:
            return format_integer(self.dict.get('collections'))
        except:
            return None

    @property
    def followers(self):
        return self.dict.get("followers")
    
    @property
    async def formatted_followers(self):
        try:
            return format_integer(self.dict.get("followers"))
        except:
            return None

    @property
    def following(self):
        return self.dict.get("following")
    
    @property
    def formatted_following(self):
        try:
            return format_integer(self.dict.get('following'))
        except:
            return None

    @property
    def badges(self):
        return self.dict.get("badges")

class GoogleImage(object):
    def __init__(self,dict):
        self.dict = dict

    @property
    def url(self):
        if self.dict.get("url"):
            return self.dict['url']

    @property
    def source(self):
        if self.dict.get("source"):
            return self.dict['source']

    @property
    def title(self):
        if self.dict.get("title"):
            return self.dict['title']

    @property
    def domain(self):
        if self.dict.get("domain"):
            return self.dict['domain']

class GoogleImageRequest(object):
    def __init__(self,dict):
        self.dic = dict
        status=self.dic['status']

    @property
    def results(self):
        return [GoogleImage(dict=res) for res in self.dic['results']]


class GoogleSearch(object):
    def __init__(self,dict):
        self.dict = dict

    @property
    def title(self):
        return self.dict.get('title')

    @property
    def link(self):
        return self.dict.get('link')

    @property
    def snippet(self):
        return self.dict.get('snippet')

class GoogleSearchRequest(object):
    def __init__(self,dict):
        self.dict = dict

    @property
    def results(self):
        return [GoogleSearch(res) for res in self.dict['results']]


class Oxford(object):
    def __init__(self,dict):
        self.dict = dict

    @property
    def status(self):
        return self.dict.get('status')

    @property
    def message(self):
        return self.dict.get('message')

    @property
    def word(self):
        return self.dict.get("word")

    @property
    def wordtype(self):
        return self.dict.get("wordtype")

    @property
    def pronounciation(self):
        return self.dict.get("pronounciation")

    @property
    def definition(self):
        return self.dict.get("definition")

    @property
    def examples(self):
        return self.dict.get("examples")

@dataclass
class UwUify:
    text: str = None

class TwitterUser(object):
    def __init__(self,dict):
        self.dict = dict

    @property
    def error(self):
        return self.dict.get("error")

    @property
    def username(self):
        return self.dict.get("username")

    @property
    def nickname(self):
        return self.dict.get("nickname")

    @property
    def url(self):
        return self.dict.get("url")

    @property
    def id(self):
        return self.dict.get("id")

    @property
    def bio(self):
        return self.dict.get("bio")

    @property
    def location(self):
        return self.dict.get("location")

    @property
    def avatar_url(self):
        return self.dict.get("avatar_url")

    @property
    def banner_url(self):
        return self.dict.get("banner_url")

    @property
    def created_at(self):
        return self.dict.get("created_at")

    @property
    def verified(self):
        return self.dict.get("verified")

    @property
    def private(self):
        return self.dict.get("private")

    @property
    def followers(self):
        return self.dict.get("followers")

    @property
    def formatted_followers(self):
        try:
            return format_integer(self.dict.get('raw_followers'))
        except:
            return None

    @property
    def following(self):
        return self.dict.get("following")

    @property
    def formatted_following(self):
        try:
            return format_integer(self.dict.get('raw_following'))
        except:
            return None


    @property
    def tweets(self):
        return self.dict.get("tweets")

    @property
    def formatted_tweets(self):
        try:
            return format_integer(self.dict.get('raw_tweets'))
        except:
            return None

    @property
    def likes(self):
        return self.dict.get("likes")
    
    @property
    def formatted_followers(self):
        try:
            return format_integer(self.dict.get('raw_followers'))
        except:
            return None


    @property
    def raw_followers(self):
        return self.dict.get("raw_followers")

    @property
    def raw_following(self):
        return self.dict.get("raw_following")

    @property
    def raw_tweets(self):
        return self.dict.get("raw_tweets")

    @property
    def raw_likes(self):
        return self.dict.get("raw_likes")

    @property
    def color(self):
        return self.dict.get("color")

class TwitterAuthor(object):
    def __init__(self,dict):
        self.dict = dict

    @property
    def screen_name(self):
        return self.dict.get("screen_name")

    @property
    def avatar(self):
        return self.dict.get("avatar")

class TwitterMedia(object):
    def __init__(self,dict):
        self.dict = dict

    @property
    def image(self):
        return self.dict.get("image")

    @property
    def video(self):
        return self.dict.get("video")

class TwitterPost(object):
    def __init__(self,dict):
        self.dict = dict

    @property
    def nsfw(self):
        return self.dict.get("nsfw")

    @property
    def color(self):
        return self.dict.get('color')

    @property
    def timestamp(self):
        return self.dict.get("timestamp")

    @property
    def text(self):
        return self.dict.get("text")

    @property
    def url(self):
        return self.dict.get("url")

    @property
    def like_count(self):
        return self.dict.get("like_count")

    @property
    def formatted_like_count(self):
        try:
            return format_integer(self.dict.get('raw_like_count'))
        except:
            return None

    @property
    def retweet_count(self):
        return self.dict.get('retweet_count')
    
    @property
    def formatted_retweet_count(self):
        try:
            return format_integer(self.dict.get('raw_retweet_count'))
        except:
            return None

    @property
    def raw_like_count(self):
        return self.dict.get("raw_like_count")

    @property
    def raw_retweet_count(self):
        return self.dict.get('raw_retweet_count')

    @property
    def author(self):
        return TwitterAuthor(dict=self.dict['author'])

    @property
    def media(self):
        return [TwitterMedia(dict=res) for res in self.dict['media']]

class TwitchUser(object):
    def __init__(self,dict):
        self.dict = dict

    @property
    def username(self):
        return self.dict.get('username')

    @property
    def display_name(self):
        return self.dict.get('display_name')

    @property
    def followers(self):
        return self.dict.get('followers')

    @property
    def viewers(self):
        return self.dict.get('viewers')

    @property
    def created_at(self):
        return self.dict.get("created_at")

    @property
    def description(self):
        return self.dict.get('description')

    @property
    def avatar(self):
        return self.dict.get('avatar')


class MedalPost(object):
    def __init__(self,dict):
        self.dict = dict

    @property
    def title(self):
        return self.dict.get("title")

    @property
    def video(self):
        return self.dict.get('video')

    @property
    def url(self):
        return self.dict.get('url')




