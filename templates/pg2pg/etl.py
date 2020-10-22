from pg2pg.ss import data_import as di
from pg2pg.store import data_export as de
# import pg2pg.ss.data_import as di

def to_stage():
    di.main()
    
def to_dwh():
    de.main()

def main():
    pass

if __name__ == "__main__":
    main()