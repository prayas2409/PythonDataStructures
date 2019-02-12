from Utility.UtilityDataStructures import UtilityDataStructures

u = UtilityDataStructures()

try:
    dict = {'1':1}
    sets = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success': False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]

    count = 0
    for io in sets:
        if io['success']:
            # the dictionary has the value True at key success in it
            count += 1
    print(count)

except Exception as e:
        print("Process stopped because %s" % e)

