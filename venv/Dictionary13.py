from Utility.UtilityDataStructures import UtilityDataStructures
util = UtilityDataStructures()
flag: bool = True

while flag:
    try:
        dict1 = {'1': 1}
        dict1.clear()
        sets = [{'id1': '1', 'successs': True, 'names': 'Lary'}, {'id': '2', 'status': False, 'naam': 'Rabi'}, {'id': '3', 'success': True, 'name': 'Alex'}]
        for io in sets:
            dict1.update(io)
        print(dict1)
        val = []
        count = 0
        for (k, v) in dict1.items():
            if val.__contains__(v): continue
            else:
                val.append(v)
                count += 1
        print(val," and count is ",count)

    except Exception as e:
        print("Process stopped because %s" % e)
    print("To exit press 0 else press any other number")
    if util.get_integer() == 0:
            flag = False
