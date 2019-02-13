
from Utility.UtilityDataStructures import UtilityDataStructures
util = UtilityDataStructures()
flag: bool = True
while flag:

    try:
        sets = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'status': False, 'naam': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]
        flag = True
        key = list(sets[0].keys())
        count = len(key)
        print(key)
        for element in sets:
            for k, v in element.items():
                flag = True
                for ke in key:
                    if key.__contains__(k):
                        flag = False
                        break
                if not flag:
                    continue
                else:
                    key.append(k)
                    count += 1
        print(key, "and number of different keys is ", count)
    except Exception as e:
            print("Process stopped because %s" % e)
    print("To exit press 0 else press any other number")
    if util.get_integer() == 0:
        flag = False
