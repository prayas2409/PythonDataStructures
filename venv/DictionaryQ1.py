from Utility.UtilityDataStructures import UtilityDataStructures
util = UtilityDataStructures()
flag: bool = True
while flag:

    try:
        dict1 = {"0": 11, "1": 13, "2": 12, "3": 16, '4': 14}
        print("The dictionary before sorting is")
        for key in dict1:
            print("For key ", key, " value is: ", dict1[key])

        keys = [key for key in dict1]
        values = [dict1[key] for key in dict1]
        temp = 0
        j = 0
        # sorting dictionary in  ascending order
        for j in range(0, values.__len__()):
            for i in range(values.__len__()-1):
                if values[i] > values[i+1]:
                    temp = keys[i]
                    keys[i] = keys[i+1]
                    keys[i+1] = temp
                    temp = values[i]
                    values[i] = values[i+1]
                    values[i+1] = temp
        # store empty values again in dictionary to make it clear
        dict1 = {'': ''}
        print("The dictionary after sorting is")
        # storing values in dictionary after sorting
        for i in range(keys.__len__()):
            dict1[keys[i]] = values[i]
        dict1.__delitem__('')
        print("Now printing dictionary")
        print(dict1)

        print("In descending order")
        # sorting in descending order
        for j in range(values.__len__()):
            for i in range(values.__len__()-1):
                if values[i] < values[i+1]:
                    temp = keys[i]
                    keys[i] = keys[i+1]
                    keys[i+1] = temp
                    temp = values[i]
                    values[i] = values[i+1]
                    values[i+1] = temp
        dict1 = {'': ''}
        for i in range(keys.__len__()):
            dict1[keys[i]] = values[i]
        dict1.__delitem__('')
        print("Now printing dictionary")
        print(dict1)

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
    print("To exit press 0 else press any other number")
    if util.get_integer() == 0:
        flag = False
