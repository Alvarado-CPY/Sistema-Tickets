import sqlite3
import os


class BBDD:
    def __init__(self) -> None:
        self.db_path = os.path.join(".", "database", "workers.db")

    def generateDatabaseTables(self):
        tables = (
            self.tableUsers(),
            self.tableActiveUser(),
            self.tableUserRecord(),
            self.tableWorkers(),
            self.tableNewIncome(),
            self.tableSuspensions(),
            self.tableReactivations(),
            self.tableDischarge(),
            self.tableTickets(),
        )

        with sqlite3.connect(self.db_path) as bd:
            cursor = bd.cursor()
            for create_table in tables:
                cursor.execute(create_table)

            bd.commit()

    def tableUsers(self):
        return """CREATE TABLE IF NOT EXISTS users(
            user_id INTEGER PRIMARY KEY,
            user_ci INTEGER,
            username STRING,
            password STRING,
            user_level INTEGER
        )"""

    def setDefaultUser(self, password):
        with sqlite3.connect(self.db_path) as bd:
            cursor = bd.cursor()
            user = cursor.execute("SELECT * FROM users").fetchone()

            if user == None:
                cursor.execute("INSERT INTO users VALUES(?,?,?,?,?)",
                               (None, 123, "admin", password, 0))
                bd.commit()

    def tableActiveUser(self):
        return """CREATE TABLE IF NOT EXISTS active_user(
            user_id INTEGER PRIMARY KEY
        )"""

    def tableUserRecord(self):
        return """CREATE TABLE IF NOT EXISTS record(
            user_id INTEGER PRIMARY KEY,
            user_action STRING,
            date DATE
        )"""

    def tableWorkers(self):
        return """CREATE TABLE IF NOT EXISTS workers(
            worker_id INTEGER PRIMARY KEY,
            nationality STRING,
            worker_ci INTEGER,
            worker_fullname STRING,
            birthday DATE,
            age INTEGER,
            gender STRING,
            admission_date DATE,
            title_of_position STRING,
            workload STRING,
            working_hours STRING,
            specialty STRING,
            type_of_staff STRING,
            administrative_location STRING,
            physical_location STRING,
            service_commission STRING,
            state STRING,
            bank_account STRING,
            bank_code STRING,
            bank STRING
        )"""

    def tableNewIncome(self):
        return """CREATE TABLE IF NOT EXISTS newIncome(
            worker_ci INTEGER PRIMARY KEY,
            account_type STRING
        )"""

    def tableReactivations(self):
        return """CREATE TABLE IF NOT EXISTS reactivations(
            worker_ci INTEGER PRIMARY KEY,
            account_type STRING,
            reactivation_date DATE
        )"""

    def tableSuspensions(self):
        return """CREATE TABLE IF NOT EXISTS suspensions(
            worker_ci INTEGER PRIMARY KEY,
            desincorporation_date DATE,
            suspension_reason STRING,
            support_number INTEGER
        )"""

    def tableDischarge(self):
        return """CREATE TABLE IF NOT EXISTS discharge(
            worker_ci INTEGER PRIMARY KEY,
            discharge_date DATE,
            discharge_reason STRING,
            support_number INTEGER
        )"""

    def tableTickets(self):
        return """CREATE TABLE IF NOT EXISTS tickets(
            worker_ci INTEGER PRIMARY KEY,
            payment_date DATE,
            tickets INTEGER
        )"""
