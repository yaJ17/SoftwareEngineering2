from databases.database import DatabaseManager
from logic.login_module import run_login
from Crypto.Random import get_random_bytes

# Usage example
if __name__ == "__main__":
    key = b'[Xd\xee[\\\x90\x8c\xc8t\xba\xe4\xe0\rR\x87\xe6\xbe\xce\x8a\x02lC6\xf7G\x15O\xca\x182\xd0'
    db_manager = DatabaseManager('localhost', 'root', 'admin', key)
    db_manager.connect_to_database()
    db_manager.create_schema_and_tables()
    #db_manager.add_dummy_data()
    

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
    db_manager.set_product(4, "123", 123, 123123,12312,12312312)
    #db_manager.add_order(1, 234, 30, 'A')
    # db_manager.set_order(1, 1222, 70, 'F')
    #db_manager.set_raw_material(5, 'NGasdasdIin', 255, 366, 788, 'marx', '123123123')

    """ DEMONSTRATION """
    #db_manager.add_client('Teleperformance', 'Quezon City', '0931239222', 2)
    #db_manager.set_client_detail(8, 'New New Client', 'Bulacan', '123123' )
    db_manager.close_connection()
