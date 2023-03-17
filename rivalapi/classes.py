import typing
from dataclasses import dataclass

@dataclass
class WeHeartItUser:
    username: str = None
    display:  str = None
    avatar:  str = None
    posts:  int = 0
    hearts:  int = 0
    link:  str = None
    location:  str = None
    collections:  int = 0
    followers:  int = 0
    following:  int = 0
    badges: typing.Union[list,str,None] = None

@dataclass
class GoogleImage:
    url:  str = None
    source:  str = None
    title:  str = None
    domain:  str = None

@dataclass
class GoogleSearch:
    title: str = None
    link: str = None
    snippet: str = None

@dataclass
class Oxford:
    status: bool = False
    message: str = None
    word: str = None
    wordtype: str = None
    pronounciation: str = None
    definition: str = None
    examples: list = None

@dataclass
class UwUify:
    text: str = None

@dataclass
class TwitterUser:
    error: str = None
    username: str = None
    nickname: str = None
    url: str = None
    id: int = None
    bio: str = None
    location: str = None
    avatar_url: str = None
    banner_url: str = None
    created_at: float = None
    verified: str = None
    private: str = None
    followers: str = None
    following: str = None
    tweets: str = None
    likes: str = None
    raw_followers: int = None
    raw_following: int = None
    raw_tweets: int = None
    raw_likes: int = None
    color: int = None

@dataclass
class TwitterAuthor:
    avatar: str = None
    screen_name: str = None

@dataclass
class TwitterMedia:
    image: str = None
    video: str = None

@dataclass
class TwitterPost:
    nsfw: str = None
    color: int = None
    timestamp: int = None
    text: str = None
    url: str = None
    like_count: str = None
    retweet_count: str = None
    raw_like_count: int = None
    raw_retweet_count: int = None
    footer_url: str = None
    author: list[TwitterAuthor] = None
    media: list[TwitterMedia] = None

@dataclass
class TwitchUser:
    username: str = None
    display_name: str = None
    followers: str = None
    viewers: str = None
    created_at: int = None
    description: str = None
    avatar: str = None









