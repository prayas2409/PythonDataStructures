class BayesTheorem:

    def __init__(self):
        # chances of person having the cancer
        self.p_having_cancer = 1 / 100
        # probability of the +ve test that are true
        self.p_test_true = 90 / 100
        # not having cancer still got true
        self.p_false_Result = 8 / 100
        # probability of not having cancer is 1 - prob of having cancer
        self.p_not_having_cancer = 1 - self.p_having_cancer

    def prob_Cancer_When_Result_Positive(self):
        p_test_positive = self.p_having_cancer * self.p_test_true + self.p_not_having_cancer * self.p_false_Result
        p_cancer_given_positive: float = (self.p_having_cancer * self.p_test_true) / p_test_positive
        return p_cancer_given_positive


bayes_object = BayesTheorem()
print("The probability of having the cancer when you got the test +ve is %.2f" % bayes_object.prob_Cancer_When_Result_Positive())
# for a next time the value of having cancer will be the previously calculated
 