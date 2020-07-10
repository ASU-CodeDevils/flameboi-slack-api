import os
import json
import urllib.request

from base64 import b64decode
from urllib.parse import urlparse

EXPECTED_TOKEN = os.environ['VERIFICATION_TOKEN']

def respond(err, resp_type, block=None):
    return {
        'statusCode': '400' if err else '200',
        'headers': {
            'Content-Type': 'application/json',
        },
        'body': err.message if err else json.dumps({
            'blocks': block,
            'response_type': resp_type 
        })
    }


def lambda_handler(event, context):
    
    params = urllib.parse.parse_qs(b64decode(event['body']))
    
    token = params[b'token'][0].decode("utf-8")
    
    if token != EXPECTED_TOKEN:
        return respond(Exception('Invalid request token'))
        

    block = [
    	{
            "type": "divider"
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "<https://open.spotify.com/playlist/0lHeOLHPtj3dZnI7hjbEiy?si=vsB1ABcPQZWLDfELbbcPSw|:partywizard:*CodeDevils:partywizard:*>"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "<https://open.spotify.com/playlist/1d8nCeom1L86vGT2JgSkzN?si=TjIS1iVcTPqIaGwocuaywA|:partywizard:*ReggaeDevils*:partywizard:>"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "<https://open.spotify.com/playlist/37i9dQZF1DWXLeA8Omikj7?si=kdJfP56gS1mAPYEcsOc5fg|*Brain Food*>"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "<https://open.spotify.com/playlist/37i9dQZF1DWWQRwui0ExPn?si=SB-cPgIsTL-gvA9xWH3rrg|*LoFi Beats*>"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "<https://open.spotify.com/playlist/37i9dQZF1DWZeKCadgRdKQ?si=1VgEAzJmRF-nJ0qNRPd-1A|*Deep Focus*>"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "<https://open.spotify.com/playlist/1VWJjbN7LBzM6M4FG76ImT|*Concentrate Your Mind / Asian LoFi Hip Hop*>"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "<https://open.spotify.com/playlist/08fTEpRNEn0FcyXOWZ60wO?si=xCjkW151TNuhsyjHswqlfQ|*Acid Jazz/Lounge/Dub/Triphop*>"
            }
        }
    ]


    if b'text' in params:
        com = params[b'text'][0].decode("utf-8")
        stripped = com.split(' ', 1)
        if 'privat' in stripped[0]:
            return respond(None, 'ephemeral', block)
    else:
        return respond(None, 'in_channel', block)
