import aiohttp,asyncio,orjson,typing,discord,io
from .classes import Universal,WeHeartItUser,GoogleImage,GoogleSearch,Oxford,UwUify,TwitterUser,TwitterPost,TwitchUser,MedalPost,TwitterMedia,TwitterAuthor,GoogleImageRequest,GoogleSearchRequest,TikTokUser
import humanize

def format_integer(value:int):
    val=humanize.intword(value).replace(" thousand","k").replace(" million","m").replace(" billion","b")
    return val

class RivalInstagramAPI(object):
    def __init__(self, api_key, username, password, proxy):
        self.__api_key = api_key
        self.username = username
        self.password = password
        self.proxy = proxy
        self.session_id = None
    
    async def instagram_auth(self,username:str=None,password:str=None,proxy:str=None):
        if username == None:
            username = self.username
        if password == None:
            password = self.password
        if proxy == None:
            proxy = self.proxy
        async with aiohttp.ClientSession() as session:
            async with session.post(f"https://api.rival.rocks/instagram/auth/login",data={'username':username,'password':password,'proxy':proxy},headers={'api-key':self.__api_key}) as f:
                data=str(await f.text())
        self.session_id = data
        return self.session_id
    
    async def session_id(self):
        if self.session_id == None:
            return await self.instagram_auth(self.username,self.password,self.proxy)

    
    async def instagram_user(self,user:str,sessionid:str=None):
        if sessionid == None:
            sessionid = await self.session_id()
        async with aiohttp.ClientSession() as session:
            async with session.post(f"https://api.rival.rocks/instagram/user/info",data={'username':user,'sessionid':sessionid},headers={'api-key':self.__api_key}) as f:
                if f.status == 500:
                    async with session.post(f"https://api.rival.rocks/instagram/relogin",data={'sessionid':sessionid},headers={'api-key':self.__api_key}) as relogin:
                        if relogin.status == 500:
                            await self.instagram_auth(self.username,self.password,self.proxy)
                            async with session.post(f"https://api.rival.rocks/instagram/user/info",data={'username':user,'sessionid':sessionid},headers={'api-key':self.__api_key}) as nf:
                                data=await nf.json()
                else:
                    data=await f.json()
            return Universal(data).to_obj()
        
    async def instagram_media(self,url:str,sessionid:str=None):
        if sessionid == None:
            sessionid = await self.session_id()
        async with aiohttp.ClientSession() as session:
            async with session.post("https://api.rival.rocks/instagram/media/info",data={'url':url,'sessionid':sessionid},headers={'api-key':self__api_key}) as f:
                if f.status == 500:
                    async with session.post(f"https://api.rival.rocks/instagram/relogin",data={'sessionid':sessionid},headers={'api-key':self.__api_key}) as relogin:
                        if relogin.status == 500:
                            await self.instagram_auth(self.username,self.password,self.proxy)
                            async with session.post("https://api.rival.rocks/instagram/media/info",data={'url':url,'sessionid':sessionid},headers={'api-key':self__api_key}) as nf:
                                data=await nf.json()
                else:
                    data=await f.json()
            return Universal(data).to_obj()
        
    async def instagram_story(self,username:str,sessionid:str=None):
        if sessionid == None:
            sessionid = await self.session_id()
        async with aiohttp.ClientSession() as session:
            async with session.post("https://api.rival.rocks/instagram/story/user_stories",data={'username':username,'sessionid':sessionid},headers={'api-key':self.__api_key}) as f:
                if f.status == 500:
                    async with session.post(f"https://api.rival.rocks/instagram/relogin",data={'sessionid':sessionid},headers={'api-key':self.__api_key}) as relogin:
                        if relogin.status == 500:
                            await self.instagram_auth(self.username,self.password,self.proxy)
                            async with session.post("https://api.rival.rocks/instagram/story/user_stories",data={'username':username,'sessionid':sessionid},headers={'api-key':self.__api_key}) as nf:
                                data=await nf.json()
                else:
                    data=await f.json()
            return Universal(data).to_obj()
        

class RivalAPI(object):
    def __init__(self, api_key):
        self.__api_key = api_key
        self.base_url = 'https://api.rival.rocks/'

    async def request(self,method:str,endpoint:str,params:typing.Any):
        async with aiohttp.ClientSession(headers={'api-key':self.__api_key}) as session:
            if method == "get":
                async with session.get(self.base_url+endpoint+params.replace(' ','%20'),headers={'api-key':self.__api_key}) as response:
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
        
    async def tags(self,discriminator:int):
        return await self.request(method="get",endpoint="tags",params=None)

            
    async def tiktok(self,url:str):
        return await self.request(method="get",endpoint=f"tiktok",params=f"?url={url}")
            
    async def tiktok_userinfo(self,username:str):
        request = await self.request(method="get",endpoint="tiktok/userinfo",params=f"?username={username}")
        return TikTokUser(dict=request)
    
    async def medal(self,url:str):
        try:
            request = await self.request(method="get",endpoint="medal",params=f"?url={url}")
            return MedalPost(dict=request)
        except Exception as e:
            print(e)
            return None

    async def twitter_userinfo(self,username:str):
        try:
            request = await self.request(method="get",endpoint="twitter/user",params=f"?username={username}")
            return TwitterUser(dict=request)
        except Exception as e:
            print(e)
            return None

    async def twitter_post(self,url:str):
        try:
            request = await self.request(method='get',endpoint='twitter/post',params=f'?url={url}')
            return TwitterPost(dict=request)
        except Exception as e:
            print(e)
            return None

    async def tags(self,discriminator:str):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(self.base_url+"tags",headers={'api-key':self.__api_key}) as f:
                    t=await f.json()
            tags = reversed(t[discriminator])
            return tags
        except Exception as e:
            return None

    async def twitch(self,username:str):
        try:
            request = await self.request(method='get',endpoint='twitch',params=f'?username={username}')
            return TwitchUser(dict=request)
        except Exception as e:
            print(e)
            return None

    async def google_images(self,query:str,safe:bool=False):
         try:
            request = await self.request(method='post',endpoint='google/image',params={'query':query.replace(' ','%20'),'safe':f'{safe}'})
            return GoogleImageRequest(dict=request)
         except Exception as e:
            print(e)
            return e

    async def google_search(self,query:str,safe:bool=False):
        try:
            request = await self.request(method='post',endpoint='google/search',params={'query':query.replace(' ','%20'),'safe':f'{safe}'})
            return GoogleSearchRequest(dict=request)
        except Exception as e:
            print(e)
            return None
    
    async def weheartit_userinfo(self,username:str):
        request = await self.request(method='get',endpoint='weheartit/user',params=f"?username={username}")
        return WeHeartItUser(dict=request['user'])

    async def media_color(self,url:str):
        return await self.request(method='get',endpoint='media/color',params=f'?url={url}')
    
    async def media_ocr(self,url:str):
        return await self.request(method='get',endpoint='media/ocr',params=f'?url={url}')
    
    async def oxford(self,word:str,type:str="american_english"):
        try:
            request =await self.request(method='get',endpoint='oxford',params=f"?word={word}&type={type}")
            return Oxford(dict=request)
        except Exception as e:
            print(e)
            return None

    async def lastfm_chart(self,username:str,filename:str="lastfm",chart_size:str="3x3",chart_type:str="album",timeperiod:str="alltime",limit:int=15):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.base_url+f"lastfm/chart?username={username}&size={chart_size}&chart_type={chart_type}&timeperiod={timeperiod}&limit={limit}",headers={'api-key':self.__api_key}) as response:
                if response.status == 404:
                    return None
                return discord.File(fp=io.BytesIO(await response.read()),filename=f"{filename}.png")
