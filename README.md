# Span Coding Challenge
# Code by Christopher Sommerville

## About
A project focusing on interacting with/modifying examples of push notifications for a Span system.

This project is written in Python 3.9.0.

Part 1 of the project involved converting notifications in `.json` format from a legacy format to a new 2.0 format.
Part 2 of the project involved removing duplicate notifications (in the new 2.0 format) based on select criteria.
Part 3 of the project inolved sorting a list of new format notifications based on select criteria.

## Code structure
The bulk of the code for the functionality of the project is contained within the `src` folder in the `NotificationModFunctions.py` file. This file contains all of the functions necessary for the three parts of the challenge. The rest of the `.py` files in the `src` folder import functions from the `NotificationModFunctions.py` file in order to solve each part of the coding challenge.
Unit tests are included in the file `testing.py` within the `src` folder with the test data being contained in the `tests` folder. 

## How to run
Within the `src` folder, the files `convert_notifications.py`, `deduplication.py`, and `sort_notifications.py` contain executable Python code which brings up the command line and allows the user to specify an input file (or use the default data in the `data` folder) and specify an output file (or output the results to the console). Any output files specified are sent to the main directory where this readme is located. No third-party libraries were used for any part of the project so the files are ready to run as-is and all of the necessary instructions are explained when running the files.

