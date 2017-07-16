# Newsworthy

## Purpose

The Newsworthy command-line application is designed to classify a piece of writing as either 'fake news' or 'real news' based on analysis of the language used in the piece, and machine learning classification algorithms.

## Prerequisites

Newsworthy is built using Python 3 and leveraging the following libraries - numpy, scipy, scikit-learn

## How to Run

* Clone/fork/download the repo as desired
* Open the terminal and navigate to the newsworthy-app directory
* Execute 'python3 running_scikit.py'
* Choose the percentage of the training data which will be used to train the model (in general, the higher percentage that is chosen, the more 'certain' the model should become in its classification)
* Paste in the piece of writing to classify as a string (if you want to scrape news stories from the web, please investigate the 'news_scraper.py' file and customise as required before executing)

## Authors

* Simon Ashbery - https://github.com/SiAshbery
* Christopher Harrop - https://github.com/bannastre
* Roland Grenke - https://github.com/rogrenke
* Colin Scally - https://github.com/cdscally

## Context

The application was developed by a team of 4 developers over the course of 4 days as part of the Makers Academy practice project week.

This project involved all members of the team picking up a new language (having no previous experience with Python) and learning a new concept (again no team member had experience with machine learning).

Having finished the week, we came away with a number of learnings:
* Data volume in machine learning is critical - without an efficient way to scrape news stories there was a large variance in confidence of results
* Assumptions made in training selection and classification of training data can easily bias outcomes. Without a rigid definition of fake news, we chose sources which are generally accepted to be 'real' and sources generally accepted to be 'fake'. However, we must acknowledge this is an assumption
* Binary classification is difficult where one class is focussed ('fake news' tends to revolve around politics, particularly America) and the other is broad ('real news' can be about any topic). This trained our model to tend to classify all news about American politics as 'fake'
