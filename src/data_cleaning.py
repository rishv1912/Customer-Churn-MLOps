import logging 
from abc import ABC,abstractmethod

import numpy as np 
import pandas as pd 
from sklearn.model_selection import train_test_split

from typing import Union 

class DataStrategy(ABC):
    
    @abstractmethod
    def handle_data(self,data):
        pass 


class DataPreProcessingStrategy(DataStrategy):
    pass


class DataDivideStrategy(DataStrategy):
    pass

class DataCleaning(DataStrategy):
    pass


