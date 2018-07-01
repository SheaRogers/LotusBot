import requests
import os
import json


class StatusFuncs():
    def Alerts(self=None, alertType=None):
        """get alerts"""
        r = requests.get(url=' https://api.warframestat.us/pc')
        js = json.loads(r.text)
        res = ''
        if alertType is None:
            for item in js['alerts']:
                res += "There is an alert for " + item['rewardTypes'][0] + '\n'
        else:
            for item in js['alerts']:
                if item['rewardTypes'] == alertType:
                    res += "There is an alert for " + \
                        item['rewardTypes'] + '\n'
        return res
