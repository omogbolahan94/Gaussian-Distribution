<p>This project is about calculating Probability Distribution Function  (PDF) of a Gaussian Distribution.</p>
<br/>
<p>There are five (5) files in the project folder. They are:</p>
*   distribution.py: this file has the `Distribution` class with two methods. The method `__init__` to initialize the class 
with the mean and standard deviation value and the `read_data_file` method to read the numbers.txt file which contains 
the data
*   gaussian.py: this file contains the `GaussianDistribution` class which inherits the attributes and methods of the 
`Distribution` class. Its methods performs mathematical operations like mean, standard deviation, PDF, and plots the histogram of the 
pdf
*   numbers.txt: this file contains strings of numerical values on a seperate line.
*   main.py: this file is used to run the `GaussianDistribution` class on a given mean and standard deviation values.
*   test.py: this file contains unit test code class for the `GaussianDistribution` class.
*    test_code.py: this file is used to run the `test.py` file