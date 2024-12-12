# Data Processing and Storage Assignment 

This project implements an in-memory key-value database with transaction support. The database supports basic operations such as put, get, and transaction management (begin_transaction, commit, rollback).

Features
Key-Value Store: Keys are strings, and values are integers.


Transaction Support:
Changes are only applied to the database after commit.
Changes can be discarded using rollback.
Safe multi-step operations with all-or-nothing behavior.


Exceptions:
Calling put outside of a transaction raises an exception.
Attempting to commit or rollback without an active transaction raises an exception.


Usage
Prerequisites
Python 3.6 or higher is required to run the code.
Steps to Run
Clone the repository or download the script.
Save the script as data_processing.py
Open a terminal and navigate to the folder containing the script.

Run the script: 
python3 data_processing.py  


Improving This Assignment 
I think having some method of testing out code to ensure that the funcitons we made worked would be good to add to the assignment. This could look like adding descriptions of test cases with expected outputs. For my own project, I tried writing tests cases so that when the file is ran, the cases are automatically ran through and displays the results in the terminal. 
