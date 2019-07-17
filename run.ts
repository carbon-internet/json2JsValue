
function json2JsValue(value: any, tabs: string = '') {
    let newtabs = tabs+'  '

    if(Array.isArray(value)) {

        let elements = value.map( v => json2JsValue(v, newtabs) );
        return `Json.arr(\n${newtabs}` + elements.join(`,\n${newtabs}`) + '\n' + tabs + ')';
    }
    else if(typeof value === 'object') {

        let properties = Object.keys(value).map( x => `\n${newtabs}"${x}" -> ${json2JsValue(value[x], newtabs)}` );
        return 'Json.obj(' + properties.join(',') + '\n' + tabs + ')';
    }
    else if(typeof value === 'string') return `"${value}"`;
    else return String(value).toLowerCase();
}

let v = {
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

console.log(json2JsValue(v));