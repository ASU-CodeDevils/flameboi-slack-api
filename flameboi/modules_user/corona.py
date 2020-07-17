import requests
import json

def lambda_handler(event, context):
    
    
    url = "https://covid-193.p.rapidapi.com/statistics"
    
    querystring = {"country":"all"}
    querystring2 = {"country":"USA"}
    
    headers = {
        'x-rapidapi-host': "covid-193.p.rapidapi.com",
        'x-rapidapi-key': "556658f588mshae9e612c19896b6p181723jsnb7e9ebd5dfbf"
        }
    
    response = requests.request("GET", url, headers=headers, params=querystring)
    response2 = requests.request("GET", url, headers=headers, params=querystring2)
    
    res = response.json()
    res2 = response2.json()
    
    usCases = res2['response'][0]['cases']
    usDeaths = res2['response'][0]['deaths']
    allCases = res['response'][0]['cases']
    allDeaths = res['response'][0]['deaths']
    
    
    ans = "Current Covid-19 Stats\nWorldwide\n\tCases:\n\t\tActive: {}\n\t\tNew: {}\n\t\tCritical: {}\n\t\tRecovered: {}\n\t\tTotal: {}\n\tDeaths: \n\t\tNew: {}\n\t\tTotal: {}\n".format(allCases['active'], allCases['new'], allCases['critical'], allCases['recovered'], allCases['total'], allDeaths['new'], allDeaths['total'])
    ans += "\nUSA\n\tCases:\n\t\tActive: {}\n\t\tNew: {}\n\t\tCritical: {}\n\t\tRecovered: {}\n\t\tTotal: {}\n\tDeaths:\n\t\tNew: {}\n\t\tTotal: {}".format(usCases['active'], usCases['new'], usCases['critical'], usCases['recovered'], usCases['total'], usDeaths['new'], usDeaths['total'])
        
    ansblock = [
    		{
    			"type": "section",
    			"fields": [
    				{
    					"type": "mrkdwn",
    					"text": "*Worldwide*"
    				},
    				{
    					"type": "mrkdwn",
    					"text": "*USA*"
    				}
    			]
    		},
    		{
    			"type": "divider"
    		},
    		{
    			"type": "section",
    			"fields": [
    								{
    					"type": "mrkdwn",
    					"text": "Active Cases: %s" % allCases['active']
    				},
    				{
    					"type": "mrkdwn",
    					"text": "Active Cases: %s" % usCases['active']
    				},
    				{
    					"type": "mrkdwn",
    					"text": "New Cases: %s" % allCases['new']
    				},
    				{
    					"type": "mrkdwn",
    					"text": "New Cases: %s" % usCases['new']
    				},
    				{
    					"type": "mrkdwn",
    					"text": "Critical Cases: %s" % allCases['critical']
    				},
    				{
    					"type": "mrkdwn",
    					"text": "Critical Cases: %s" % usCases['critical']
    				},
    				{
    					"type": "mrkdwn",
    					"text": "Recovered Cases: %s" % allCases['recovered']
    				},
    				{
    					"type": "mrkdwn",
    					"text": "Recovered Cases: %s" % usCases['recovered']
    				},
                    {
    					"type": "mrkdwn",
    					"text": "Total Cases: %s" % allCases['total']
    				},
    				{
    					"type": "mrkdwn",
    					"text": "Total Cases: %s" % usCases['total']
    				}
    			]
    		},
    		{
    			"type": "divider"
    		},
    		{
    			"type": "section",
    			"fields": [
    				{
    					"type": "mrkdwn",
    					"text": "New Deaths: %s" % allDeaths['new']
    				},
    				{
    					"type": "mrkdwn",
    					"text": "New Deaths: %s" % usDeaths['new']
    				},
    				{
    					"type": "mrkdwn",
    					"text": "Total Deaths: %s" % allDeaths['total']
    				},
    				{
    					"type": "mrkdwn",
    					"text": "Total Deaths: %s" % usDeaths['total']
    				}
    			]
    		}
    	]
    
        
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': json.dumps({
            'blocks': ansblock,
            'response_type': 'in_channel'
        }),
    }
