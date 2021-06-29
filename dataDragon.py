#!/usr/bin/env python
# coding: utf-8
import requests

class DataDragon():
    
    def __init__(self, version):
        self.version = version
    
    def getItensInfo(self):
        return requests.get("http://ddragon.leagueoflegends.com/cdn/"+self.version+"/data/pt_BR/item.json").json()
    
    def getItensId(self):
        self.response = requests.get("http://ddragon.leagueoflegends.com/cdn/"+self.version+"/data/pt_BR/item.json").json()
        self.itemNameById = {}
        for key,item in self.response['data'].items():
            if(key > 6695):
                break
            self.itemNameById[int(key)] = item['name']
            
        return self.itemNameById
    
    def getChampionsInfo(self):
        return requests.get("http://ddragon.leagueoflegends.com/cdn/"+self.version+"/data/pt_BR/champion.json").json()
    
    def getChampId(self):
        self.response = requests.get("http://ddragon.leagueoflegends.com/cdn/"+self.version+"/data/pt_BR/champion.json").json()
        self.championId = {}
        for i in self.response['data']:
            iD = self.response['data'][i]['id']
            key = self.response['data'][i]['key']
            self.championNameById[int(key)] = iD
            
        return self.championId