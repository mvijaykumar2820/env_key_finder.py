import os

query = input("What key are you looking for?: ").lower()

def getapikey(pattern):
    matches = {}
    for key, value in os.environ.items():
        if pattern in key.lower():
            matches[key] = value
    return matches

results = getapikey(query)

if results:
    for k, v in results.items():
        print(f"{k} found:", v)
else:
    print("No matching keys found.")