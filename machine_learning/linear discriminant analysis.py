"""
    Linear Discriminant Analysis


    Assumptions About Data :
        1. The input variables has a gaussian distribution.
        2. The variance calculated for each input variables by class grouping is the same.
        3. The mix of classes in your training set is representative of the problem.


    Learning The Model :
        The LDA model requires the estimation of statistics from the training data :
            1. Mean of each input value for each class.
            2. Probability of an instance belong to each class.
            3. Covariance for the input data for each class

        Calculate the class means :
            mean(x) = 1/n ( for i = 1 to i = n --> sum(xi))

        Calculate the class probabilities :
            P(y = 0) = count(y = 0) / (count(y = 0) + count(y = 1))
            P(y = 1) = count(y = 1) / (count(y = 0) + count(y = 1))

        Calculate the variance :
            We can calculate the variance for dataset in two steps :
                1. Calculate the squared difference for each input variable from the group mean.
                2. Calculate the mean of the squared difference.
                ------------------------------------------------
                Squared_Difference = (x - mean(k)) ** 2
                Variance = (1 / (count(x) - count(classes))) * (for i = 1 to i = n --> sum(Squared_Difference(xi)))

    Making Predictions :
        discriminant(x) = x * (mean / variance) - ((mean ** 2) / (2 * variance)) + Ln(probability)
        ------------------------------------------------------------------------------------------
        After calculating the discriminant value for each class, the class with the largest discriminant value
        is taken as the prediction.

    Author: @EverLookNeverSee

"""

# importing modules
from random import gauss
from math import log
from os import system, name     # to use < clear > or < cls > commands in terminal or cmd


# Making training dataset drawn from a gaussian distribution
def Normal_gen(mean: float, std_dev: float, instance_count: int) -> list:
    """ This function generates gaussian distribution instances
        based-on given mean and standard deviation
        :param mean: mean value of class
        :param std_dev: value of standard deviation entered by usr or default value of it
        :param instance_count: instance number of class
        :return: a list containing generated values based-on given mean, std_dev and instance_count
        """
    generated_instances = []  # An empty list to store generated instances
    # for loop iterates over instance_count
    for r in range(instance_count):
        # appending corresponding gaussian distribution to 'generated_instances' list
        generated_instances.append(gauss(mean, std_dev))

    return generated_instances
