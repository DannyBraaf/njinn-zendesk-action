import requests
import base64
import json


class Execute:

    def run(self):

        if self.ticketid:
            url = +self.url+'/api/v2/tickets/'+self.ticketid+'.json'
        else:
            url = +self.url+'/api/v2/tickets'
        
        creds = ''+self.username+':'+self.password+':'
        b64auth = base64.standard_b64encode(creds.encode('utf-8'))
        headers = { 'Authorization': 'Basic %s' % b64auth.decode(),
        'Content-Type': 'application/json'
        }

        

        response = requests.get(url, headers=headers)

        print(response.text)

        return response.json()
