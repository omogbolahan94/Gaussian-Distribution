from gaussian import GaussianDistribution

# obj = GaussianDistribution()
# obj.read_data_file('numbers.txt')
# print(obj)
#
# gauss1 = GaussianDistribution(5, 25)
# gauss2 = GaussianDistribution(10, 25)
#
# new_gauss = gauss1 + gauss2
# print(new_gauss)
# obj.plot_histogram_pdf()

# initialize two gaussian distributions
gaussian_one = GaussianDistribution(25, 3)
gaussian_two = GaussianDistribution(30, 2)

# initialize a third gaussian distribution reading in a data efile
gaussian_three = GaussianDistribution()
gaussian_three.read_data_file('numbers.txt')
gaussian_three.calculate_mean()
gaussian_three.calculate_stdev()

# print out the mean and standard deviations
print(gaussian_one.mean)
print(gaussian_two.mean)

print(gaussian_one.stdev)
print(gaussian_two.stdev)

print(gaussian_three.mean)
print(gaussian_three.stdev)

# the histogram plot of the pdf
gaussian_three.plot_histogram_pdf()
