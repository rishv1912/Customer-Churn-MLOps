import logging 
from abc import ABC,abstractmethod

import numpy as np 
import pandas as pd 
from sklearn.model_selection import train_test_split

from typing import Union 

class DataStrategy(ABC):
    pass

