from Utility.UtilityDataStructures import UtilityDataStructures
util = UtilityDataStructures()
flag: bool = True

while flag:
    try:
        # creating a new dictionary
        dict1 = {'1': 1}
        # clearing the dictionary for use
        dict1.clear()
        # creating set of dictionary
        sets = [{'id1': '1', 'successs': True, 'names': 'Lary'},
                {'id': '2', 'status': False, 'naam': 'Rabi'},
                {'id': '3', 'success': True, 'name': 'Alex'}]
        # adding elements to the dictionary
        for io in sets:
            dict1.update(io)
        print(dict1)
        val = []
        count = 0
        # for key, value in dictionary items
        for (k, v) in dict1.items():
            # storing unique vals in new list
            if val.__contains__(v):
                continue
            else:
                val.append(v)
                count += 1
        print(val, " and count is ", count)

    except Exception as e:
        print("Process stopped because %s" % e)
    print("To exit press 0 else press any other number")
    if util.get_integer() == 0:
            flag = False
