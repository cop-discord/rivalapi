import aiohttp,asyncio,orjson,typing,discord
from classes import WeHeartItUser,GoogleImage,GoogleSearch,Oxford,UwUify,TwitterUser,TwitterPost,TwitchUser,MedalPost,TwitterMedia,TwitterAuthor

class RivalAPI(object):
    def __init__(self, api_key):
        self.__api_key = api_key
        self.base_url = 'https://api.rival.rocks/'

    async def request(self,method:str,endpoint:str,params:typing.Any):
        async with aiohttp.ClientSession(headers={'api-key':self.__api_key}) as session:
            if method == "get":
                async with session.get(self.base_url+endpoint+params,headers={'api-key':self.__api_key}) as response:
                    if 'uwuify' not in endpoint:
                        if response.status == 404:
                            return None
                        return await response.json()
            elif method == "post":
                async with session.post(self.base_url+endpoint,params=params,headers={'api-key':self.__api_key}) as response:
                    if response.status == 404:
                        return None
                    return await response.json()
            
    async def uwuify(self,text:str):
        return await self.request(method="get",endpoint="uwuify",params=f"?text={text}")
    
    async def user(self,user_id:int):
        return await self.request(method="get",endpoint="user",params=f"?user_id={user_id}")
        
    async def tags(self):
        return await self.request(method="get",endpoint="tags",params=None)
            
    async def tiktok(self,url:str):
        return await self.request(method="get",endpoint=f"tiktok",params=f"?url={url}")
            
    async def tiktok_userinfo(self,username:str):
        return await self.request(method="get",endpoint="tiktok/userinfo",params=f"?username={username}")
            
    async def medal(self,url:str):
        try:
            request = await self.request(method="get",endpoint="medal",params=f"?url={url}")
            return MedalPost(request['video'],request['title'],request['url'])
        except Exception as e:
            print(e)
            return None

    async def twitter_userinfo(self,username:str):
        try:
            request = await self.request(method="get",endpoint="twitter/user",params=f"?username={username}")
            return TwitterUser(request['error'],request['username'],request['nickname'],request['url'],request['id'],request['bio'],request['location'],request['avatar_url'],request['banner_url'],request['created_at'],request['verified'],request['private'],request['followers'],request['following'],request['tweets'],request['likes'],request['raw_followers'],request['raw_following'],request['raw_tweets'],request['raw_likes'],request['color'])
        except Exception as e:
            print(e)
            return None

    async def twitter_post(self,url:str):
        try:
            request = await self.request(method='get',endpoint='twitter/post',params=f'?url={url}')
            return TwitterPost(request['nsfw'],request['color'],request['timestamp'],request['text'],request['url'],request['like_count'],request['retweet_count'],request['raw_like_count'],request['raw_retweet_count'],request['footer_url'],TwitterAuthor(request['author']),TwitterMedia(request['media']))
        except Exception as e:
            print(e)
            return None

    async def twitch(self,username:str):
        try:
            request = await self.request(method='get',endpoint='twitch',params=f'?username={username}')
            return TwitchUser(request['username'],request['display_name'],request['followers'],request['viewers'],request['created_at'],request['description'],request['avatar'])
        except Exception as e:
            print(e)
            return None

    async def google_images(self,query:str,safe:bool=False):
        try:
            request = await self.request(method='post',endpoint='google/images',params={'query':query,'safe':f'{safe}'})
            return [GoogleImage(res['url'],res['source'],res['title'],res['domain']) for res in request['results']]
        except Exception as e:
            print(e)
            return None

    async def google_search(self,query:str,safe:bool=False):
        try:
            request = await self.request(method='post',endpoint='google/search',params={'query':query,'safe':f'{safe}'})
            return [GoogleSearch(res['title'],res['link'],res['snippet']) for res in request['results']]
        except Exception as e:
            print(e)
            return None
    
    async def weheartit_userinfo(self,username:str):
        try:
            request = await self.request(method='get',endpoint='weheartit/user',params=f"?username={username}")
            return WeHeartItUser(request['username'],request['display'],request['avatar'],request['posts'],request['hearts'],request['link'],request['location'],request['collections'],request['followers'],request['following'],request['badges'])
        except Exception as e:
            print(e)
            return None

    async def media_color(self,url:str):
        return await self.request(method='get',endpoint='media/color',params=f'?url={url}')
    
    async def media_ocr(self,url:str):
        return await self.request(method='get',endpoint='media/ocr',params=f'?url={url}')
    
    async def oxford(self,word:str,type:str="american_english"):
        try:
            request =await self.request(method='get',endpoint='oxford',params=f"?word={word}&type={type}")
            return Oxford(request['status'],request['message'],request['word'],request['wordtype'],request['pronounciation'],request['definition'],request['examples'])
        except Exception as e:
            print(e)
            return None

    async def lastfm_chart(self,username:str,filename:str="lastfm",chart_size:str="3x3",chart_type:str="album",timeperiod:str="alltime",limit:int=15):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.base_url+f"lastfm/chart?username={username}&size={chart_size}&chart_type={chart_type}&timeperiod={timeperiod}&limit={limit}",headers={'api-key':self.__api_key}) as response:
                if response.status == 404:
                    return None
                return discord.File(fp=io.BytesIO(await response.read()),filename=f"{filename}.png")
