
from Utility.UtilityDataStructures import UtilityDataStructures
util = UtilityDataStructures()
flag: bool = True
while flag:
    try:
        sets = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success': False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]

        count = 0
        for io in sets:
            if io['success']:
                # the dictionary has the value True at key success in it
                count += 1
        print("The success has the value True ", count, " times")

    except Exception as e:
            print("Process stopped because %s" % e)

    print("To exit press 0 else press any other number")
    if util.get_integer() == 0:
        flag = False
