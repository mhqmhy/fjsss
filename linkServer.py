import requests
import re
import json

class LoginAccount():
    def __init__(self):
        self.account = {
            "username": "SheepHuan",
            "password": "xx"
        }
        self.token=''
        self.user_id=''
    def login(self,account): #登陆
        # account=self.account
        headers = {
            "Content-Type": 'application/json',
            "User-Agent": 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Mobile Safari/537.36'
        }
        response = requests.post('https://api.shisanshui.rtxux.xyz/auth/login', json.dumps(account), headers=headers)
        reData = json.loads(response.text)
        # if isinstance(reData["data"],str) and reData["data"]=='xyz.rtxux.game.shisanshui.exception.AppException: Username or password not match':#返回了错误
        #     self.signIn(account)
        # elif isinstance(reData["data"],str):
        #     print('Web Error:',reData["data"])
        #     return
        try:
            self.token = reData["data"]["token"]
            print(self.token,'登录成功')
            self.account=account
            return 'OK'
        except:
            print('Web Error',reData["data"])
    def signIn(self,account):
        headers = {
            "Content-Type": 'application/json',
            "User-Agent": 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Mobile Safari/537.36'
        }
        response = requests.post('https://api.shisanshui.rtxux.xyz/auth/register', json.dumps(account), headers=headers)
        reData = json.loads(response.text)
        print(reData)
        if reData["data"]["msg"] == "Success":
            # 注册成功
            try:
                self.user_id = reData["data"]["user_id"]
                print(self.user_id, '注册成功')
                self.account = account
                return 'OK'
            except:
                print('Web Error',reData["data"])
            # self.login(account)

    def check(self): #验证登陆信息
        if self.token == '':
            self.login(self.account)
        if self.user_id=='':
            headers = {
                "X-Auth-Token": '',
                "User-Agent": 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Mobile Safari/537.36'
            }
            headers["X-Auth-Token"] = self.token
            response = requests.get('https://api.shisanshui.rtxux.xyz/auth/validate', headers=headers)
            reData=json.loads(response.text)
            self.user_id=reData["data"]["user_id"]
        dic={}
        dic["account"]=self.account
        dic["token"]=self.token
        dic["user_id"]=self.user_id
        return dic

    def loginOut(self):
        headers = {
            "X-Auth-Token": '',
            "User-Agent": 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Mobile Safari/537.36'
        }
        headers["X-Auth-Token"] = self.token
        response = requests.post('https://api.shisanshui.rtxux.xyz/auth/logout', headers=headers)
        print(response.text)

class Game():
    def __init__(self):
        pass
    def openGame(self,token):
        headers = {
            "X-Auth-Token": '',
            "User-Agent": 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Mobile Safari/537.36'
        }
        headers["X-Auth-Token"] = token
        response = requests.post('https://api.shisanshui.rtxux.xyz/game/open', headers=headers)
        print(response.text)
    def historyList(self,token):
        headers = {
            "X-Auth-Token": '',
            "User-Agent": 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Mobile Safari/537.36'
        }
        headers["X-Auth-Token"] = token
        response = requests.get('https://api.shisanshui.rtxux.xyz/history', headers=headers)
        print(response.text)

if __name__=="__main__":
    account = {
        "username": "SheepHuan",
        "password": "GoodJob"
    }
    a=LoginAccount()
    a.login(account)


