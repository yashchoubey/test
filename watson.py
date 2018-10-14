import json


from watson_developer_cloud import ToneAnalyzerV3


tone_analyzer = ToneAnalyzerV3(
	version='2017-09-21',
	username=credentials['username'],
	password=credentials['password'],
	url=credentials['url']
)
 	# print(json.dumps(tone_analysis, indent=2))

tone_analysis = tone_analyzer.tone(
    {'text': ":("},
    'application/json'
).get_result()
print [k["tone_name"] for k in tone_analysis['document_tone']["tones"]]
print "------------------------------------------------------"
# print(json.dumps(tone_analysis, indent=2))