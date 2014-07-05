### pocket.py ---
##
## Filename: pocket.py
## Author: Fred Qi
## Created: 2014-07-05 13:17:06(+0400)
##
## Last-Updated: 2014-07-05 22:47:51(+0400) [by Fred Qi]
##     Update #: 13
######################################################################
##
### Commentary:
##
##
######################################################################
##
### Change Log:
##
##
######################################################################

import os
import os.path
import json
import urllib2

def request_auth(consumer_key):
    headers = {'Content-Type' : 'application/json; charset=UTF-8',
               'X-Accept': 'application/json'}

    payload = {'consumer_key': consumer_key,
               'redirect_uri': 'pocketapp29509:authorizationFinished' }

    request_data = json.dumps(payload)

    # url = "https://getpocket.com/v3/oauth/authorize"
    url = 'https://getpocket.com/v3/oauth/request'

    response_data = makeRequest(headers, request_data, url)
    return response_data['code']

def makeRequest(headers, data, url):
    request = urllib2.Request(url, data, headers)
    response = urllib2.urlopen(request)
    data = json.load(response)
    return data


class pocket:
    """Wrapper for pocket access."""

# '29509-32d79c608f247b164bd57d00',
# '2703223d-08bb-0a3e-d80f-c44032'
    def __init__(self):
        self.url_add = 'https://getpocket.com/v3/add'
        self.url_mod = 'https://getpocket.com/v3/send'
        self.url_get = 'https://getpocket.com/v3/get'
        pass

    def _make_request(self, req_headers, req_data, req_url):
        request = urllib2.Request(req_url, req_data, req_headers)
        response = urllib2.urlopen(request)
        data = json.load(response)
        return data

    def load_token(self, filename='.pocket-token.json'):
        """Read the token for accessing pocket."""
        homepath = os.getenv('HOME')
        filename = os.path.join(homepath, filename)
        token_file = open(filename, 'r')
        token = json.load(token_file)
        token_file.close()
        self.consumer_key = token['consumer_key']
        self.access_token = token['access_token']

    def save_token(self, filename='.pocket-token.json'):
        # self.consumer_key = '29509-32d79c608f247b164bd57d00'
        # self.access_token = '2703223d-08bb-0a3e-d80f-c44032'
        token = {'consumer_key': self.consumer_key,
                 'access_token': self.access_token}
        homepath = os.getenv('HOME')
        filename = os.path.join(homepath, filename)
        token_file = open(filename, 'w')
        json.dump(token, token_file)
        token_file.close()
        
    
    def retrieve_favorite(self):
        """Download the list of pocket favorite URLs."""
        # access_token = '2703223d-08bb-0a3e-d80f-c44032'
        header = {'Content-Type': 'application/json'}
        payload = {'consumer_key': self.consumer_key,
                   'access_token': self.access_token,
                   'favorite': 1,
                   'detailType': 'simple' }
        req_data = json.dumps(payload)
        favorite = self._make_request(header, req_data, self.url_get)
        
        return favorite

    def modify_items(self, itemids, actions):
        header = {'Content-Type': 'application/json'}
        action_data = None
        if hasattr(actions, '__iter__'):
            action_data = [{'item_id': itemid, 
                            'action': act}
                           for itemid, act in zip(itemids, actions)]
        elif type(actions) is str:
            action_data = [{'item_id': itemid, 
                            'action': actions} for itemid in itemids]
            
        payload = {'consumer_key': self.consumer_key,
                   'access_token': self.access_token,
                   'actions': action_data}
        req_data = json.dumps(payload)
        response = self._make_request(header, req_data, self.url_mod)
        return response

    def extract_title_url(self, item):
        """Extract the title and url from the data."""
        url = item['given_url']
        if 'resolved_url' in item:
            url = item['resolved_url']

        title = item['given_title']
        if 'resolved_title' in item:
            if len(item['resolved_title']) > 0:
                title = item['resolved_title']

        return title, url
       

######################################################################
### pocket.py ends here
