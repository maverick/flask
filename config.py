import os

host = os.environ.get('MYSQL_HOST')
user = os.environ.get('MYSQL_USER')
password = os.environ.get('MYSQL_PASSWORD')
sa_user = os.environ.get('MYSQL_SA_USER')
sa_password = os.environ.get('MYSQL_SA_PASSWORD')
database = os.environ.get('MYSQL_DB')
port = os.environ.get('MYSQL_PORT') or 3306

DATABASE_CONNECTION_URI = f'mysql://{user}:{password}@{host}:{port}/{database}'

DATABASE_SA_CONNECTION_URI = f'mysql://{sa_user}:{sa_password}@{host}:{port}/{database}'

print(DATABASE_CONNECTION_URI)
print(DATABASE_SA_CONNECTION_URI)
