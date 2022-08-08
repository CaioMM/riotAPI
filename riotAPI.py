#!/usr/bin/env python
# coding: utf-8
import requests

class MatchAPI():
    """
    Class for access riot Match API
    parameters:
    region = americas, asia or europe
    version = api version
    apiKey = dev api_key for access
    """
    def __init__(self, region='americas', version='v5', apiKey=''):
        self.region = region
        self.version = version
        self.apiKey = apiKey
        self.headers = {"X-Riot-Token": self.apiKey}
    
    def setUrl(self):
        """
        Set baser URL to api access
        """
        return f'https://{self.region}.api.riotgames.com/lol/match/{self.version}/matches/'

    def playerHistory(self,puuid,queue,start,count):
        """
        Request for player match history
        """
        self.response = requests.get(self.setUrl()+'by-puuid/'+puuid+'/ids?queue='+str(queue)+'&start='+str(start)+'&count='+str(count),headers=self.headers)
        return self.response.json()

    def matchInfo(self,matchId):
        """
        Request specific match information
        """
        self.response = requests.get(self.setUrl()+matchId,headers=self.headers)
        return self.response.json()

    def timeLine(self,matchId):
        """
        Request timeline of specific match
        """
        self.response = requests.get(self.setUrl()+matchId+'/timeline',headers=self.headers)
        return self.response.json()

class LeagueAPI():
    """
    Class for access riot Match API
    parameters:
    region = br1, eun1, euw1, jp1, kr, la1, la2, na1, oc1, ru, tr1
    version = api version
    apiKey = dev api_key for access
    """
    def __init__(self, region, version, apiKey):
        self.region = region
        self.version = version
        self.apiKey = apiKey
        self.headers = {"X-Riot-Token": self.apiKey}

    def setUrl(self):
        """
        Set baser URL to api access
        """
        return f'https://{self.region}.api.riotgames.com/lol/league/{self.version}/'

    def challengerLeagues(self, queue):
        """
        return challengers players
        queue: RANKED_SOLO_5x5, RANKED_FLEX_SR, RANKED_FLEX_TT
        """
        self.response = requests.get(self.setUrl()+'challengerleagues/by-queue/'+queue,headers=self.headers)
        return self.response.json()

    def entriesBySummoner(self,encryptedSummonerId):
        """
        return information of specific summoner
        encryptedSummonerId: id of summoner (string)
        """
        self.response = requests.get(self.setUrl()+'entries/by-summoner/'+encryptedSummonerId,headers=self.headers)
        return self.response.json()

    def entries(self,queue,tier,division):
        """
        return information of summoners in an specific tier division queue
        Get all the league entries
        queue: RANKED_SOLO_5x5, RANKED_FLEX_SR, RANKED_FLEX_TT
        tier: DIAMOND, PLATINUM, GOLD, SILVER, BRONZE, IRON
        division: I, II, III, IV
        """
        self.response = requests.get(self.setUrl()+'entries/'+queue+'/'+tier+'/'+division+'?page=1',headers=self.headers)
        return self.response.json()

    def grandMasterLeagues(self, queue):
        """
        return grandmaster players
        queue: RANKED_SOLO_5x5, RANKED_FLEX_SR, RANKED_FLEX_TT
        """
        self.response = requests.get(self.setUrl()+'grandmasterleagues/by-queue/'+queue,headers=self.headers)
        return self.response.json()

    def leagues(self, leagueId):
        """
        return league info by league id
        leagueId: id of league (string)
        """
        self.response = requests.get(self.setUrl()+'leagues/'+leagueId,headers=self.headers)
        return self.response.json()

    def masterLeagues(self, queue):
        """
        return master players
        queue: RANKED_SOLO_5x5, RANKED_FLEX_SR, RANKED_FLEX_TT
        """
        self.response = requests.get(self.setUrl()+'masterleagues/by-queue/'+queue,headers=self.headers)
        return self.response.json()

class SummonerAPI():
    """
    Class for access riot Summoner API
    parameters:
    region = br1, eun1, euw1, jp1, kr, la1, la2, na1, oc1, ru, tr1
    version = api version
    apiKey = dev api_key for access
    """
    def __init__(self, region, version, apiKey):
        self.region = region
        self.version = version
        self.apiKey = apiKey
        self.headers = {"X-Riot-Token": self.apiKey}

    #/lol/summoner/v4/summoners/by-account/{encryptedAccountId}
    def setUrl(self):
        """
        Set baser URL to api access
        """
        return f'https://{self.region}.api.riotgames.com/lol/summoner/{self.version}/'

    def byAccount(self,encryptedAccountId):
        """
        return summoner info by encrypted account id
        encryptedAccountId: encrypted account id (string)
        """
        self.response = requests.get(self.setUrl()+'summoners/by-account/'+encryptedAccountId,headers=self.headers)
        return self.response.json()

    def byName(self,summonerName):
        """
        return summoner info by summoner name
        summonerName: summoner name (string)
        """
        self.response = requests.get(self.setUrl()+'summoners/by-name/'+summonerName,headers=self.headers)
        return self.response.json()

    def byPUUID(self,encryptedPUUID):
        """
        return summoner info by encryptedPUUID
        encryptedPUUID: encrypted PUUID (string)
        """
        self.response = requests.get(self.setUrl()+'summoners/by-puuid/'+encryptedPUUID,headers=self.headers)
        return self.response.json()

    def bySummonerID(self,encryptedSummonerId):
        """
        return summoner info by encrypted Summoner Id
        encryptedSummonerId: encrypted Summoner Id (string)
        """
        self.response = requests.get(self.setUrl()+'summoners/'+encryptedSummonerId,headers=self.headers)
        return self.response.json()

    