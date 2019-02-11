from Utility.UtilityDataStructures import UtilityDataStructures

u = UtilityDataStructures()

try:
    dict = {"IV":"S001", "VII": "S002", "VI": "S001", "IIV": "S005", "IIIV":"S005", "V":"S009","VIII":"S007"}
    print(dict)
    keys = [key for key in dict]
    print(keys)
    values = [v for (k,v) in dict.items()]
    print(values)
    array = [values.__len__()][1]

    for i in range(values.__len__()):
        count = 0
        k = 0
        j = i+1
        array[i][1] = 0
        array[i][0] = values[i]
        ranges = range(values.__len__())
        for j in range(i+1, ranges):
            if values[j] == values[i]:
                array[i][j] = values[j]

        for j in range(ranges):
            while array[j][1]>0:
                values.__delitem__(array[j][0])
                array[j][1] -= 1
                ranges -= 1

    try:

        print(values)
    except:
        print('Key not found')


except Exception as e:
    print("Process stopped because %s" % e)
