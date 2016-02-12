import csv
import pandas as pd
def readCsv(output_file):
    '''
    f = open(output_file, 'rb')

    dataReader = csv.reader(f)
    for row in dataReader:
       print row; print'\n'
    '''
    df = pd.read_csv(output_file, header=None, delimiter=',', quotechar='\"')
    # print df
    data = df.ix[:,1:3]
    # print data

    for column in df:
        print(df[column])




if __name__ == '__main__':
    output_file = '201605010411.csv'
    readCsv(output_file)
