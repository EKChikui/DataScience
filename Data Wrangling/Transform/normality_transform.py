
import numpy as np
import pandas as pd

def transformation_log(DF):
    """
    Performs Logaritmic transformation, EXCEPTS if there is negative
    numbers.

    """
    data = DF.copy()

    for column in data.columns:
        data_min = data[column].min()

        if(data_min > 0):
            data[column] = data[column].apply(lambda x: np.log(x))

        else:
            print(f" > Column: {column} = Cannot perform logaritmic transformation (Negative Number(s))")

    return data


def transform_exp(DF, c=3):
    """
    Perform Exponential transformation, raising the distribution by a
    power "c" (default=3) and could be a constant between 0 and 5.
    
    """
    data = DF.copy()

    for column in data.columns:
        data[column] = data[column].apply(lambda x: np.power(x, c))


    return data


def transform_boxcox(DF):
    """
    Performs Box-Cox Transformation. The lmbda is the value used to fit
    the non-gaussian distribution to gaussian distribution. If you wish
    to perform the inverse box-cox, you need this value.

    Equation: y = (x ** (lmbda - 1))/lmbda  for  lmbda != 0,
                   log(x)                   for  lmbda = 0,

    More info:
    https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.boxcox.html
    https://www.ime.usp.br/~abe/lista/pdfQWaCMboK68.pdf (An Analysis of Tranformations)
    
    """
    from scipy.stats import boxcox
    data = DF.copy()

    for column in data.columns:
        data_min = data[column].min()

        if(data_min > 0):
            data[column], lmbda = boxcox(data[column])

        else:
            print(f" > Column: {column} = Cannot perform logaritmic transformation (Negative Number(s))")

    return data


def transform_reciprocal(DF):
    """
    Performs a Reciprocal transformation using the INVERSE value.

    """
    data = DF.copy()

    for column in data.columns:
        data[column] = data.column.apply(lambda x: x ** (-1))

    return data

