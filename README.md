# Sentiment analysis project with machine learning

## Abstract

This is a simple project that uses artificial intelligence models that analyze feelings expressed in Portuguese sentences. Two models were created, one based on a Bayesian algorithm and the other based on a logistic regression algorithm.

## Main technologies used
- Python 3.8
- Django 4.1.4
- scikit-learn 1.2.0 

## Instructions for using this project on your machine

1º) Clone the repository with the following command:
~~~
git clone https://github.com/NascimentoFrancisco/sentiment-analysis.git
~~~

2º) Open it in your favorite editor and create and activate the virtualenv
> Windows:

Creation
~~~
python -m venv venv
~~~
Activation
~~~
venv\Scripts\activate
~~~

> Linux:

Creation
~~~
python3 -m venv venv
~~~
Activation
~~~
. venv/bin/activate
~~~

3º) Install the dependencies
~~~
pip install -r requirements.txt
~~~

4º) Make the migrations and migrate

~~~
python manage.py makemigrations
~~~
~~~
python manage.py migrate
~~~

5º) Start the server and access the link

~~~
python manage.py runserver
~~~
~~~
http://127.0.0.1:8000/
~~~