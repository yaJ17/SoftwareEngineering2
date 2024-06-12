from databases.database import DatabaseManager

def run_login():
  username = "admins"
  password = "admins"

  host = 'localhost'
  user = 'root'
  password = 'admin'
  database = 'rexie'
  db = DatabaseManager(host, user, password)
  db.connect_to_database(database)

  db.check_account_login(username, password)
