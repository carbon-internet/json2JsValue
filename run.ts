
function handlevalue(value: Object, tabs: String) {
    let newtabs = tabs+'  '

    if(typeof value === 'object') {

        // let entries = Object.entries(value);

        let entries = Object.keys(value).map( x => `\n${newtabs}"${x}" -> ${handlevalue(value[x], newtabs)}` );


        return 'Json.obj(' + entries.join(',') + '\n' + tabs + ')';
    }
    //[.format(newtabs, k, handlevalue(v, newtabs)) for k, v in value.items()]

    // ','.join()

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

console.log(handlevalue(v, '  '));