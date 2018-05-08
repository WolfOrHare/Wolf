# ** encoding=utf-8 **
import settings
from base_api.register_baseapi import RegisterBase
from unittest.case import TestCase

class TestRegisterApi(TestCase):
    username = 'test3'
    password = '2'
    exa_password = '3'
    data = {'reg_email':username,'reg_password':password,'exa_password':exa_password}
    def test_register(self):
        print("**start test register**")

        registerbase = RegisterBase(reg_email=self.username,reg_password=self.password,exa_password=self.exa_password)
        # response做数据返回验证用
        response = registerbase.post(data=self.data)
        self.assertEqual(registerbase.get_status_code(),200)





    def tearDown(self):
        print("stop test register")