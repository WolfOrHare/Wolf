from base import BaseApi
from loginbase import LoginApi


class LoginBaseApi(BaseApi):
    url = "/login_check/"

    def __init__(self, email,password, *args, **kwargs):
        super(LoginBaseApi, self).__init__(*args, **kwargs)
        self.email = email
        self.password = password

    def build_base_param(self):
        base_param = super(LoginBaseApi, self).build_base_param()
        # response = BaseApi().post(self.email ,self.password)
        # base_param['token'] = response.token
        return base_param

