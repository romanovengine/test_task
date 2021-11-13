import collections, itertools
import json

with open('employees.json', 'r', encoding='utf-8') as f:
    text = json.load(f)

    temp_dict = collections.defaultdict(list)

    for key, group in itertools.groupby(text, lambda item: item["dept"]):  # group by dept

        for e in group:
            del e['dept']  # remove key,value for key = dept
            temp_dict[key].append(e)

    result_list = [{'dept': key, 'count': len(value), 'people': value} for key, value in temp_dict.items()]
    for dept in result_list:
        dept['count'] = len(dept['people'])

print(result_list)



