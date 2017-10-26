from ln2sql import main as __main__
import re


def getSql(query):
    # unit test
    # args = ['-d', 'ln2sqlmodule/emp_dump.sql', '-l', 'ln2sqlmodule/lang/english.csv', '-i', query, '-j', 'ln2sqlmodule/output.json','-x']
    # args = ['-d', 'ln2sqlmodule/emp_dump.sql', 'ln2sqlmodule/lang/english.csv', '-i', query, '-j', 'ln2sqlmodule/output.json']

    # args = ['-d', 'ln2sqlmodule/timesheet.sql', '-l',
    #         'ln2sqlmodule/lang/english.csv', '-i', query, '-j', 'ln2sqlmodule/output.json']

    args = ['-d', 'ln2sqlmodule/heyzot-analytics.sql',
            '-l', 'ln2sqlmodule/lang/english.csv', 
            '-i', query, 
            '-j', 'ln2sqlmodule/output.json']

    sql = __main__(args)

    return str(sql)


def getSql_like(query):
    sql = getSql(query)

    sql = sql.replace('=', 'LIKE')

    # 'abc def' -> '%abc%def%'
    for i in re.findall("'(.*?)'", sql):
        sql = sql.replace(i, "%" + i + "%")
        sql = sql.replace(i,i.replace(' ','%'))

    return sql
