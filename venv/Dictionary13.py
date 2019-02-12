from Utility.UtilityDataStructures import UtilityDataStructures

u = UtilityDataStructures()

try:
    dict = {'1': 1}
    dict.clear()
    sets = [{'id1': '1', 'successs': True, 'names': 'Lary'}, {'id': '2', 'status': False, 'naam': 'Rabi'}, {'id': '3', 'success': True, 'name': 'Alex'}]
    for io in sets:
        dict.update(io)
    print(dict)
    val = []
    count = 0;

    for (k,v) in dict.items():
        if(val.__contains__(v)): continue
        else:
            val.append(v)
            count += 1
    print(val," and count is ",count)

except Exception as e:
        print("Process stopped because %s" % e)

