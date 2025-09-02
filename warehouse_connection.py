server = [server name goes here]
database = [database goes here]
connection_string = ('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+
                    ';DATABASE='+database+
                    ';ENCRYPT=no;TRUSTED_CONNECTION=yes;'
   )
connection_url = sa.engine.URL.create(
   "mssql+pyodbc",
   query=dict(odbc_connect=connection_string)
   )
engine = sa.create_engine(connection_url, fast_executemany= True)
query = '''
        SELECT * FROM [Database].[Schema].[Table]
       '''
df = pd.read_sql(query, engine)