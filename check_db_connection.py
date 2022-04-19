import pymysql

from fixture.db import DbFixture

db = DbFixture(host='127.0.0.1', name='bugtracker', user='root', password='')

try:
    l = db.get_project_list()
    # for item in l:
    #     print(item)
    # print(len(l))
    print(l)
finally:
    pass  # db.destroy()