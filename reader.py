
import pandas as pd
def read_file(file_name):
    ''' Reads the csv file of user input using pandas and returns the data as data set

    :param file_name:
        User inputted string
    :return:
        Returns pandas data set read from user input
    '''
    df = pd.read_csv(file_name)
    return df
