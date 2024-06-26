import psycopg2
from env import POSTGRES_DB, POSTGRES_USER, POSTGRES_PASSWORD


conn = psycopg2.connect(f"dbname={POSTGRES_DB} user={POSTGRES_USER} host=db password={POSTGRES_PASSWORD}")
cursor = conn.cursor()
