## 使用docker-compose启动portia

- 参考
    - [[可视化抓取]portia2.0尝鲜体验以及自动化畅想-数据输出以及原理分析](http://brucedone.com/archives/1059)
    
- 步骤
    - 创建目录
        - mkdir -p portia/compose
        - mkdir -p portia/run
    - 新建portia/compose/docker-compose.yml
```yaml
portia:
    image: scrapinghub/portia
    ports:
        - 9001:9001
    volumes:
        - /Users/play/Study/2018/portia/run:/app/data/projects
```    
   - 启动
        - cd portia/compose/
        - docker-compose up
        - 在浏览器输入 http://127.0.0.1:9001/
