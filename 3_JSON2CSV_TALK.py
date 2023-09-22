from asyncio.windows_events import NULL
from fileinput import filename
import json
import csv
allitems = []
filename = 'TALK'  # ต้นฉบับ
outputfile = 'TALK'  # CSV ขาออก
with open(filename+'.json', encoding='utf8') as f:
    data = json.load(f)
    for i in data['Exports']:
        for x in i['Table']['Data']:
            print('ID :' + x['Name'])
            for y in x['Value']:
                if y['Name'] == 'Text(0)':
                    print('Text :' + str(y['Value'][0]['Value']))
                    allitems.append(
                        [x['Name'], y['Value'][0]['Value'], ""])
with open(outputfile+'.csv', 'w', encoding='utf8', newline='') as f:
    write = csv.writer(f)
    write.writerow(["ID", "Text", "Translate"])
    write.writerows(allitems)
