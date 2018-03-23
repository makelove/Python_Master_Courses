## Frontera 最好的scrapy 分布式框架

- https://github.com/scrapinghub/frontera
- https://www.jianshu.com/p/ff8846ad0e94

- Frontera是一个由抓取前沿和分发/缩放原语组成的网络抓取框架，允许构建大规模的在线网络爬虫。

- Frontera负责在爬网过程中遵循的逻辑和策略。它存储和优先搜寻由抓取工具提取的链接，以决定下一个要访问的页面，并且能够以分布的方式进行。

- 主要特点
在线操作：小批量请求，在提取后立即执行解析。
可插入的后端架构：将低级存储逻辑与爬网策略分开。可定制抓取策略，
三种运行模式：单进程，分布式蜘蛛，分布式后端和蜘蛛。
透明的数据流，允许使用Kafka轻松集成自定义组件。
消息总线抽象，提供一种实现自己的传输的方法（开箱即用的ZeroMQ和Kafka）。使用 ZeroMQ and Kafka 为分布式爬虫实现消息总线，
RDBMS和HBase后端。集成 SQLAlchemy 支持关系型数据库（Mysql， PostgreSQL， sqlite 等等）， 集成 HBase 非常好得支持键值对数据库，
用RDBMS重新审视逻辑。
可选使用Scrapy进行读取和解析。Scrapy易于集成，

使用 Graph Manager 创建伪站点地图和模拟抓取，进行精确抓取逻辑调优。
透明的传输层概念(message bus)和通信协议，

3子句BSD许可证，允许用于任何商业产品。
Python 3支持。