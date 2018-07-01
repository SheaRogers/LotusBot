import requests
import os
import json


class StatusFuncs():
    def Alerts(self=None, alertType=None):
        """get alerts"""
        r = requests.get(url=' https://api.warframestat.us/pc/alerts')
        js = json.loads(r.text)
        res = ''
        if alertType is None:
            res += 'There are ' + \
                str(len(js)) + ' alerts right now:\n'
            for item in js:
                res += "- " + \
                    item['mission']['reward']['asString'] + \
                    " with " + item['eta'] + " remaining\n"
        else:
            res += 'Here are the alerts for ' + \
                alertType + ' right now:\n'
            for item in js:
                if alertType in item['rewardTypes'][0]:
                    res += "- " + \
                        item['mission']['reward']['asString'] + \
                        " with " + item['eta'] + " remaining\n"
            if res == 'Here are the alerts for ' + alertType + ' right now:\n':
                res = 'There are no alerts for ' + alertType + ' right now.'
        return res

    def Sortie(self=None):
        """get sorties"""
        r = requests.get(url=' https://api.warframestat.us/pc/sortie')
        js = json.loads(r.text)
        res = ''
        res += 'Here are the details for the current sortie missions:\n'
        for item in js['sortie']['variants']:
            res += "- " + \
                item['missionType'] + \
                " | " + item['modifier'] + " | " + item['node'] + "\n"
        return res
