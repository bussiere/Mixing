import itertools
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# filename: specs.py
from flask import Flask
from flask import request
import json
app = Flask(__name__)
app.url_map.strict_slashes = False

def make_error(status_code, sub_code, message, action):
    response =  {
        'status': status_code,
        'sub_code': sub_code,
        'message': message,
        'action': action
    }
    return json.dumps(response),status_code


@app.route('/api/v1/combine', methods=['POST'])
def loginVanilla():
    content = request.get_json(silent=True)
    print(content)
    if (content['separator'] == None):
        separator = ":"
    else :
        separator = content['separator']
    if (content['list'] == None) :
        return make_error(400, 1, 'parameter', None)
    result = combine(content['list'],separator)
    resp = {'result': result}
    return json.dumps(resp), 200, {'ContentType': 'application/json'}






def combine(lst2,separator=":"):
    lst2 = sorted(lst2)
    combs = []
    lst = []
    for data in lst2:
        lst.append(separator + data + separator)

    for i in xrange(1, len(lst) + 1):
        els = [list(x) for x in itertools.combinations(lst, i)]
        combs.extend(els)

    result = []
    print(combs)

    for data in combs:
        stre = ""
        for d in data:
            stre = stre + d
        stre = stre.replace(separator+separator, separator)
        stre = stre[1:]
        stre = stre[:-1]
        result.append(stre)
    result = sorted(result)
    return result


if __name__ == '__main__':
    app.run(debug=True)







