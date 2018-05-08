from base import BaseApi
from loginbase import LoginApi


class LoginBaseApi(LoginApi):

    def __init__(self, *args, **kwargs):
        super(LoginBaseApi, self).__init__(*args, **kwargs)
        self.email = self.email
        self.password = self.password
        self.data = {'email': self.email, 'password': self.password}

    def build_base_param(self):
        base_param = super(LoginBaseApi, self).build_base_param()
        response = LoginApi().post(self.data)
        base_param['token'] = response.token
        return base_param

    # def post(self,data):
    #     return {'reg_email': data['reg_email'], 'reg_password': data['reg_password'], 'exa_password': data['exa_password']}

