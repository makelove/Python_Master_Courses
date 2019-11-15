- 官网
    - https://mitmproxy.org/
    - 文档 https://docs.mitmproxy.org/stable/
- 安装
    - brew install mitmproxy
    - pip install mitmproxy

- 执行
    - mitmproxy -p 8888
    - 定制
        - mitmproxy -s demo1.py -p 8888
    - 先执行 mitmweb
        - 自动打开浏览器 http://127.0.0.1:8081/#/flows
        - 用curl测试
            - curl -x 127.0.0.1:8888 https://httpbin.org/ip
                - 需要安装HTTPS证书
                - curl -x 127.0.0.1:8888 -k https://httpbin.org/ip
            - curl -x 127.0.0.1:8888 http://httpbin.org/ip
                - 不需要
            - curl -x 127.0.0.1:8888 -k https://ip.cn

- 安装手机证书
    - 文档 https://docs.mitmproxy.org/stable/concepts-certificates/
    - mitmweb -p 8888
    - 手机设置代理 
        - 浏览器打开 mitm.it
        - 安装
        - 信任
        
- 定制        


    
```bash
(.py3) pro:~ play$ mitmproxy -h
usage: mitmproxy [options]

optional arguments:
  -h, --help            show this help message and exit
  --version             show version number and exit
  --options             Show all options and their default values
  --commands            Show all commands and their signatures
  --confdir PATH        Path to the mitmproxy config directory
  --set option[=value]  Set an option. When the value is omitted, booleans are
                        set to true, strings and integers are set to None (if
                        permitted), and sequences are emptied. Boolean values
                        can be true, false or toggle.
  -q, --quiet           Quiet.
  -v, --verbose         Increase log verbosity.
  --mode MODE, -m MODE  Mode can be "regular", "transparent", "socks5",
                        "reverse:SPEC", or "upstream:SPEC". For reverse and
                        upstream proxy modes, SPEC is host specification in
                        the form of "http[s]://host[:port]".
  --no-anticache
  --anticache           Strip out request headers that might cause the server
                        to return 304-not-modified.
  --no-showhost
  --showhost            Use the Host header to construct URLs for display.
  --rfile PATH, -r PATH
                        Read flows from file.
  --scripts SCRIPT, -s SCRIPT
                        Execute a script. May be passed multiple times.
  --stickycookie FILTER
                        Set sticky cookie filter. Matched against requests.
  --stickyauth FILTER   Set sticky auth filter. Matched against requests.
  --save-stream-file PATH, -w PATH
                        Stream flows to file as they arrive. Prefix path with
                        + to append.
  --no-anticomp
  --anticomp            Try to convince servers to send us un-compressed data.
  --console-layout {horizontal,single,vertical}
                        Console layout.
  --no-console-layout-headers
  --console-layout-headers
                        Show layout component headers

Proxy Options:
  --listen-host HOST    Address to bind proxy to.
  --listen-port PORT, -p PORT
                        Proxy service port.
  --no-server, -n
  --server              Start a proxy server. Enabled by default.
  --ignore-hosts HOST   Ignore host and forward all traffic without processing
                        it. In transparent mode, it is recommended to use an
                        IP address (range), not the hostname. In regular mode,
                        only SSL traffic is ignored and the hostname should be
                        used. The supplied value is interpreted as a regular
                        expression and matched on the ip or the hostname. May
                        be passed multiple times.
  --tcp-hosts HOST      Generic TCP SSL proxy mode for all hosts that match
                        the pattern. Similar to --ignore, but SSL connections
                        are intercepted. The communication contents are
                        printed to the log in verbose mode. May be passed
                        multiple times.
  --upstream-auth USER:PASS
                        Add HTTP Basic authentication to upstream proxy and
                        reverse proxy requests. Format: username:password.
  --proxyauth SPEC      Require proxy authentication. Format: "username:pass",
                        "any" to accept any user/pass combination, "@path" to
                        use an Apache htpasswd file, or
                        "ldap[s]:url_server_ldap:dn_auth:password:dn_subtree"
                        for LDAP authentication.
  --no-rawtcp
  --rawtcp              Enable/disable experimental raw TCP support. TCP
                        connections starting with non-ascii bytes are treated
                        as if they would match tcp_hosts. The heuristic is
                        very rough, use with caution. Disabled by default.
  --no-http2
  --http2               Enable/disable HTTP/2 support. HTTP/2 support is
                        enabled by default.

SSL:
  --certs SPEC          SSL certificates of the form "[domain=]path". The
                        domain may include a wildcard, and is equal to "*" if
                        not specified. The file at path is a certificate in
                        PEM format. If a private key is included in the PEM,
                        it is used, else the default key in the conf dir is
                        used. The PEM file should contain the full certificate
                        chain, with the leaf certificate as the first entry.
                        May be passed multiple times.
  --no-ssl-insecure
  --ssl-insecure, -k    Do not verify upstream server SSL/TLS certificates.

Client Replay:
  --client-replay PATH, -C PATH
                        Replay client requests from a saved file. May be
                        passed multiple times.

Server Replay:
  --server-replay PATH, -S PATH
                        Replay server responses from a saved file. May be
                        passed multiple times.
  --no-server-replay-kill-extra
  --server-replay-kill-extra
                        Kill extra requests during replay.
  --no-server-replay-nopop
  --server-replay-nopop
                        Don't remove flows from server replay state after use.
                        This makes it possible to replay same response
                        multiple times.

Replacements:
  --replacements PATTERN, -R PATTERN
                        Replacement patterns of the form
                        "/pattern/regex/replacement", where the separator can
                        be any character. May be passed multiple times.

Set Headers:
  --setheaders PATTERN, -H PATTERN
                        Header set pattern of the form
                        "/pattern/header/value", where the separator can be
                        any character. May be passed multiple times.

Filters:
  See help in mitmproxy for filter expression syntax.

  --intercept FILTER    Intercept filter expression.
  --view-filter FILTER  Limit the view to matching flows.

```    
