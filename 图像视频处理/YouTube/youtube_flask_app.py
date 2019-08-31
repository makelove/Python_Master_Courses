# -*-coding:utf8-*-#

import base64,requests
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

DEVELOPER_KEY = 'xxx'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'
youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)
#
from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>YouTube搜索</title>
</head>
<body>
<div>
    <h1>YouTube搜索</h1>
    <div style="border:green solid 2px;">
        <form method="get" action="/search">
            <div><input size="40" name="keyword" type="text" placeholder="输入关键词"></div>
            <div>
                <button type="submit">搜索</button>
            </div>
        </form>
    </div>
</div>
</body>
</html>'''


@app.route('/search', methods=['GET'])
def youtube_search():

    # print('request.args',request.args)
    keyword = request.args.get('keyword', "")

    # Call the search.list method to retrieve results matching the specified
    # query term.
    search_response = youtube.search().list(
        q=keyword,
        part='id,snippet',
        maxResults=10
    ).execute()
    html = '''<head>
    <meta charset="UTF-8">
    <title>搜索结果</title>
</head>
<div>
        <h2>搜索结果</h2>
        <ul>'''
    for item in search_response.get('items', []):
        channelTitle = item['snippet']['channelTitle']
        title = item['snippet']['title']
        description = item['snippet']['description']
        publishedAt = item['snippet']['publishedAt']

        video_url = 'https://www.youtube.com/watch?v=' + item['id'].get('videoId','')
        image_url = item['snippet']['thumbnails']['high']['url']#https://i.ytimg.com/vi/mdViOV3tsUo/hqdefault.jpg
        try:
            rs=requests.get(image_url)
            base64_data = base64.b64encode(rs.content)
            img_url='data:image/jpg;base64,'+base64_data.decode()
        except:
            img_url=image_url

        html += '''
            <li>
                <div style="border:green solid 2px;">
                    <div>频道:'''+channelTitle+'''</div>
                    <div>标题:'''+title+'''</div>
                    <div>描述:'''+description+'''</div>
                    <div>发布时间:'''+publishedAt+'''</div>
                    <div><a href="'''+video_url+'''" target="_blank">
                        <img src="'''+img_url+'''">
                    </a></div>
                </div>
            </li>
        '''

    html += '''</ul>
    </div>'''
    return html


if __name__ == '__main__':
    app.run(debug=True)
