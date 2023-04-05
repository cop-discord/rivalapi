API Wrapper for https://api.rival.rocks
A key is required for all endpoints other then uwuify
To install you need [git](https://git-scm.com/downloads) installed. After installing it, run
```shell
pip install git+https://github.com/cop-discord/rivalapi.git
```

| Function     | Arguments | Description   |
| ------------- | ------------- | ------------- |
| user | user_id | URL to the source image |
| tags | None | get tags | 
| twitter_userinfo | username  | get a twitter user lookup |
| twitter_post | url | get a twitter post's information | 
| uwuify | text | uwuify text |
| tiktok | url | get a tiktok post's information |
| tiktok_userinfo | username | get a tiktok user lookup |
| medal | url | get a medal clip lookup |
| twitch | username | get user information on a twitch account |
| google_images | query,safe(boolean) | get a google image search request |
| google_search | query,safe(boolean) | get a google search request |
| weheartit_userinfo | username | get a weheartit account's statistics |
| media_color | url | get an image's dominant color |
| media_ocr | url | get text output from an image |
| oxford | word,type | get a word's definition |
| lastfm_chart | username,filename,size,chart_type,timeperiod,limit | get a lastfm chart of a specific lastfm user |

### Code Example:
```python
from rivalapi import RivalAPI

rival = RivalAPI("YOUR-API-KEY")
await rival.weheartit_userinfo(username="perv")
```
