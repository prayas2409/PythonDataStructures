from Utility.UtilityDataStructures import UtilityDataStructures

u = UtilityDataStructures()

try:
    l1 = ['Prayas', 'Deepak', 'Sunil', 'Veejay', 'Suhas', 'Narayan', 'Ajay']
    l2 = ['Rakesh', 'sunil', 'Manoj']
    flag = False
    for string1 in l1:
       for string2 in l2:
           if string1.lower() == string2.lower():
                print(True)
                exit()
    print(False)

except Exception as e:
    print("Process stopped because %s" % e)
