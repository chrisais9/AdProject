import json
import urllib.request
import xmltodict


def isValidWord(word):

    encText = urllib.parse.quote(word)
    url = "https://opendict.korean.go.kr/api/search?key=84F9B4D48BC9DBB44FADD685A0ED4188&advanced=y&type1=word&q=" + encText
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    data = response.read()
    rescode = response.getcode()

    if (rescode == 200):
        data = json.loads(json.dumps(xmltodict.parse(data)))
        return data['channel']['total']
    else:
        return -1