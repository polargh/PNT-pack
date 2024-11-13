import json

to_convert = input('Enter which file you would like to convert: ')

final = {
    "model": {
        "type": "minecraft:range_dispatch",
        "property": "minecraft:custom_model_data",
        "index": 0,
        "entries": []
    }
}

with open(to_convert, encoding='utf-8') as f:
    parsed = json.load(f)
    for override in parsed.get('overrides'):
       modelDataInt = override.get('predicate').get('custom_model_data')
       model = override.get('model')
       print('Passing model:', model)

       final['model']['entries'].append({
           "threshold": modelDataInt,
           "model": {
               "type": "minecraft:model",
               "model": model
           }
       })

with open("../../items/"+to_convert, 'w') as f:
    json.dump(final, f, indent=4)

print(f'Finished, saved in /assets/minecraft/items')
input()