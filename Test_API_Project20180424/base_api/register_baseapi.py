from base import BaseApi
class RegisterBase(BaseApi):
    url = "/register/"

    def __init__(self, reg_email, reg_password,exa_password, *args, **kwargs):
        super(RegisterBase, self).__init__(*args, **kwargs)
        self.reg_email = reg_email
        self.reg_password = reg_password
        self.exa_password = exa_password

    # 对BaseApi类中build_custom_param方法重写,传入用户名密码等其他参数
    def build_custom_param(self, data):
        return {'reg_email': data['reg_email'], 'reg_password': data['reg_password'], 'exa_password': data['exa_password']}