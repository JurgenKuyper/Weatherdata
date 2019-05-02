import os
try:
    os.remove("running.txt")
except FileNotFoundError:
    print("done")
# import json
# with open("datastore.json", "r") as File:
#     print(json.loads(File.read()))