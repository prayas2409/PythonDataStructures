class UtilityDataStructures:

    def arrayQ1(array,num):
        for i in range(num):
            print (array[i])

    def getInteger(self):
        while True:
            try:
                n = int(input())
                return n
            except:
                print("not a proper input please try again")

    def getPositiveInteger(self):
        while True:
            try:
                n = int(input())
                if n > 1:
                    return n
                else:
                    print("Enter a positive number")
            except:
                print("not a proper input please try again")

    def deleteFromBack(self,dlist,ds):

        llist = [dlist]
        llist.reverse()
        llist.__delitem__(ds)
        llist.reverse()
        print('deleted successfully')
        return llist

    def swipeFromRtoL(self, list, start, last):

        for i in range(start, last):
            list[i] = list[i+1]
        return list
