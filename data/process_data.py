import sys
import pandas as pd
import numpy as np
from string import digits
from sqlalchemy import create_engine


"""Function for loading data """

def load_data(messages_filepath, categories_filepath):
    messages = pd.read_csv(messages_filepath)
    categories = pd.read_csv(categories_filepath)

    """Merege two datasets using common id and split the data by ;"""

    df = pd.merge(messages , categories, on="id")
    categories = df['categories'].str.split(';', expand=True)

    """Select the first row of the categories dataframe and use
    this row to extract a list of new column names for categories"""

    row = categories.iloc[0]
    category_colnames = [category_name for category_name in row]

    """Remove numbers and dash('-')"""

    for i in range(0,len(category_colnames),1):
        remove_digits = str.maketrans('', '', digits)
        category_colnames[i]= category_colnames[i].translate(remove_digits)
        category_colnames[i] = category_colnames[i].replace('-','')

    """Convert category values to numbers 0 or 1."""

    categories.columns = category_colnames
    for column in categories:
        """Set each value to be the last character of the string"""

        categories[column] = categories[column].astype(str).str[-1:]

        """Convert column from string to numeric"""

        categories[column] = categories[column].astype(int)

    """Replace categories column in df with new category columns"""

    df=df.drop(['categories',], axis=1)
    df = pd.concat([df,categories],axis=1)
    return df


"""Drop duplictes and convert to binary"""

def clean_data(df):
    df=df.drop_duplicates()

    for i in range(4,df.shape[1],1):
        df.loc[df[df.columns[i]] > 1, df.columns[i]] = 1

    return df

"""Save the data to the SQLite database with a Table name"""

def save_data(df, database_filename):
    engine = create_engine('sqlite:///' + database_filename)
    df.to_sql('myTable', engine, index=False, if_exists='replace')


def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)

        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)

        print('Cleaned data saved to database!')

    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()
