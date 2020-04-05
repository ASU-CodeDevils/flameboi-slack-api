import requests
import json


    
    
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
ans += "\nUSA\n\tCase:\n\t\tActive: {}\n\t\tNew: {}\n\t\tCritical: {}\n\t\tRecovered: {}\n\t\tTotal: {}\n\tDeaths:\n\t\tNew: {}\n\t\tTotal: {}".format(usCases['active'], usCases['new'], usCases['critical'], usCases['recovered'], usCases['total'], usDeaths['new'], usDeaths['total'])

ansblock = {
	"blocks": [
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
			"text": {
				"type": "mrkdwn",
				"text": "Cases"
			}
		},
		{
			"type": "section",
			"fields": [
								{
					"type": "mrkdwn",
					"text": "Active: %s" % allCases['active']
				},
				{
					"type": "mrkdwn",
					"text": "Active: %s" % usCases['active']
				},
				{
					"type": "mrkdwn",
					"text": "New: %s" % allCases['new']
				},
				{
					"type": "mrkdwn",
					"text": "New: %s" % usCases['new']
				},
				{
					"type": "mrkdwn",
					"text": "Critical: %s" % allCases['critical']
				},
				{
					"type": "mrkdwn",
					"text": "Critical: %s" % usCases['critical']
				},
				{
					"type": "mrkdwn",
					"text": "Recovered: %s" % allCases['recivered']
				},
				{
					"type": "mrkdwn",
					"text": "Recovered: %s" % usCases['recivered']
				},
                {
					"type": "mrkdwn",
					"text": "Total: %s" % allCases['total']
				},
				{
					"type": "mrkdwn",
					"text": "Total: %s" % usCases['total']
				}
			]
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Deaths"
			}
		},
		{
			"type": "section",
			"fields": [
				{
					"type": "mrkdwn",
					"text": "New: %s" % allCases['new']
				},
				{
					"type": "mrkdwn",
					"text": "New: %s" % usCases['new']
				},
				{
					"type": "mrkdwn",
					"text": "Total: %s" % allCases['total']
				},
				{
					"type": "mrkdwn",
					"text": "Total: %s" % usCases['total']
				}
			]
		}
	]
}

# return {
#     'statusCode': 200,
#     'headers': {
#         'Content-Type': 'application/json'
#     },
#     'body': json.dumps({
#         'text': ans,
#         'response_type': 'in_channel'
#     }),
# }
