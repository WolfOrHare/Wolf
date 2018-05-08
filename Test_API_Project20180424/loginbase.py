import requests,settings,json

class LoginApi(object):
    url = '/login_check/'
    username = 'test1'
    password = '1'


    base_url = settings.TEST_BASE_URL
    def __init__(self):
        self.url_params = []
        self.base_url = self.base_url
        self.email = self.username
        self.password = self.password
        print("LoginBase")

    def post(self,data):

        # 增加固定参数
        bbp = self.build_base_param()
        # 增加其他参数
        # bcp = self.build_custom_param(data)

        # 更新到data里
        data.update(bbp)
        # data.update(bcp)


        self.response = requests.post(self.api_url(), data,headers=settings.HEADERS)
        return self.response

    def get(self,data):
        if not data:
            data = {}
        # 增加固定参数
        bbp = self.build_base_param()
        # 增加其他参数
        bcp = self.build_custom_param(data)

        # 更新到data里
        data.update(bbp)
        data.update(bcp)

        self.response = requests.get(self.api_url(),data,headers = settings.HEADERS)
        return self.response

    # 不常用，先写上，有点像数据库的增删改查。
    def put(self):
        requests.put()
        return self.response

    def head(self):
        requests.head()
        return self.response

    def delete(self):
        requests.delete()
        return self.response

    def options(self):
        requests.options()
        return self.response

    def api_url(self):
        if not self.url:
            raise RuntimeError("no url been set")
        # print("test urlname is %s" % self.url)
        return self._get_url(self.url)

    # 返回测试用的link
    def _get_url(self,url):
        format_url = url.format(*self.url_params)
        print("test1 url is :" ,"{0}{1}".format(self.base_url,format_url))
        return "{0}{1}".format(self.base_url,format_url)

    # 获取响应状态码
    def get_code(self):
        if self.response:
            print(json.loads(self.response.text))
            return json.loads(self.response.text)

    # 获取http状态码
    def get_status_code(self):
        if self.response:
            print(self.response.status_code)
            return self.response.status_code

    # 获取消息状态码
    def get_response_massge(self):
        if self.response:
            print(json.loads(self.response.text)['msg'])
            return json.loads(self.response.text)['msg']

    # 增加固定参数
    def build_base_param(self):
        return {
            # "version":settings.VERSION,
            "version": "",
            "token":""
        }

    # 增加通用参数外的其他参数
    def build_custom_param(self,data):
        return {"":""

        }