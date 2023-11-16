import math
import statistics
import numpy as np
from scipy.stats import *
import matplotlib.pyplot as plt



class Distributions:
    """
    Class creates array of randomly selected values from user selected distribution with user selected
    mean, standard deviation, and sample size. The samples can be accessed using class attribute 
    laplace_dist,lognormal_dist, or normal_dist, depending on the corresponding distribution entered 
    into the object.
    
    Attributes:
    ------------

        distribution (str): distribution to sample from, only 'normal', 'lognormal', and 'laplace' will 
        create sample. Any other distribution enter will simply create the class instance.

        mean (float): mean of distribution to sample from

        std_dev (float): standard devation of model to sample from

        size (int): size of sample to create

        laplace_dist (array or None) = array of randomly selected values from laplace distribution
        if laplace distribution selected; None otherwise

        lognormal_dist (array or None) = array of randomly selected values from lognormal distribution
        if laplace distribution selected; None otherwise

        normal_dist (array or None)= array of randomly selected values from normal distribution
        if laplace distribution selected; None otherwise

    
    Methods:
    ----------

        __str__ : returns string representation
            
        __eq__ : checks equality between two Distribution objects using distribution,
        mean, standard deviation, and size.
        

    
    """
    # Set potential future arrays to none to be accessed later
    laplace_dist = None
    lognormal_dist = None
    normal_dist = None

    def __init__(self, distribution, mean, st_dev, size):
        # Lognormal
        if distribution == "lognormal":
          # scipy standardizes s and scale by setting s=sd and scale=exp(mu)
          self.lognormal_dist = lognorm.rvs(s=st_dev, scale=math.exp(mean), size=size)  

          self.distribution = distribution
          self.mean = round(statistics.mean(self.lognormal_dist), 2)
          self.st_dev = round(statistics.stdev(self.lognormal_dist), 2)
          self.size = int(size)

        elif distribution == "normal":
          # Normal
          self.normal_dist = norm.rvs(loc=mean, scale=st_dev, size=size)

          self.distribution = distribution
          self.mean = round(statistics.mean(self.normal_dist), 2)
          self.st_dev = round(statistics.stdev(self.normal_dist), 2)
          self.size = int(size)

        elif distribution == "laplace":
          # Laplace
          # Calculate b:
          var = st_dev**2
          b = math.sqrt(var/2)
          self.laplace_dist = laplace.rvs(loc=mean, scale=b, size=size)

          self.distribution = distribution
          self.mean = round(statistics.mean(self.laplace_dist), 2)
          self.st_dev = round(statistics.stdev(self.laplace_dist), 2)
          self.size = int(size)
        
        else:
          # For when 1 of 3 distributions not entered correctly
          print("You may have meant to type 'normal', 'lognormal' or 'laplace' for distribution. We'll create the object anyways.")
          self.distribution = str(distribution)
          self.mean = float(mean)
          self.st_dev = float(st_dev)
          self.size = int(size)

    def __str__(self):
       return f"Distribution: {self.distribution}, Mean: {self.mean}, Standard Deviation: {self.st_dev}, Size: {self.size}"

    def __eq__(self, other):
        if type(self) == type(other):
            return (self.distribution == other.distribution) and (self.mean == other.mean) and \
            (self.st_dev == other.std_dev) and (self.size == other.size)
        else:
            return NotImplemented


class NumpyDistribution:
    """
    Class creates array of randomly selected values from user selected distribution with user 
    selected mean, standard deviation, and sample size only using numpy methods.. The samples can
    be accessed using class attribute laplace_dist, lognormal_dist, or normal_dist, depending on 
    the corresponding distribution entered into the object. 
    
    Attributes:
    ------------

        distribution (str): distribution to sample from, only 'normal', 'lognormal', and 'laplace' will 
        create sample. Any other distribution enter will simply create the class instance.

        mean (float): mean of distribution to sample from

        std_dev (float): standard devation of model to sample from

        size (int): size of sample to create

        laplace_dist (array or None) = array of randomly selected values from laplace distribution
        if laplace distribution selected; None otherwise

        lognormal_dist (array or None) = array of randomly selected values from lognormal distribution
        if laplace distribution selected; None otherwise

        normal_dist (array or None)= array of randomly selected values from normal distribution
        if laplace distribution selected; None otherwise

    
    Methods:
    ----------

        __str__ : returns string representation
            
        __eq__ : checks equality between two NumpyDistribution objects using distribution,
        mean, standard deviation, and size.
        

    
    """
    laplace_dist = None
    lognormal_dist = None
    normal_dist = None

    def __init__(self, distribution, mean, st_dev, size):
        
        if distribution == "lognormal":
          self.lognormal_dist = np.random.lognormal(mean=mean, sigma=st_dev, size=size)  

          self.distribution = distribution
          self.mean = np.round(np.mean(self.lognormal_dist), decimals=2)
          self.st_dev = np.round(np.std(self.lognormal_dist), decimals=2)
          self.size = size 

        elif distribution == "normal":
          self.normal_dist = np.random.normal(loc=mean, scale=st_dev, size=size)

          self.distribution = distribution
          self.mean = np.round(np.mean(self.normal_dist), decimals=2)
          self.st_dev = np.round(np.std(self.normal_dist), decimals=2)
          self.size = size

        elif distribution == "laplace":
          # same calculation as in Distributions class
          var = st_dev**2
          b=np.sqrt(var/2)
          self.laplace_dist = np.random.laplace(loc=mean, scale=b, size=size)

          self.distribution = distribution
          self.mean = np.round(np.mean(self.laplace_dist), decimals=2)
          self.st_dev = np.round(np.std(self.laplace_dist), decimals=2)
          self.size = size
        
        else:
          print("You may have meant to type 'normal', 'lognormal' or 'laplace' for distribution. We'll create the object anyways.")
          self.distribution = str(distribution)
          self.mean = float(mean)
          self.st_dev = float(st_dev)
          self.size = int(size)
        


    def __str__(self):
      return f"Distribution: {self.distribution}, Mean: {self.mean}, Standard Deviation: {self.st_dev}, Size: {self.size}"

    
    def __eq__(self, other):

        if type(self) == type(other):
            return (self.distribution == other.distribution) and (self.mean == other.mean) and \
            (self.st_dev == other.std_dev) and (self.size == other.size)
        else:
            return NotImplemented
        

# if __name__ == "__main__":
#    norm_dist = Distributions("normal", 10, 5, 1000)
#    lognorm_dist = NumpyDistribution("lognormal", 2, 1, 1000)
#    laplace_dist = Distributions("laplace", 2, 1, 123)
#    print(laplace_dist)
#    print(lognorm_dist.st_dev)
#    print(norm_dist.st_dev)
#    print(norm_dist)
#    print(lognorm_dist)
#    print(type(lognorm_dist.lognormal_dist))
#    laplace_dist = Distributions("laplace", 10, 4, 10000)
#    print(norm_dist)
#    print(lognorm_dist)
#    print(laplace_dist)
#    norm_dist = NumpyDistribution("normal", 10, 5, 10000)
#    lognorm_dist = NumpyDistribution("lognormal", 2, 1, 10000)
#    laplace_dist = NumpyDistribution("laplace", 10, 4, 10000)
#