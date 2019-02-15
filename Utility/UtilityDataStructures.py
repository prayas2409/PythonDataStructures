class UtilityDataStructures:


    def arrayQ1(array,num):
        for counter in range(num):
            print(array[counter])

    def get_integer(self):
        while True:
            try:
                # try to convert the input to integer
                numinput = int(input())
                return numinput
            except:
                print("not a proper input please try again")

    def get_positive_integer(self):
        while True:
            try:
                numinput = int(input())
                # trying to check if the number is greater than 0
                if numinput > 0:
                    return numinput
                else:
                    print("Enter a positive number")
            except:
                print("not a proper input please try again")

    def delete_from_back(dlist, ditem):

        llist = [dlist]
        # reverse list
        llist.reverse()
        # deletes first occurrence of the item
        llist.remove(ditem)
        llist.reverse()
        print('deleted successfully')
        return llist


    def swipe_from_r_to_l(self,list, start, last):

        for counter in range(start, last):
            # swiping of the elements from right to left
            list[counter] = list[counter+1]
        return list

    def equalsList(self, list1, list2):
        # if length not equal
        if list1.__len__() != list2.__len__():
            return False
        else:
            for counter in range(list1.__len__()):
                # each element is equal or not
                if list1[counter] != list2[counter]:
                    return False
            return True

    def if_common_element(self, list1, list2):

        for string1 in list1:
            for string2 in list2:
                if string1.lower() == string2.lower():
                   return True
        return False

    def longest_string(self, list1):

        llength = 0
        longstring = ""
        for item in list1:
            if item.__len__() > llength:
                # if length greater than current store the length
                llength = item.__len__()
                longstring = item
        print("longest element is ", longstring)
        return llength

    def sort(self, list1):
        # sorting
        for counter1 in range(0, list1.__len__()):
            for counter2 in range(counter1+1, list1.__len__()):
                if list1[counter1] > list1[counter2]:
                    temp = list1[counter2]
                    list1[counter2] = list1[counter1]
                    list1[counter1] = temp
        return list1
