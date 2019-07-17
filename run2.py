import json

jsval = """
{
    "class": "fruit",
    "type": "apple",
    "props": {
        "color": "red",
        "size": 2,
        "is_ripe": true
    },
    "stockists": [
        "Tesco", "Sainsburys"
    ]
}
"""

js = json.loads(jsval)

def handlevalue(value, tabs = ''):
    newtabs = tabs+'  '
    if type(value) == dict:
        return 'Json.obj(' + ','.join(['\n{}"{}" -> {}'.format(newtabs, k, handlevalue(v, newtabs)) for k, v in value.items()]) + '\n' + tabs + ')'
    elif type(value) == list:
        return 'Json.arr(\n{}'.format(newtabs) + ',\n{}'.format(newtabs).join([str(handlevalue(v, newtabs)) for v in value]) + '\n' + tabs + ')'
    elif type(value) == str:
        return '"{}"'.format(value)
    else:
        return '{}'.format(value).lower()
        
print(handlevalue(js))
