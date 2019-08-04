# -*- coding: utf-8 -*

import sys
import re
import unicodedata

from Table import Table
import settings

reload(sys)
sys.setdefaultencoding("utf-8")


class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


class Database:

    def __init__(self):
        self.tables = []

    def get_number_of_tables(self):
        return len(self.tables)

    def get_tables(self):
        return self.tables

    def get_tables_into_dictionnary(self):
        data = {}
        for table in self.tables:
            data[table.name] = []
            for column in table.columns:
                data[table.name].append(column.name)
        return data

    def get_primary_keys_by_table(self):
        data = {}
        for table in self.tables:
            data[table.name] = table.primary_keys
        return data

    def get_primary_keys_of_table(self, table):
        for _table in self.tables:
            if _table.name == table:
                return _table.primary_keys

    def get_foreign_keys_of_table(self, table):
        for _table in self.tables:
            if _table.name == table:
                return _table.get_foreign_keys()

    def add_table(self, table):
        self.tables.append(table)

    def load(self, path):
        with open(path) as f:
            content = f.read()

            tables_string = [p.split(';')[0]
                             for p in content.split('CREATE') if ';' in p]
            for table_string in tables_string:
                if 'TABLE' in table_string:
                    table = self.create_table(table_string)
                    self.add_table(table)

            alter_table_string = [p.split(';')[0]
                                  for p in content.split('ALTER') if ';' in p]
            for s in alter_table_string:
                if 'TABLE' in s:
                    self.alter_table(s)

    def predict_type(self, string):
        if 'int' in string.lower():
            return 'int'
        elif 'char' in string.lower() or 'text' in string.lower():
            return 'string'
        elif 'date' in string.lower():
            return 'date'
        else:
            return 'unknow'

    def create_table(self, table_string):
        lines = table_string.split("\n")
        table = Table()
        for line in lines:
            if 'TABLE' in line:
                table_name = re.search("`(\w+)`", line)
                table.set_name(table_name.group(1))
            elif 'PRIMARY KEY' in line:
                primary_key_columns = re.findall("`(\w+)`", line)
                for primary_key_column in primary_key_columns:
                    table.add_primary_key(primary_key_column)
            else:
                column_name = re.search("`(\w+)`", line)
                if column_name is not None:
                    column_type = self.predict_type(line)
                    table.add_column(column_name.group(1), column_type)
        return table

    def alter_table(self, alter_string):
        lines = alter_string.replace('\n', ' ').split(';')
        for line in lines:
            if 'PRIMARY KEY' in line:
                table_name = re.search("TABLE `(\w+)`", line).group(1)
                table = [t for t in self.tables if t.get_name() == table_name][
                    0]

                primary_key_columns = re.findall(
                    "PRIMARY KEY \(`(\w+)`\)", line)
                for primary_key_column in primary_key_columns:
                    table.add_primary_key(primary_key_column)
            elif 'FOREIGN KEY' in line:
                table_name = re.search("TABLE `(\w+)`", line).group(1)
                table = [t for t in self.tables if t.get_name() == table_name][
                    0]

                foreign_keys_list = re.findall(
                    "FOREIGN KEY \(`(\w+)`\) REFERENCES `(\w+)` \(`(\w+)`\)", line)

                for col, ref_table, ref_col in foreign_keys_list:
                    table.add_foreign_key(col, ref_table, ref_col)

    def print_me(self):
        if settings.DEBUG:
            for table in self.tables:
                print('+-------------------------------------+')
                print("| %25s           |" % (table.name.upper()))
                print('+-------------------------------------+')
                for column in table.columns:
                    if column.name in table.primary_keys:
                        print("| 🔑 %31s           |" % (
                            color.BOLD + column.name + ' (' + column.type + ')' + color.END))
                    else:
                        print("|   %23s           |" %
                              (column.name + ' (' + column.type + ')'))
                print('+-------------------------------------+\n')
