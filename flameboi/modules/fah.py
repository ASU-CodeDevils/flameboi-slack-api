'''
TODO: implement this using the newly modular setup
'''

import os
import json
import urllib.request

from base64 import b64decode
from urllib.parse import urlparse

EXPECTED_TOKEN = os.environ['VERIFICATION_TOKEN']

def respond(err, res=None):
    return {
        'statusCode': '400' if err else '200',
        'headers': {
            'Content-Type': 'application/json',
        },
        'body': err.message if err else json.dumps({
            'text': res,
            'response_type': 'in_channel'
        })
    }


def lambda_handler(event, context):
    
    params = urllib.parse.parse_qs(b64decode(event['body']))
    
    token = params[b'token'][0].decode("utf-8")
    
    if token != EXPECTED_TOKEN:
        return respond(Exception('Invalid request token'))
        
    count = -1
    output = ""
    
    url = "https://apps.foldingathome.org/daily_team_summary.txt"

    file = urllib.request.urlopen(url)

    for line in file:
        decoded_line = line.decode("utf-8")
        if "CodeDevils" in decoded_line:
            output = decoded_line
            break
        count += 1
        
    if not output:
        return respond(None, "CodeDevils not found!")
    
    data = output.split('\t', 3)

    return respond(None, f"The CodeDevils are currently ranked #{count:,} with {int(data[2]):,} points amassed!\nFor a full breakdown of our team go to https://stats.foldingathome.org/team/249718!")
