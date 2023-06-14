# Kayak Trip Planning - Project on Extract, Transform and Load

![python-shield](https://forthebadge.com/images/badges/made-with-python.svg)  


## Table of contents
* [Project](#project)
* [Pipeline](#pipeline)
* [Deliverables](#deliverables)  
* [Technologies](#technologies)  
* [Getting Started](#getting-started)  
* [License](#license)  
* [Author](#author)  

## Project 🚧   

Kayak is a travel search engine that helps user plan their trip at the best price. Founded in 2004, Kayak was acquired by Booking Holdings later on. With over $300 million revenue a year, Kayak operates in almost all countries and all languages to help their users book travels accros the globe.

The marketing team needs help on a new project. After doing some user research, the team discovered that 70% of their users who are planning a trip would like to have more information about the destination they are going to. Therefore, Kayak Marketing Team would like to create an application that will recommend where people should plan their next holidays.  

The goal is to create an app that will recommend users where to plan their next holidays. It takes real up-to-date data on Weather and Hotels in the area. The application will recommend the best destinations and hotels in France.  

Tasks:

Scraping location information, acquiring up-to-date weather information and accessing to hotel information in each destination
All the data will be stored in a data lake in cloud. ETL process will be run from datalake to a data warehouse. 

## Pipeline  

<img src = ".pipeline_summary.png">

## Deliverables  

Availabe deliverables 📬:  

1- Two maps with TOP 5 destinations and TOP 20 hotels in the area  
2- A .csv file in an S3 bucket containing enriched information about weather and hotels for each French city  
3- A SQL Database to get the cleaned data from S3  

## Technologies

Project is created with:
* Python
* Jupyter Notebook
* Python libraries (see /requirements.txt)
* VSCode 1.71.2
* Amazon AWS + RDS

or this github project can be launched on [colab-google](https://colab.research.google.com) without any local installations. It is free and requires Google account sign-in.  

## Getting Started

To run this project, 
1. Clone the repo:
   ```sh
   git clone https://github.com/levist7/Kayak_ETL_Project.git
   ```
2. Install [packages](#technologies)

3. Install python libraries
   ```sh
   pip3 install -r requirements.txt
   ```

## License

Distributed under the MIT License. See LICENSE.txt for more information.

## Author  

* [levist7](https://github.com/levist7)  
---
Made with ❤️ in Paris
---
