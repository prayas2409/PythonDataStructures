from Utility.UtilityDataStructures import UtilityDataStructures

u = UtilityDataStructures()

try:
    l1 = ['Prayas', 'Deepak', 'Sunil', 'Veejay', 'Suhas', 'Narayan', 'Ajay']
    print("Enter the length ")
    length = u.getPositiveInteger()

    for string in l1:
        if string.__len__() > length:
            print(string)

except Exception as e:
    print("Process stopped because %s" % e)
