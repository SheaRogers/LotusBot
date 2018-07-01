import requests
import json


class Getter():
    def getStatus(self):
        r = requests.get(url=' https://api.warframestat.us/pc')
        return r.json()

    def getAlerts(self):
        r = Getter().getStatus()
        ret = ''

        for item in r['alerts']:
            ret += "There is an alert for " + item['rewardTypes'] + '\n'
        return ret
