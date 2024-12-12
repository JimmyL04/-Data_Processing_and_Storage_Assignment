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

## Results and Explanation

### Results
```css
None
No active transaction. Cannot put value.
5
6
No active transaction. Cannot commit.
None
```
## Explanation of Results

### First Output: `None`
This is the result of calling `db.get("A")` when key "A" does not exist in the database. Since no value has been assigned to "A", the `get` method correctly returns `None`.

### Second Output: `No active transaction. Cannot put value.`
This occurs because `db.put("A", 5)` is called outside of a transaction. The program raises an exception, as the `put` method is only allowed during an active transaction.

### Third Output: `5`
After starting a transaction with `db.begin_transaction()` and assigning `db.put("A", 5)`, the `get` method retrieves the value of "A" within the transaction. The value `5` is visible only within the active transaction.

### Fourth Output: `6`
The value of "A" is updated to `6` using `db.put("A", 6)` within the same transaction. After committing the transaction with `db.commit()`, the change is saved to the main state. When `db.get("A")` is called again, it returns the committed value `6`.

### Fifth Output: `No active transaction. Cannot commit.`
This occurs because `db.commit()` is called without an active transaction. The program raises an exception, as there is no transaction to commit.

### Sixth Output: `None`
A new transaction is started, and the value of "B" is set to `10` with `db.put("B", 10)`. However, this transaction is rolled back with `db.rollback()`, discarding all changes. When `db.get("B")` is called, it returns `None`, as the key "B" does not exist in the main state after the rollback.


   
## Improving This Assignment

To improve this assignment to become an official assignment,  a few enhancements could be added. Adding an automated test cases using frameworks like `unittest` or `pytest` could help validate the functionality of each method and ensure that the functions are done correctly. Including examples of expected inputs and outputs in the assignment instructions would clarify requirements and reduce confusion. Furthermore having methods, such as `delete(key)` to remove entries and `size()` to return the count of entries, could expand the assignment's scope. This might be a too much but allowing for nested transactions would simulate real-world database scenarios which could be good. 


