class UtilityDataStructures:


    def arrayQ1(array,num):
        for counter in range(num):
            print(array[counter])

    def get_integer(self):
        while True:
            try:
                numinput = int(input())
                return numinput
            except:
                print("not a proper input please try again")

    def get_positive_integer(self):
        while True:
            try:
                numinput = int(input())
                if numinput > 0:
                    return numinput
                else:
                    print("Enter a positive number")
            except:
                print("not a proper input please try again")

    def delete_from_back(dlist, ditem):

        llist = [dlist]
        llist.reverse()
        llist.__delitem__(ditem)
        llist.reverse()
        print('deleted successfully')
        return llist


    def swipe_from_r_to_l(self,list, start, last):

        for counter in range(start, last):
            list[counter] = list[counter+1]
        return list

    def equalsList(self, list1, list2):
        if list1.__len__() != list2.__len__():
            return False
        else:
            for counter in range(list1.__len__()):
                if list1[counter] != list2[counter]:
                    return False
            return True

    def if_common_element(self, list1, list2):

        for string1 in list1:
            for string2 in list2:
                if string1.lower() == string2.lower():
                   return True
        return False
