/**
 * Created by play on 2018/4/10.
 */
var context;
// 初始化
function init() {
    if (typeof qt != 'undefined') {
        new QWebChannel(qt.webChannelTransport, function (channel) {
                context = channel.objects.pyjs;
            }
        );
    }
    else {
        alert("qt对象获取失败！");
    }
}
// 向qt发送消息
function sendMessage(msg) {
    if (typeof context == 'undefined') {
        alert("context对象获取失败！");
    }
    else {
        context.onMsg(msg);
    }
}
// 控件控制函数
function onBtnSendMsg() {
    var cmd = document.getElementById("待发送消息").value;
    sendMessage(cmd);
}
init();
