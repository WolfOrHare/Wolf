import settings
import requests,certifi,urllib3,json
from unittest.case import TestCase
import selenium

class  TestAppGet(TestCase):
    # 访问selenuim server，这里端口可以默认写4444
    # test_selenium = selenium("192.123.90.1", "4444", "*firefox", "http://www.baidu.com")
    # test_selenium.start()

    url = 'http://httpbin.org/cookies/set/sessioncookie/123456789'
    url2 = 'https://www.baidu.com'
    def test_app_get(self):
        print("start test get")
        # 如果是https的那就要加verify= True，否则会出现ssl证书验证的报错
        # rq = requests.get(url = self.url,verify = True)

        # 也可以这么写
        http = urllib3.PoolManager(
            cert_reqs='CERT_REQUIRED',
            ca_certs=certifi.where()
        )

        rq = http.request('GET',url=self.url2)

        print(rq)
    def tearDown(self):
        print("stop test get")