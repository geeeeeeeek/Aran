#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests, json
tuling_key = "cdd4f8362ad24ab5aae007d97d6fb35f"

def auto_reply(msg, uid):
    print 'Input message -->', msg
    if tuling_key:
        url = "http://www.tuling123.com/openapi/api"
        user_id = uid.replace('@', '')[:30]
        body = {'key': tuling_key, 'info': msg.encode('utf8'), 'userid': user_id}
        r = requests.post(url, data = body)
        respond = json.loads(r.text)
        print json.dumps(respond, indent=4, sort_keys=True).decode('unicode-escape').encode('utf8')

        result = ''
        code = respond['code']
        text = respond['text']
        if code == 100000: # TEXT
            result = text
        elif code == 200000: # URL
            result = text + '\n' + respond['url']
        elif code == 302000: # News list
            for item in respond['list']:
                result += u'【'+ item['source'] + u'】' + item['article'] + '\n' + item['detailurl'] + '\n\n'
        elif code == 308000: # Cook menu
            for item in respond['list']:
                result += u'【'+ item['name'] + u'】' + item['info'] + '\n' + item['detailurl'] + '\n\n'
        print 'ROBOT---->', result
        return result
    else:
        return u'我知道啦'
