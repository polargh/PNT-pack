import json
import os

for file in os.listdir("."):
    if not file.endswith(".json"):
        continue

    print(file)

    with open(file) as f:
        jsonFile = json.load(f)
        for entry in jsonFile["model"]["entries"]:
            model = entry["model"]["model"]
            resultFile = model.split(":")[-1] + ".json"
            outputFileContent = {
                "type": "minecraft:model",
                "model": model
            }
            try:
                os.makedirs(os.path.dirname("./auto/" + resultFile))
            except:
                pass
            with open("./auto/" + resultFile, 'w') as outputFile:
                json.dump(outputFileContent, outputFile, indent=4)

print("Finished")
input()