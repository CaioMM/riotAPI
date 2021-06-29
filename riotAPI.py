#!/usr/bin/env python
# coding: utf-8
import requests

class RiotAPI():
    
    def __init__(self,region,apiKey,version):
    
        self.region = region
        self.apiKey = apiKey
        self.version = version
        self.url = "https://"+self.region+".api.riotgames.com/lol/"
        
    def requestSummonerInfoByName(self, summonerName):
#         Retorna as informações do Invocador
        self.summonerName = summonerName
        self.response = requests.get(self.url+"summoner/"+self.version+"/summoners/by-name/"+self.summonerName+"?api_key="+self.apiKey)
#        self.summonerId = self.summonerInfo.json()['id']
#        self.accountId = self.summonerInfo.json()['accountId']
        return self.response.json()

    def requestSummonerInfoBySummonerId(self, summonerId):
#         Retorna as informações do Invocador
        self.summonerId = summonerId
        self.response = requests.get(self.url+"summoner/"+self.version+"/summoners/"+self.summonerId+"?api_key="+self.apiKey)
        return self.response.json()
    
    def requestCurrentGameInfo(self, summonerId):
#         Retorna informações da partida em curso
        self.summonerId = summonerId
        self.response = requests.get(self.url+"spectator/"+self.version+"/active-games/by-summoner/"+self.summonerId+"?api_key="+self.apiKey)
        return self.response.json()
    
    def requestMatchHistory(self, accountId, beginIndex=0,endIndex=0, queueId=0):
#         Retorna o histórico de partida do invocador
        self.accountId = accountId
        self.beginIndex = beginIndex
        self.endIndex = endIndex
        self.queueId = queueId
        
#         Caso o Id da fila seja definido
        if self.queueId != 0:
               self.response = request.get(self.url+"match/"+self.version+"/matchlists/by-account/"+self.accountId+"?queue="+self.queueId+"?api_key="+self.apiKey)
            
#         Caso o número de partidas solicitados seja definido
        if self.beginIndex == 0 and self.endIndex == 0:            
               self.response = requests.get(self.url+"match/"+self.version+"/matchlists/by-account/"+self.accountId+"?api_key="+self.apiKey)
        else:
               self.response = requests.get(self.url+"match/"+self.version+"/matchlists/by-account/"+self.accountId+"?endIndex="+str(self.endIndex)+"&beginIndex="+str(self.beginIndex)+"&api_key="+self.apiKey)
        return self.response.json()
    
    def requestSummonerRankedMatches(self, accountId):
#         Retorna todas as partidas rankeadas de um Jogador
        self.accountId = accountId
        self.queueId = 420
        self.response = requests.get(self.url+"match/"+self.version+"/matchlists/by-account/"+self.accountId+"?queue="+str(self.queueId)+"&api_key="+self.apiKey)
        
        return self.response.json()
        
    def requestMatchData(self, gameId):
#         Retorna as informações de uma partida
        self.gameId = gameId
        self.response = requests.get(self.url+"match/"+self.version+"/matches/"+str(self.gameId)+"?api_key="+self.apiKey)
        return self.response.json()
    
    def requestMatchTimeLine(self, gameId):
#         Retorna os eventos de uma partida
        self.gameId = gameId
        self.response = requests.get(self.url+"match/"+self.version+"/timelines/by-match/"+str(self.gameId)+"?api_key="+self.apiKey)
        return self.response.json()

    def requestChallengerRank(self):
#         Retorna os jogadores na divisão Desafiante na ordem em que estão rankeados
        self.response = requests.get(self.url+"league-exp/"+self.version+"/entries/RANKED_SOLO_5x5/CHALLENGER/I?page=1&api_key="+self.apiKey)
        return self.response.json()        

    def requestPlayerChampionsMastery(self, summonerId):
        self.summonerId = summonerId
        self.response = requests.get(self.url+"champion-mastery/"+self.version+"/champion-masteries/by-summoner/"+self.summonerId+"?api_key="+self.apiKey)
        return self.response.json()