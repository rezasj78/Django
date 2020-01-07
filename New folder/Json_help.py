import json

JF = open("package.json", "r")
j = json.load(JF)
j = json.dumps(j["friends_phone"])
JF.close()
file = open("package2.json", "w")
file.write(j)
file.close()