# Data Processing and Storage Assignment

## Overview
This project implements an **in-memory key-value database** with transaction support. The database supports basic operations such as `put`, `get`, and transaction management (`begin_transaction`, `commit`, `rollback`).

## Features

### Key-Value Store
- **Keys**: Strings.
- **Values**: Integers.

### Transaction Support
- **Commit**: Changes are only applied to the database after calling `commit`.
- **Rollback**: Changes can be discarded using `rollback`.
- **Safety**: Allows for safe multi-step operations with all-or-nothing behavior.

### Exceptions
- Calling `put` outside of a transaction raises an exception.
- Attempting to `commit` or `rollback` without an active transaction raises an exception.

## Usage

### Prerequisites
- Python 3.6 or higher.
- If you need to install Python 3.6 or higher, run the following command in your terminal:
   ```bash
   sudo apt-get install python3


### Steps to Run
1. Clone the repository or download the script.
2. Save the script as `data_processing.py`.
3. Open a terminal and navigate to the folder containing the script.
4. Run the script:
   ```bash
   python3 data_processing.py
   
## Improving This Assignment

To improve this assignment to become an official assignment,  a few enhancements could be added. Adding an automated test cases using frameworks like `unittest` or `pytest` could help validate the functionality of each method and ensure that the functions are done correctly. Including examples of expected inputs and outputs in the assignment instructions would clarify requirements and reduce confusion. Furthermore having methods, such as `delete(key)` to remove entries and `size()` to return the count of entries, could expand the assignment's scope. This might be a too much but allowing for nested transactions would simulate real-world database scenarios which could be good. 


