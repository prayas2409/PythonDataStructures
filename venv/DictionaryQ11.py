
from Utility.UtilityDataStructures import UtilityDataStructures
util = UtilityDataStructures()
flag: bool = True
while flag:

    try:
        dict1 = {'1': 1}
        sets = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success': False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]
        dict1.clear()
        count = 0
        for io in sets:
            dict1[count] = io
            count += 1
        print(dict1)
    except Exception as e:
            print("Process stopped because %s" % e)

    print("To exit press 0 else press any other number")
    if util.get_integer() == 0:
        flag = False
