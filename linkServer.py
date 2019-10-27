import json
import requests
import execjs

Pokedic = {"$2": 0, "0": "$2", "$3": 1, "1": "$3", "$4": 2, "2": "$4", "$5": 3, "3": "$5", "$6": 4, "4": "$6",
           "$7": 5,
           "5": "$7", "$8": 6, "6": "$8", "$9": 7, "7": "$9", "$10": 8, "8": "$10", "$J": 9, "9": "$J",
           "$Q": 10,
           "10": "$Q", "$K": 11, "11": "$K", "$A": 12, "12": "$A", "&2": 13, "13": "&2", "&3": 14, "14": "&3",
           "&4": 15,
           "15": "&4", "&5": 16, "16": "&5", "&6": 17, "17": "&6", "&7": 18, "18": "&7", "&8": 19, "19": "&8",
           "&9": 20,
           "20": "&9", "&10": 21, "21": "&10", "&J": 22, "22": "&J", "&Q": 23, "23": "&Q", "&K": 24, "24": "&K",
           "&A": 25,
           "25": "&A", "*2": 26, "26": "*2", "*3": 27, "27": "*3", "*4": 28, "28": "*4", "*5": 29, "29": "*5",
           "*6": 30,
           "30": "*6", "*7": 31, "31": "*7", "*8": 32, "32": "*8", "*9": 33, "33": "*9", "*10": 34, "34": "*10",
           "*J": 35,
           "35": "*J", "*Q": 36, "36": "*Q", "*K": 37, "37": "*K", "*A": 38, "38": "*A", "#2": 39, "39": "#2",
           "#3": 40,
           "40": "#3", "#4": 41, "41": "#4", "#5": 42, "42": "#5", "#6": 43, "43": "#6", "#7": 44, "44": "#7",
           "#8": 45,
           "45": "#8", "#9": 46, "46": "#9", "#10": 47, "47": "#10", "#J": 48, "48": "#J", "#Q": 49, "49": "#Q",
           "#K": 50,
           "50": "#K", "#A": 51, "51": "#A"}


def get_js():
    f = open("./main.js", 'r', encoding='utf-8')  # 打开JS文件
    x = f.readlines()
    f.close()
    htmlstr = ''
    for i in x:
        htmlstr += i
    return htmlstr


def get_des_psswd(hand):
    jsstr = get_js()
    ct = execjs.compile(jsstr)
    result = ct.call("optimize_hand", hand)
    return result

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
        response = requests.post('http://api.revth.com/auth/login', json.dumps(account), headers=headers)
        reData = json.loads(response.text)

        try:
            self.token = reData["data"]["token"]
            print(self.token,'登录成功')
            self.account=account
            return 'OK'
        except:
            print('Web Error',reData["data"])
    def signIn(self,account):#注册接口
        headers = {
            "Content-Type": 'application/json',
            "User-Agent": 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Mobile Safari/537.36'
        }
        response = requests.post('http://api.revth.com/auth/register', json.dumps(account), headers=headers)
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
            response = requests.get('http://api.revth.com/auth/validate', headers=headers)
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
        response = requests.post('http://api.revth.com/auth/logout', headers=headers)
        print(response.text)

class Game():
    def __init__(self):
        self.game_id=''
        self.pokes=[]
    def openGame(self,token):
        try:
            headers = {
                "X-Auth-Token": '',
                "User-Agent": 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Mobile Safari/537.36'
            }
            headers["X-Auth-Token"] = token
            response = requests.post('http://api.revth.com/game/open', headers=headers)
            reData=json.loads(response.text)
            self.game_id=reData["data"]["id"]
            pokes=reData["data"]["card"].split(' ')
            print('game-id:',reData["data"]["id"])
            return pokes
        except Exception as e:
            print('linkServer/Game()/opengame()',e)
            return None
    def submitPoke(self,token,pokes):
        cards=[]
        for i in pokes:
            cards.append(Pokedic[i])
        pokes=get_des_psswd(cards)
        cards.clear()
        for i in pokes:
            new = []
            for j in i :
                new.append(Pokedic[str(j)])
            cards.append(" ".join(new))

        headers = {
            "Content-Type":'application/json',
            "X-Auth-Token": token,
            "User-Agent": 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Mobile Safari/537.36'
        }
        dic={}
        dic["id"]=self.game_id
        dic["card"]=cards
        response = requests.post('http://api.revth.com/game/submit', json.dumps(dic),headers=headers)
        reData = json.loads(response.text)
        try:
            print('出牌成功',reData["data"]["msg"])
        except:
            print('Web Error',reData["data"])

class historyInfo():
    def __init__(self,token):
        self.token=token

    def update(self,id):
        pass


'5063'

if __name__=="__main__":
    account = {
        "username": "SheepHuan",
        "password": "yanghuan"
    }
    a=LoginAccount()
    a.login(account)


