from django.http import HttpResponse

# 配置路由，在插件提交返回中配置地址（如本例 http://127.0.0.1:8000）
# Create your views here.
from httpapi.HTTPSDK import *


def qq(request):
    # 传入值需要解码（兼容不同版本）
    sdk = HTTPSDK.httpGet(request.body)
    print(sdk.getMsg())
    # 字符编码问题
    sdk.sendPrivdteMsg(sdk.getMsg().QQ, '你发送了这样的消息：' + sdk.getMsg().Msg)
    sdk.getLoginQQ()

    # 回调演示，提交返回获取群列表、登录QQ等
    if sdk.isCallback() and sdk.getMsg().Type == HTTPSDK.TYPE_GET_LOGIN_QQ:
        print('Login QQ:' + str(sdk.getLoginQQ()))

    return HttpResponse(sdk.toJsonString(), content_type="application/json,charset=utf-8")
