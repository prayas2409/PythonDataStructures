from Utility.UtilityDataStructures import UtilityDataStructures

try:
    dict = {"0":11,"1":13,"2":12,"3":16,'4':14}
    print("The dictionary before sorting is")
    for key in dict:
        print("For key ",key, " value is: ",dict[key])

    keys = [key for key in dict]
    values = [dict[key] for key in dict]
    temp = 0
    j = 0
    for j in range(values.__len__()):
        for i in range(values.__len__()-1):
            if values[i]>values[i+1]:
                temp = keys[i]
                keys[i]=keys[i+1]
                keys[i+1] = temp;
                temp = values[i]
                values[i]=values[i+1]
                values[i+1]=temp;
    dict.clear()
    print("The dictionary after sorting is")

    for i in range(keys.__len__()):
        dict[keys[i]]=values[i]
    print("Now printing dictionary")
    print(dict)

    print("In descending order");

    for j in range(values.__len__()):
        for i in range(values.__len__()-1):
            if values[i] < values[i+1]:
                temp = keys[i]
                keys[i] = keys[i+1]
                keys[i+1] = temp;
                temp = values[i]
                values[i] = values[i+1]
                values[i+1] = temp;
    dict.clear()
    for i in range(keys.__len__()):
        dict[keys[i]] = values[i]
    print("Now printing dictionary")
    print (dict)

except Exception as e:
    print("Process stopped because %s" % e)
    '''
    print("Sorting with the help of items")
    for j in range(dict.__len__()):
        i=0
        for (k,v)  in dict.items():
            if i < (dict.__len__() - 1):
                if dict[k[i]] > dict[k[i + 1]]:
                    item2 = dict[k[i]]
                    dict[k[i]] = dict[k[i + 1]]
                    dict[k[i + 1]] = item2
            else: break
            i +=1
    print("Now printing dictionary")
    
    print(dict)
'''

