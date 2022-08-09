class Distribution:
    """
        Distribution of dataset and their mean and standard deviation

        Args:
            mu (): the mean of the distribution. Default mean value is 1
            sigma (): the standard deviation of the distribution. Default value is 0

        Attributes:
            mean (): the mean value of the distribution
            stdev (): the standard deviation of the distribution
            data (list of float): list of float values extracted from the raw text file

        """

    def __init__(self, mu=0, sigma=1):
        self.mean = mu
        self.stdev = sigma
        self.data = []

    def read_data_file(self, file_name, sample=True):
        """
            Method to read in data from a txt file. The txt file should have
            one number (float) per line. The numbers are stored in the data attribute.
            After reading in the file, the mean and standard deviation are calculated

            Args:
                file_name (string): name of a file to read from
                sample (bool): whether the data represent a sample or population
                    Default value is True

            Returns:
                None

        """
        with open(file_name) as file:
            line = file.read()
            # update the data attribute
            data_list = list(map(int, line.split('\n')))

        # update the data
        self.data = data_list