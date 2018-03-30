## 介绍Puppeteer和无头Chrome
- https://dev.to/mohamed3on/an-introduction-to-puppeteer-and-headless-chrome

Headless Chrome是Chrome 59（Linux和Mac）和Chrome 60（Windows）中新发布的功能。它允许以编程方式测试网站而无需启动浏览器窗口，从而使自动化测试变得更加容易，从而让您更有信心地在不破坏任何内容的情况下更改您的应用。

首先，什么是“无头”？
无头基本上意味着'没有GUI'，这意味着在Chrome的情况下，你会使用可编程API，而不是可以与GUI交互的GUI。Headless模式的一个很好的例子就是当你使用SSH处理服务器时，以及使用shell命令进行所有交互。

利用无人机与木偶一起使用
Puppeteer是由Chrome团队制作的一款npm套装软件，可通过便捷的高级API轻松与无头Chrome进行互动。
这是一个新发布的模块，它与PhantomJS或Selenium非常相似，但是它使用最新版本的Chrome和使用无头模式作为默认模式。

您可以使用无头Chrome和Puppeteer运行哪种测试？
Puppeteer的一个很好的用例是为你的UI自动测试，截取它的截图或者将它导出为PDF。
由于无头版Chrome可以让您执行普通浏览器的任何操作，因此您可以使用它来自动执行系统的整个使用案例（端到端测试）。例如，用户登录，表单提交，按钮点击，页面导航等。
您还可以使用Puppeteer定期抓取网站，并将您想要提取的相关信息存储在数据库中，这与您使用Python的美味汤包完成的操作类似。

包起来
总而言之，Puppeteer是一个软件包，允许您以自动的方式编程处理网页，无论是截取网页截图，还是将其导出为PDF，或者单击按钮并填写表单，或者提取/刮取页面的内容供以后检查。它为您提供了一个非常强大的API，可让您在完整的浏览器中执行任何操作，而无需使用浏览器。
如果您有兴趣并想了解更多关于无头Chrome的信息，请查看本文。
如果你想看看如何使用木偶匠的例子，请点击这里。
