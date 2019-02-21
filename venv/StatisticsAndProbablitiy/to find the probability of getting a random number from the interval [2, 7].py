from Utility.UtilityDataStructures import UtilityDataStructures


class Probability_Random_Number:
    def __init__(self):
        self.list_numbers = [x for x in range(2, 8)]

    def getting_probability(self, point_x):
        probability = self.list_numbers.count(point_x) / len(self.list_numbers)
        print("The probability to find {} in the set {} is {} ".format(point_x, self.list_numbers, probability))


probability_object = Probability_Random_Number()
util = UtilityDataStructures()
print("Enter the number to find probability in the range 2 - 7 ")
probability_object.getting_probability(util.get_integer())
