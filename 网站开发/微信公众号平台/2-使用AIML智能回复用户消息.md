## 2-使用AIML智能回复用户消息

- 视频：https://www.bilibili.com/video/av21321653/

- 文档 
    - 接收普通消息 https://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1421140453
    - 被动回复用户消息 https://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1421140543
- AIML
    - 全名为Artificial Intelligence Markup Language（人工智能标记语言），是一种创建自然语言软件代理的XML语言，是由Richard Wallace和世界各地的自由软件社区在1995年至2002年发明的。
    - https://www.pandorabots.com/pandora/pics/wallaceaimltutorial.html
    - 下载英文语料
        - https://code.google.com/archive/p/aiml-en-us-foundation-alice/#!
        - pip install aiml 
```python
def load_aiml():
    cur_dir = os.getcwd()
    os.chdir('/home/xx/mysite/alice')
    alice = aiml.Kernel()
    alice.learn("startup.xml")
    alice.respond('LOAD ALICE')
    os.chdir(cur_dir)
    return alice
    
@app.route('/weixin', methods=['POST'])
def reply():
    if request.method == 'POST':
        data = request.data
        soup = BeautifulSoup(data, "xml")
        fromuser = soup.FromUserName.text
        touser = soup.ToUserName.text
        frommsgtype = soup.MsgType.text
        msgid = soup.MsgId.text
        curtime = str(int(time.time()))

        if "text" == frommsgtype:
            Content = soup.Content.text.strip()
            # print '是否英文:',Content.replace(' ','').isalpha()
            if re.match('\w+', Content):
                respond = alice.respond(Content)
    
```        
- 参考
    - https://www.biaodianfu.com/python-aiml.html