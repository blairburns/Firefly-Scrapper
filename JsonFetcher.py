import Scrapper as sp
import json

# to get real data
soup = sp.getRaw()


scripts = []

for x in soup:
    scripts.append(str(x))

soupObj = scripts[11]


JSONobject = soupObj.replace('<script>', '')
JSONobject1 = JSONobject.replace('</script>', '')
JSONobject2 = JSONobject1.replace('var PLANNER_INITIAL_STATUS = ', '')

JSON = json.loads(JSONobject2)

def fetchJSON():
    return JSON



