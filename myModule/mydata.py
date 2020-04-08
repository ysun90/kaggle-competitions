import pandas as pd

def display_all(df):
    with pd.option_context("display.max_rows", 1000, 
                           "display.max_columns", 1000): 
        print(df)

class Data:
    """Organize traning and test data for EDA and traning.
    
    Attributes:
    path: data path
    train: traning data 
    test: testing data 
    """
    def __init__(self, path='', 
                 train='train.csv', test='test.csv'):
        self.path = path
        self.train = pd.read_csv(path + train)
        self.test = pd.read_csv(path + test)
      
    def get_df_train(self):
        return self.train
    
    def get_df_test(self):
        return self.test
    
    def get_text_train(self, col):
        return self.train[col].values

    def get_text_test(self, col):
        return self.test[col].values

def main():
    data = Data()

if __name__ == '__main__':
    main()
