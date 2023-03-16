import aiohttp,asyncio,orjson,typing,discord

class RivalAPI(object):
    def __init__(self, api_key):
        self.__api_key = api_key
        self.base_url = 'https://api.rival.rocks/'

    async def request(self,method:str,endpoint:str,params:typing.Any):
        async with aiohttp.ClientSession(headers={'api-key':self.__api_key}) as session:
            if method == "get":
                async with session.get(self.base_url+endpoint+params,headers={'api-key':self.__api_key}) as response:
                    return await response.json()
            elif method == "post":
                async with session.post(self.base_url+endpoint,params=params,headers={'api-key':self.__api_key}) as response:
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
        return await self.request(method="get",endpoint="tiktok/userinfo"params=f"?username={username}")
            
    async def medal(self,url:str):
        return await self.request(method="get",endpoint="medal",params=f"?url={url}")
    
    async def twitter_userinfo(self,username:str):
        return await self.request(method="get",endpoint="twitter/user",params=f"?username={username}")
    
    async def twitter_post(self,url:str):
        return await self.request(method='get',endpoint='twitter/post',params=f'?url={url}')
    
    async def twitch(self,username:str):
        return await self.request(method='get',endpoint='twitch',params=f'?username={username}')
    
    async def google_images(self,query:str,safe:bool=False):
        return await self.request(method='post',endpoint='google/images',params={'query':query,'safe':f'{safe}'})
    
    async def google_search(self,query:str,safe:bool=False):
        return await self.request(method='post',endpoint='google/search',params={'query':query,'safe':f'{safe}'})
    
    async def weheartit_userinfo(self,username:str):
        return await self.request(method='get',endpoint='weheartit/user',params=f"?username={username}")
    
    async def media_color(self,url:str):
        return await self.request(method='get',endpoint='media/color',params=f'?url={url}')
    
    async def media_ocr(self,url:str):
        return await self.request(method='get',endpoint='media/ocr',params=f'?url={url}')
    
    async def oxford(self,word:str,type:str="american_english"):
        return await self.request(method='get',endpoint='oxford',params=f"?word={word}&type={type}")
    
    async def lastfm_chart(self,username:str,filename:str="lastfm",size:str="3x3",chart_type:str="album",timeperiod:str="alltime",limit:int=15)
        async with aiohttp.ClientSession() as session:
            async with session.get(self.base_url+f"lastfm/chart?username={username}&chart_type={chart_type}&timeperiod={timeperiod}&limit={limit}",headers={'api-key':self.__api_key}) as response:
                return discord.File(fp=io.BytesIO(await response.read()),filename=f"{filename}.png")