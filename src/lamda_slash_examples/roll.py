import json
import os
import random
import time

from base64 import b64decode
from urlparse import parse_qs
#different lib since aws lambda env butchered this... and my brain

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
    
    random.seed(time.time())
    
    params = parse_qs(b64decode(event['body']))
    
    token = params['token'][0]
    user = params['user_name'][0]
    output = 0
    
    if token != EXPECTED_TOKEN:
        return respond(Exception('Invalid request token'))

    if 'text' in params:
        number = params['text'][0]
        stripped = number.split(' ', 1)

        try:
            tmp = int(stripped[0])
        except:
            return respond(None, "A %s is not an integer... %s" % (stripped[0], user))
        
        output = random.randint(0,tmp)

    else:
        output = random.randint(0,100)

    return respond(None, "%s rolled a %d" % (user, output))
