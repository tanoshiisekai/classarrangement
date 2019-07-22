from appbase import global_db as gdb

def create_db():
    gdb.create_all()

    
