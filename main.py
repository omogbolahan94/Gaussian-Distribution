from gaussiandistribution import GaussianDistribution
import numpy as np


################################################################
# CREATING GAUSSIAN OBJECTS
################################################################

# initialize two gaussian distributions
gaussian_one = GaussianDistribution(25, 2)
gaussian_two = GaussianDistribution(30, 2)

# initialize a third gaussian distribution reading in a data file
gaussian_three = GaussianDistribution()
gaussian_three.read_data_file('numbers.txt')
# calculate the mean and standard deviation of the numbers read from number.txt and stored in the data attribute
gauss3_mean = gaussian_three.calculate_mean()
gauss3_std = gaussian_three.calculate_stdev()

# print out the mean and standard deviations of guassian object 1 and 2
print(f"MEAN: Gaussian One  = {gaussian_one.mean} & Gaussian Two = {gaussian_two.mean} & Gaussian Three = {gauss3_mean}")
print(f"STANDARD DEVIATION: Gaussian One = {gaussian_one.stdev} & Gaussian Two = {gaussian_two.stdev} & "
      f"Gaussian Three = {gauss3_std}")


####################################################
# PLOT OF GAUSSIAN 3 (SINCE IT CONTAINS DATA VALUES)
####################################################
# the histogram plot of the pdf
gaussian_three.plot_histogram_pdf()


#####################################
# ADDING GAUSSIAN OBJECT
# #######################################

added_gaussian = gaussian_one + gaussian_two

print(f"The mean and standard deviation of the addition of Gaussian One  & Gaussian Two are "
      f"{added_gaussian.mean} & {added_gaussian.stdev} respectively.")
