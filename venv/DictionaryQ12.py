from Utility.UtilityDataStructures import UtilityDataStructures

u = UtilityDataStructures()

try:
    sets = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'status': False, 'naam': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]
    flag = True
    key = list(sets[0].keys())
    count = len(key)
    print(key)
    for io in sets:
        for k,v in io.items():
            flag = True
            for ke in key:
                if key.__contains__(k):
                    flag = False
                    break
            if flag != True:
                continue
            else:
                key.append(k)
                count += 1
    print(key, "and number of different keys is ",count)
except Exception as e:
        print("Process stopped because %s" % e)
