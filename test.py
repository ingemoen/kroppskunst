import pymssql
import os

sqlServer = os.getenv('SQL_SERVER', 'none')
sqlUser = os.getenv('SQL_USER', 'none')
sqlPass = os.getenv('SQL_PASS', 'none')
sqlDb = os.getenv('SQL_DB', 'none')

def db():
    return pymssql.connect(server=sqlServer, user=sqlUser, password=sqlPass, database=sqlDb)

def mySqlQuery(query, one=False):
    cur = db().cursor()
    cur.execute(query)
    r = [dict((cur.description[i][0], value) \
               for i, value in enumerate(row)) for row in cur.fetchall()]
    cur.connection.close()
    return (r[0] if r else None) if one else r


res = mySqlQuery('dbo.sp_ProductsGet_v3_00 @guid=76393978, @language=no, @page=0, @level0=1, @level1=1, @level2=185, @qtyin=12')

print(res)