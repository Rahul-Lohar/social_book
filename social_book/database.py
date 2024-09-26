from sqlalchemy import create_engine # type: ignore
from sqlalchemy import text # type: ignore


USER = 'rahul'
PASSWORD = 'rahul2002'
HOST = 'localhost'
PORT = '5432'
DATABASE = 'social_book'

engine = create_engine(f'postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}')


def fetch_data(query):
    with engine.connect() as connection:
        result = connection.execute(text(query))
        return result.fetchall()
    
    
if __name__ == "__main__":
    query = "SELECT * FROM books;"
    try:
        data = fetch_data(query)
        print("Data fetched successfully:")
        for row in data:
            print(row)
    except Exception as e:
        print(f"Error fetching data: {e}")
        
        
