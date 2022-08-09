import math
import numpy as np
import matplotlib.pyplot as plt
from generaldistribution import Distribution


class GaussianDistribution(Distribution):
    """
    Gaussian distribution class for calculating
    and visualizing Gaussian distribution: the distribution. Default mean value is 1
        sigma (): the standard deviation of the distribution. Default value is 0

    Attributes:
        mean (): the mean value of the distribution
        stdev (): the standard deviation of the distribution
        data (list of float): list of float values extracted from the raw text file

    """

    def __init__(self, mu=0, sigma=1):
        Distribution.__init__(self, mu, sigma)

    def __repr__(self):
        """Magic method to output the characteristics of the Gaussian instance

            Args:
                None

            Returns:
                string: characteristics of the Gaussian

        """
        return f"mean: {round(self.mean, 2)} and standard deviation: {round(self.stdev, 2)}"

    def __add__(self, other):
        result = GaussianDistribution()

        # calculate the mean and standard deviation of this new gaussian distribution
        result.mean = self.mean + other.mean
        result.stdev = np.sqrt(self.stdev ** 2 + other.stdev ** 2)

        return result

    def calculate_mean(self):
        """Method to calculate the mean of the data set.

        Args:
            None

        Returns:
            float: mean of the data set

        """
        avg = 1.0 * np.mean(self.data)
        self.mean = avg
        return self.mean

    def calculate_stdev(self, sample=True):
        """Method to calculate the standard deviation of the data set.

        Args:
            sample (bool): whether the data represents a sample or population.
            Default value is True

        Returns:
            float: standard deviation of the data set

        """

        if sample:
            n = len(self.data) - 1
        else:
            n = len(self.data)

        mean = self.mean
        sigma_sqr = 0

        for x in self.data:
            sigma_sqr += (x - mean) ** 2

        sigma_sqr = sigma_sqr / n
        # sigma = round(np.sqrt(sigma_sqr), 2)
        self.stdev = np.sqrt(sigma_sqr)

        return self.stdev

    def plot_histogram(self):
        """Method to output a histogram of the instance variable data using
        matplotlib pyplot library.

        Args:
            None

        Returns:
            None
        """
        plt.hist(self.data)
        plt.title("Distribution of the dataset")
        plt.xlabel("Data")
        plt.ylabel("Count of Data Value")
        plt.show()

    def pdf(self, x):
        """Probability density function calculator for the gaussian distribution.

        Args:
            x (float): point for calculating the probability density function

        Returns:
            float: probability density function output
        """
        result = (1/np.sqrt(2 * np.pi * (self.stdev)**2)) * (np.exp(-(x - self.mean) ** 2 / (2 * (self.stdev**2))))
        return result

    def plot_histogram_pdf(self, n_spaces=50):
        """Method to plot the normalized histogram of the data and a plot of the
        probability density function along the same range

        Args:
            n_spaces (int): number of data points

        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot

        """
        mu = self.mean
        sigma = self.stdev

        min_data = min(self.data)
        max_data = max(self.data)

        # calculates the interval between x values
        interval = 1.0 * (max_data - min_data) / n_spaces

        x = []
        y = []

        # calculate the x values to visualize
        for i in range(n_spaces):
            tmp = min_data + interval * i
            x.append(tmp)
            y.append(self.pdf(tmp))

        # make the plots
        fig, axes = plt.subplots(2, sharex=True)
        fig.subplots_adjust(hspace=.5)
        axes[0].hist(self.data, density=True)
        axes[0].set_title('Normed Histogram of Data')
        axes[0].set_ylabel('Density')

        axes[1].plot(x, y)
        axes[1].set_title('Normal Distribution for \n Sample Mean and Sample Standard Deviation')
        axes[0].set_ylabel('Density')
        plt.show()

        return x, y