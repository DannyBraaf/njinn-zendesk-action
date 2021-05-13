import requests
import base64
import json


class Execute:

    def run(self):

  
        url = +self.url+'/api/v2/tickets/'+self.ticketid+'.json'
        creds = ''+self.username+':'+self.password+':'
        b64auth = base64.standard_b64encode(creds.encode('utf-8'))
        headers = { 'Authorization': 'Basic %s' % b64auth.decode(),
        'Content-Type': 'application/json'
        }

        data = '{"ticket": {"status": "'+self.Status+'", "tags": "'+self.Tags+'",  "comment": {"public": '+self.Public+', "body": "'+self.Comment+'"}}}'

        response = requests.put(url, headers=headers, data=data)

        print(response.text)

        return response.json()
    
    
    
 

