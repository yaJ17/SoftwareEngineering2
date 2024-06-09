from connect import DatabaseManager

def main():

    host = 'localhost'
    user = 'root'
    password = 'admin'
    database = 'rexie'

    db_manager = DatabaseManager(host, user, password,)
    
    # Connect to MySQL server (without specifying a database)
    db_manager.connect_to_database(database)
    
    # Create schema and insert data
    db_manager.create_schema()
    db_manager.print()
    # Close the connection

    db_manager.close_connection()

if __name__ == "__main__":
    main()
