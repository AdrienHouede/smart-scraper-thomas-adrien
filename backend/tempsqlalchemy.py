from sqlalchemy import create_engine, inspect

# Format : dialect+driver://user:password@host:port/dbname
engine = create_engine("mysql+pymysql://user:userpass@localhost:3306/paris_scraping")

# Inspecter la base
inspector = inspect(engine)
tables = inspector.get_table_names()

print("Tables dans la base :", tables)