import settings,json
from base_api.login_baseapi import LoginBaseApi
from unittest.case import TestCase

class TestLoginApi(TestCase):
    username = 'test1'
    password = '1'
    data = {'email':username,'password':password}

    def test_login(self):
        print("**start test login**")

        loginbase = LoginBaseApi(email=self.username,password=self.password)
        loginbase.post(self.data)

        # 获取到链接状态
        status_cide = loginbase.get_status_code()
        self.assertEqual(status_cide,200)

        # 这里返回参数是ok，如果失败返回fail，不同请求接口返回参数不一样
        response_massge = loginbase.get_response_massge()
        self.assertEqual(response_massge,'ok')

        # # 返回参数中如果有结果，需要对比返回参数是否与入参一致
        # content = json.loads(self.response.content)['result']['content']
        # self.assertEqual(content['email'], self.username)

    def tearDown(self):
        print("stop test login")