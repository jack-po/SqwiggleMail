import urllib2, base64, json
from pprint import pprint

api_token = "cli_1234567890abcdef"
request = urllib2.Request("https://api.sqwiggle.com/streams")
base64string = base64.encodestring('%s:%s' % (api_token, "X")).replace('\n', '')
request.add_header("Authorization", "Basic %s" % base64string)   
result = urllib2.urlopen(request)
pprint(json.loads(result.read()))