# Green computing Python REST API

Fully functional CRUD RESTful API with Flask and SQLAlchemy.
CodeCarbon package is installed to track CO2 emissions.

## Prerequisites
You need Python installed, you can check it with python command, I have the 3.8 version:
```
$ python
Python 3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:48:03) [MSC v.1928 64 bit (AMD64)] on win32
```
You also need to have Flask installed (CMD or Powershell in Windows)
```
pip install Flask
pip install -r .\requirements.txt --upgrade
```

## Run in local
To run the api:
```
flask run
```
When the api is started you can call endpoint opening in your browser http://127.0.0.1:5000/
(For example http://127.0.0.1:5000/health).
You can check the emissions in your terminal logs and in the emission.csv file.