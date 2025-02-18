import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
import nltk
from nltk.corpus import stopwords

from sklearn.multioutput import MultiOutputClassifier
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier, AdaBoostClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report
import pickle

"""Load data from database and return the data and labels in X and Y"""

def load_data(database_filepath):
    engine = create_engine('sqlite:///' + database_filepath)
    df = pd.read_sql_table('myTable', engine)

    X = df.message
    Y = df[df.columns[4:]]
    category_names = Y.columns
    return X,Y,category_names


"""Tokenize the text"""

def tokenize(text):
    nltk_tokens = nltk.word_tokenize(text)
    return nltk_tokens


"""Building the pipeline"""

def build_model():
    pipeline = Pipeline([
        ('vect', CountVectorizer(tokenizer=tokenize)),
        ('tfidf', TfidfTransformer()),
        ('clf', MultiOutputClassifier(RandomForestClassifier()))
        ])

    """Selecting a paremeter to perform gridsearch"""

    parameters = {
    'clf__estimator__n_estimators': [150, 200],
     }

     """Defining gridsearch with cv and n _jibs"""

    cv = GridSearchCV(pipeline, param_grid=parameters, cv=2, n_jobs=4, verbose=2)
    return cv
    # return pipeline


"""Print the report"""

def evaluate_model(model, X_test, Y_test, category_names):
    y_predict = model.predict(X_test)
    report = classification_report(Y_test, y_pred, target_names=category_names)
    print(report)
    # return y_predict

"""Save the model using pickle"""

def save_model(model, model_filepath):
    pickle.dump(model, open(model_filepath, 'wb'))


"""Define the sequence of program run"""

def main():
    if len(sys.argv) == 3:
        database_filepath, model_filepath = sys.argv[1:]
        print('Loading data...\n    DATABASE: {}'.format(database_filepath))
        X, Y, category_names = load_data(database_filepath)
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

        print('Building model...')
        model = build_model()

        print('Training model...')
        model.fit(X_train, Y_train)

        print('Evaluating model...')
        evaluate_model(model, X_test, Y_test, category_names)

        print('Saving model...\n    MODEL: {}'.format(model_filepath))
        save_model(model, model_filepath)

        print('Trained model saved!')

    else:
        print('Please provide the filepath of the disaster messages database '\
              'as the first argument and the filepath of the pickle file to '\
              'save the model to as the second argument. \n\nExample: python '\
              'train_classifier.py ../data/DisasterResponse.db classifier.pkl')


if __name__ == '__main__':
    main()
