import itertools

class Correlation_Coefficient:

    def __init__(self):
        # self.set_x = list(68, 72, 65, 70, 62, 75, 78, 64, 68)
        # self.set_y = list(90, 85, 88, 100, 105, 98, 70, 65, 72)
        self.set_x = list([1,1,1,1,1])
        self.set_y = list([2,2,2,2,2])
        self.mean_x = self.mean_y = 0
        self.standard_dev_x = self.standard_dev_y = 0
        self.correlation_coefficient = 0

    def calculate_mean_x_and_y(self):
        self.mean_x += (item for item in self.set_x)
        self.mean_y += (item for item in self.set_y)

    def calculate_standard_deviation_x_and_y(self):
        self.standard_dev_x += ((item - self.mean_x) ** 2 for item in self.set_x)
        self.standard_dev_y += ((item - self.mean_y) ** 2 for item in self.set_y)

    def z_score_calculator_x(self, point_x):
        # calculating Z score for point x using mean and standard deviation for that object
        return (point_x - self.mean_x) / self.standard_dev_x

    def z_score_calculator_y(self, point_y):
        # calculating Z score for point x using mean and standard deviation for that object
        return (point_y - self.mean_y) / self.standard_dev_y

    def calculate_Correlation_Coefficient(self):
        self.correlation_coefficient += (self.z_score_calculator_x(item_x) * self.z_score_calculator_y(item_y) for item_x , item_y in itertools.product(self.set_x, self.set_y ))


correlation_coeff_object = Correlation_Coefficient()
x = 0
x += (int(item_x) * int(item_y) for item_x, item_y in correlation_coeff_object.set_x and correlation_coeff_object.set_y)
print(x)