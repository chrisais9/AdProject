import json
import urllib.request
import xmltodict
from Server.WordWar.WordWarAPI.PyHangulUtils.hglpkg import hangulutils

def isValidWord(word):

    encText = urllib.parse.quote(word)
    url = "https://opendict.korean.go.kr/api/search?key=84F9B4D48BC9DBB44FADD685A0ED4188&advanced=y&sort=popular&type1=word&q=" + encText
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    data = response.read()
    rescode = response.getcode()

    if (rescode == 200):
        data = json.loads(json.dumps(xmltodict.parse(data)))
        return data['channel']['total']
    else:
        return -1

def chkcallword(word, preword):
    call=0
    if(word==preword) : return True
    t = hangulutils.splitstring(preword)
    k=[]
    if (t[0] == 'ㄴ'):
        k.append('ㅇ')
        for i in range(1, len(t)): k.append(t[i])
        a = hangulutils.joinstring(k)
        if a==word: call=1
    elif (t[0] == 'ㄹ'):
        k.append('ㄴ')
        for i in range(1, len(t)): k.append(t[i])
        a = hangulutils.joinstring(k)
        if a==word:call=1
    if call==1:
        return True
    else:
        return False