import json

json_str = """
{
    "simpleDeclarationRequest": {
        "requestCommon": {
            "receiptDate": "2018-05-31T12:14:08Z",
            "acknowledgementReference": "XXXXXXXXXXXXXXX",
            "requestParameters": [
                {
                    "paramName": "REGIME",
                    "paramValue": "PNGR"
                }
            ]
        },
        "requestDetail": {
            "contactDetails": {

            },
            "declarationTobacco": {
                "totalExciseTobacco": "100.54",
                "totalCustomsTobacco": "192.94",
                "totalVATTobacco": "149.92",
                "declarationItemTobacco": [
                    {
                        "commodityDescription": "Ciagerettes",
                        "quantity": "250",
                        "goodsValue": "400.00",
                        "valueCurrency": "USD",
                        "originCountry": "US",
                        "exchangeRate": "1.20",
                        "exchangeRateDate": "2018-10-29",
                        "customsValueGBP": "304.11",
                        "VATRESClaimed": false,
                        "exciseGBP": "74.00",
                        "customsGBP": "79.06",
                        "vatGBP": "91.43"
                    },
                    {
                        "commodityDescription": "Rolling Tobacco",
                        "weight": "120.00",
                        "goodsValue": "200.00",
                        "valueCurrency": "USD",
                        "originCountry": "US",
                        "exchangeRate": "1.20",
                        "exchangeRateDate": "2018-10-29",
                        "customsValueGBP": "152.05",
                        "VATRESClaimed": false,
                        "exciseGBP": "26.54",
                        "customsGBP": "113.88",
                        "vatGBP": "58.49"
                    }
                ]
            },
            "declarationAlcohol": {
                "totalExciseAlcohol": "2.00",
                "totalCustomsAlcohol": "0.30",
                "totalVATAlcohol": "18.70",
                "declarationItemAlcohol": [
                    {
                        "commodityDescription": "Cider",
                        "volume": "5",
                        "goodsValue": "120.00",
                        "valueCurrency": "USD",
                        "originCountry": "US",
                        "exchangeRate": "1.20",
                        "exchangeRateDate": "2018-10-29",
                        "customsValueGBP": "91.23",
                        "VATRESClaimed": false,
                        "exciseGBP": "2.00",
                        "customsGBP": "0.30",
                        "vatGBP": "18.70"
                    }
                ]
            },
            "declarationOther": {
                "totalExciseOther": "0.00",
                "totalCustomsOther": "341.65",
                "totalVATOther": "556.41",
                "declarationItemOther": [
                    {
                        "commodityDescription": "Televisions",
                        "quantity": "1",
                        "goodsValue": "1500.00",
                        "valueCurrency": "USD",
                        "originCountry": "US",
                        "exchangeRate": "1.20",
                        "exchangeRateDate": "2018-10-29",
                        "customsValueGBP": "1140.42",
                        "VATRESClaimed": false,
                        "exciseGBP": "0.00",
                        "customsGBP": "159.65",
                        "vatGBP": "260.01"
                    },
                    {
                        "commodityDescription": "Televisions",
                        "quantity": "1",
                        "goodsValue": "1300.00",
                        "valueCurrency": "GBP",
                        "originCountry": "GB",
                        "exchangeRate": "1.20",
                        "exchangeRateDate": "2018-10-29",
                        "customsValueGBP": "1300.00",
                        "VATRESClaimed": false,
                        "exciseGBP": "0.00",
                        "customsGBP": "182.00",
                        "vatGBP": "296.40"
                    }
                ]
            },
            "liabilityDetails": {
                "totalExciseGBP": "102.54",
                "totalCustomsGBP": "534.89",
                "totalVATGBP": "725.03",
                "grandTotalGBP": "1362.46"
            }
        }
    }
}
"""


json_str = """
{
    "type": "apple",
    "props": {
        "color": "green",
        "size": "small"
    },
    "stockists": [
        "Tesco", "Sainsburys"
    ]
}
"""

json_str = """
{
  "alcohol" : {
    "bands" : [ {
      "code" : "B",
      "items" : [ {
        "rateId" : "ALC/A2/BEER",
        "purchaseCost" : "1548.94",
        "weightOrVolume" : 2000,
        "calculation" : {
          "excise" : "1600.00",
          "customs" : "0.00",
          "vat" : "629.78",
          "allTax" : "2229.78"
        },
        "metadata" : {
          "description" : "2000 litres beer",
          "declarationMessageDescription" : "Beer",
          "cost" : "2000.00",
          "currency" : {
            "code" : "USD",
            "displayName" : "USA Dollar (USD)",
            "value" : "USD"
          },
          "country" : {
            "countryName" : "Australia",
            "alphaTwoCode" : "AU",
            "isEu" : false,
            "currencyCode" : "AUD"
          },
          "exchangeRate" : {
            "rate" : "1.2912",
            "date" : "2018-11-26"
          }
        }
      } ],
      "calculation" : {
        "excise" : "1600.00",
        "customs" : "0.00",
        "vat" : "629.78",
        "allTax" : "2229.78"
      }
    } ],
    "calculation" : {
      "excise" : "1600.00",
      "customs" : "0.00",
      "vat" : "629.78",
      "allTax" : "2229.78"
    }
  },
  "calculation" : {
    "excise" : "1600.00",
    "customs" : "0.00",
    "vat" : "629.78",
    "allTax" : "2229.78"
  }
}
"""


json = json.loads(json_str)

    # elif(type(json) == list):
    #     for i in json:
    #         print("{} >> {}:".format('  '*t, i), end='')
    #         parse_json(i, t+1)
    #         print()



def parse_json(key, value, t):

    def handle_dict(key, value, t):
        print('{}Json.obj('.format(' '*t, key))
        for k, v in value.items():
            parse_json(k, v, t+2)
        print('{})'.format(' '*t, key))

    def handle_list(key, value, t):
        print('{}Json.arr('.format(' '*t, key))
        for i in value:
            parse_json('>', i, t+2)
        print('{})'.format(' '*t, key))

    def handle_item(key, value, t):
        print('{}"{}" -> "{}"'.format(' '*t, key, value))

    if(type(value) == dict):
        handle_dict(key, value, t)
    elif(type(value) == list):
        handle_list(key, value, t)   
    else:
        handle_item(key, value, t)
            
    # else:
    #     for k, v in json.items():
    #         print("{} {}: {}".format('  '*t, k, v))

parse_json("root", json, 0)
