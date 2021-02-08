# Disaster-Respone-Pipelines

## Table of Contents
1. [Introduction](#introduction)
2. [Getting Started](#getting_started)
	1. [Dependencies](#dependencies)
	2. [Cloning](#cloning)
	3. [Executing Program](#execution)
3. [Author](#authors)
4. [License](#license)

<a name="introduction"></a>
## Introduction

This project aims to develop dissaster response pipeline system. There are three stages for this project

1. First create an ETL pipeline to prepare the data and save
2. ML pipeline to load the data, tokenize text and build the model
3. Deploy the final app on localhost using flask library.

<a name="getting_started"></a>

<a name="getting_started"></a>
## Getting Started

<a name="dependencies"></a>
### Dependencies
* Python 3.6+
* Visualization libraries: Matplotlib
* Libraries for data and array: pandas and numpy
* Machine learning libraries: Scikit-Learn
* Web App library: Flask
* Database library: sqlalchemy 
* NLP library: nlth 

<a name="cloning"></a>
### Cloning
To clone the git repository:
```
git clone https://github.com/mdsohelmahmood/Disaster-Respone-Pipeline
```

<a name="execution"></a>
### Executing Program:
ETL pipeline

* Import Python libraries
* Load messages.csv into a dataframe and inspect the first few lines.
* Load categories.csv into a dataframe and inspect the first few lines.
* Merge the messages and categories datasets using the common id
* Assign this combined dataset to df, which will be cleaned in the following steps
* Split categories into separate category columns
* Convert category values to just numbers 0 or 1.
* Replace categories column in df with new category columns
* Remove duplicates
* Save the clean dataset into an sqlite database

ML pipeline:

* Import Python libraries
* Load dataset from database with read_sql_table
* Define feature and target variables X and Y
* Write a tokenization function to process your text data
* Build a machine learning pipeline
* Train pipeline
* Test the model
* Improve the model
* Export the model as a pickle file

Flask app:

* In the last step, we will display your results in a Flask web app
* Visualizations are added for outputs


<a name="authors"></a>
## Author

* [Md Sohel Mahmood](https://github.com/mdsohelmahmood)

<a name="license"></a>
## License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
