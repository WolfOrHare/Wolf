import settings
import requests
from unittest.case import TestCase


class TestAppPost(TestCase):
    username = 'test1'
    password = '1'

    reg_username = '123'
    reg_password = '1'
    exa_password = '2'

    base_url = settings.TEST_BASE_URL
    url_login = '/login'
    url_params = []

    def test_app_post(self):
        print('**test start**!')
        # 登陆接口

        content_login={'email':self.username,'password':self.password}
        login_post = requests.post(self.api_url(),data = content_login)
        print(login_post)

        # 注册接口
        # url_register = '/register'
        # content_register = {'reg_email':self.reg_username,'reg_password':self.reg_password,'exa_password':self.exa_password}
        # register_post = requests.post(settings.TEST_BASE_URL+url_register,content_register)
        # print(register_post)
        #

    def api_url(self):
        if not self.url_login:
            raise RuntimeError("no url been set")
        print("test1 urlname is %s" % self.url_login)
        return self._get_url(self.url_login)

    def _get_url(self,url):
        format_url = url.format(*self.url_params)
        print("test url is :" ,"{0}{1}".format(self.base_url,format_url))
        return "{0}{1}".format(self.base_url,format_url)

    def get_code(self):
        print("")

    def tearDown(self):
        print("test stop!")