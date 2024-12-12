class InMemoryDB:
    def __init__(self):
        self.main_state = {}
        self.transaction_state = None
        self.in_transaction = False

    def begin_transaction(self):
        if self.in_transaction:
            raise Exception("Transaction already in progress.")
        self.transaction_state = self.main_state.copy()
        self.in_transaction = True

    def put(self, key, value):
        if not self.in_transaction:
            raise Exception("No active transaction. Cannot put value.")
        self.transaction_state[key] = value

    def get(self, key):
        if self.in_transaction:
            return self.transaction_state.get(key)
        return self.main_state.get(key)

    def commit(self):
        if not self.in_transaction:
            raise Exception("No active transaction. Cannot commit.")
        self.main_state = self.transaction_state
        self.transaction_state = None
        self.in_transaction = False

    def rollback(self):
        if not self.in_transaction:
            raise Exception("No active transaction. Cannot rollback.")
        self.transaction_state = None
        self.in_transaction = False


# Example Usage
if __name__ == "__main__":
    db = InMemoryDB()

    # Test cases based on assignment examples
    print(db.get("A"))  # Should return None
    try:
        db.put("A", 5)  # Should raise an exception
    except Exception as e:
        print(e)

    db.begin_transaction()
    db.put("A", 5)
    print(db.get("A"))  # Should return 5 (within the transaction)

    db.put("A", 6)
    db.commit()
    print(db.get("A"))  # Should return 6 (after commit)

    try:
        db.commit()  # Should raise an exception
    except Exception as e:
        print(e)

    db.begin_transaction()
    db.put("B", 10)
    db.rollback()
    print(db.get("B"))  # Should return None (after rollback)
