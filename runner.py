from databases.database import DatabaseManager
from logic.login_module import run_login
from Crypto.Random import get_random_bytes

# Usage example
if __name__ == "__main__":
    key = b'[Xd\xee[\\\x90\x8c\xc8t\xba\xe4\xe0\rR\x87\xe6\xbe\xce\x8a\x02lC6\xf7G\x15O\xca\x182\xd0'
    db_manager = DatabaseManager('localhost', 'root', 'admin', key)
    db_manager.connect_to_database()
    db_manager.create_schema_and_tables()
    # db_manager.add_dummy_data()
    

    # db_manager.populate_accounts()
    # db_manager.populate_orders()
    # db_manager.populate_raw_materials()
    # db_manager.populate_bag_components()
    # db_manager.populate_deadline_by_month('12', '2024')
    # db_manager.populate_deadline_by_week('2024-12-15', '2024-12-21')

    # db_manager.set_client_detail(1, 'xdxd account', 'vb', '123123')
    # db_manager.populate_client()
    # db_manager.add_client('marx', 'taytay', '111', 2)
    # db_manager.set_client_detail(7, 'Karren', '3333', 2)
    #db_manager.add_raw_material('NGIin', 25, 15, 'leather', 144, 50, 1, 'red')
    #db_manager.set_product(4, "123", 123, 123123,12312,12312312)
    #db_manager.add_order(1, 234, 30, 'A')
    # db_manager.set_order(1, 1222, 70, 'F')
    # db_manager.set_raw_material(5, 'NGasdasdIin', 255, 366, 788, 'marx', '123123123')
    #db_manager.populate_raw_materials()
    """ DEMONSTRATION """
    #db_manager.populate_orders()
    #db_manager.populate_bag_components()
    # db_manager.add_account('sssssss', 'Pass!aaaaa123123', 'asda','asd')
    # db_manager.add_deadline('new dedline', 'asdasdas', '2024-12-15')
    #db_manager.set_deadline(1,'jay','asd','2025-12-12',1)
    # db_manager.void_deadline(1)
    # db_manager.add_raw_material('asda',123,123,'leather',123,123123,1,'black')
    # db_manager.void_raw_material(2)
    # db_manager.add_product(1, 123123,'b',12312,123,11111)
    # db_manager.set_product(7, 'Running',123,123123,1231231,123123)
    # db_manager.populate_product()
    # db_manager.void_product(1)
    db_manager.add_transaction(1, "transaction c")
    db_manager.populate_transaction()
    db_manager.close_connection()
