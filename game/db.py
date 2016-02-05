import MySQLdb
from _mysql_exceptions import IntegrityError

connect = MySQLdb.connect(host='localhost', user='root', passwd='1111', db='game')
connect.autocommit(True)
