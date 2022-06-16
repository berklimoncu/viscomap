from re import L
import urllib.parse

def encodeURL(jsonData,depth):
    tempJsonData = jsonData
    if depth == 1:
        for key in list(tempJsonData.keys()):
            if (key != "score") and (key != "Depth"):
                for key2 in list(tempJsonData[key].keys()):
                    key2_1 = urllib.parse.quote(key2, safe='').replace(".", "%2E")
                    tempJsonData[key][key2_1] = tempJsonData[key].pop(key2)
                key_1 = urllib.parse.quote(key, safe='').replace(".", "%2E")
                tempJsonData[key_1] = tempJsonData.pop(key)
    elif depth == 2:
        for key in list(tempJsonData.keys()):
            if (key != "score") and (key != "Depth"):
                for key2 in list(tempJsonData[key].keys()):
                    if key2 != "score":
                        for key3 in list(tempJsonData[key][key2].keys()):
                            if key3 != "score":
                                key3_1 = urllib.parse.quote(key3, safe='').replace(".", "%2E")
                                tempJsonData[key][key2][key3_1] = tempJsonData[key][key2].pop(key3)
                        key2_1 = urllib.parse.quote(key2, safe='').replace(".", "%2E")
                        tempJsonData[key][key2_1] = tempJsonData[key].pop(key2)
                key_1 = urllib.parse.quote(key, safe='').replace(".", "%2E")
                tempJsonData[key_1] = tempJsonData.pop(key)
    return tempJsonData