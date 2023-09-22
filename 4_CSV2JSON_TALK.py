from fileinput import filename
import json
import csv
filename = 'EN'  # ต้นฉบับ
translated = 'translated'  # CSV ที่แปลแล้ว
outputfile = 'last'  # JSON ขาออก
with open(filename+'.json', encoding='utf8') as f:
    data = json.load(f)
    for i in data['Exports']:
        for x in i['Table']['Data']:
            print('ID :' + x['Name'])
            with open(translated+'.csv', encoding='utf-8') as csv_file:
                csv_data = csv.reader(csv_file, delimiter=',')
                for row in csv_data:
                    if row[0] == x['Name']:
                        for y in x['Value']:
                            if y['Name'] == 'Text(0)':
                                if row[2] == "":
                                    continue
                                y['Value'][0]['Value'] = row[2]
    with open(outputfile+'.json', "w", encoding='utf-8') as k:
        k.write(json.dumps(data, indent=4, ensure_ascii=False))
        k.close()
