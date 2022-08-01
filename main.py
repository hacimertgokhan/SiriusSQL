import mysql.connector
import sys

if __name__ == '__main__':
    while True:

        runFast = input("SiriusSQL: You can enter your mysql database with fast way. (Yes:Y|No:N) ")

        if runFast == 'Y' or 'y':

            file = open("siriussql.txt").readlines()
            username = ""
            password = ""
            host = ""
            dbase = ""

            for lines in file:
                if 'Username' in lines:
                    username = lines.split(":")[-1].strip()
                if 'Password' in lines:
                    password = lines.split(":")[-1].strip()
                if 'Host' in lines:
                    host = lines.split(":")[-1].strip()
                if 'Database' in lines:
                    dbase = lines.split(":")[-1].strip()

            print("MYSQL: Trying to connect your database...")
            config = {
                'user': username,
                'password': password,
                'host': host,
                'database': dbase,
                'raise_on_warnings': True
            }
            cnx = mysql.connector.connect(**config)
            if cnx.is_connected():
                print("Connection success.")
                print("About database:")
                print("   User Name: " + cnx.user)
                print("   DBase: " + cnx.database)
                print("   Host: " + cnx._host)
                print(" ")
                print("Commands: ")
                print(" Commands for MySQL")
                print(" > $db-list")
                print(" ")
                print(" Commands for SiriusSQL")
                print(" > $databases")
                print(" ")
                command = input("MySQL Command Panel: ")
                if command == '$db-list':
                    cursor = cnx.cursor()
                    databases = "show databases"
                    cursor.execute(databases)
                    print("Your mysql databases...")
                    for (databases) in cursor:
                        var = databases[0]
                        print(" #--> " + var)
                elif command == '$enter-db':
                    databaseName = input("MYSQL: Enter your mysql database name: ")
                    cursor = cnx.cursor()
                    cursor.execute("select database();")
                    database_name = cursor.fetchone()
                    print("MYSQL: Selected database: ")
                    print(database_name.__str__())
                    print("Commands for " + databaseName)
                    print("   -> $list-table")
                    print("   -> $insert")
                    print("   -> $delete")
                    print("")
                    enterDB_MYSQLDBCommand = input("MYSQL / " + databaseName + " | Command Panel: ")
                    if enterDB_MYSQLDBCommand == '$list-table':
                        cursor = cnx.cursor()
                        databases = "show tables;"
                        cursor.execute(databases)
                        result = cursor.fetchall()
                        print("MYSQL: Table list for " + databaseName)
                        for x in result:
                            print(x)
                    elif enterDB_MYSQLDBCommand == '$insert':
                        cursor = cnx.cursor()
                        valueCount = input("MYSQL / " + databaseName + " | How many values will you enter ? ")
                        if valueCount == '1':
                            value = input("MYSQL / " + databaseName + " | Please enter a table name. ")
                            print("MYSQL / " + databaseName + " | Example: INSERT INTO " + value + " (>>:TARGET:name<<) VALUES (Jhon)")
                            mxr_value = input("MYSQL / " + databaseName + " | Please enter a target. ")
                            print("MYSQL / " + databaseName + " | Example: INSERT INTO " + value + " (>>:TARGET:name<<) VALUES (>>:TARGET_VALUE:Jhon<<)")
                            mxr_targetValue = input("MYSQL / " + databaseName + " | Please enter a target value. ")
                            sql = "INSERT INTO " + value + " (" + mxr_value + ") VALUES (" + mxr_targetValue + ")"
                            cursor.execute(sql)

                            cnx.commit()

                            print(cursor.rowcount, " record inserted.")
                        elif valueCount == '2':
                            value = input("MYSQL / " + databaseName + " | Please enter a table name. ")
                            mxr_value = input("MYSQL / " + databaseName + " | Please enter a first target.")
                            mxr_value_2 = input("MYSQL / " + databaseName + " | Please enter a second target.")
                            print("MYSQL / " + databaseName + " | Example: INSERT INTO " + value + " (>>:TARGET:name<<) VALUES (Jhon)")
                            mxr_targetValue = input("MYSQL / " + databaseName + " | Please enter a first target value.")
                            mxr_targetValue_2 = input("MYSQL / " + databaseName + " | Please enter a second target value.")
                            print("MYSQL / " + databaseName + " | Example: INSERT INTO " + value + " (>>:TARGET:name<<) VALUES (>>:TARGET_VALUE:Jhon<<)")
                            sql = "INSERT INTO " + value + " (" + mxr_value + "," + mxr_value_2 + ") VALUES (%s, %s)"
                            val = (mxr_targetValue, mxr_targetValue_2)
                            cursor.execute(sql, val)

                            cnx.commit()

                            print(cursor.rowcount, " record inserted.")
            else:
                print("Connection declined.")
                cnx.close()

        elif runFast == 'N' or 'n':
            username = input("MYSQL: Enter mysql user name: ")
            password = input("MYSQL: Enter mysql user password: ")
            host = input("MYSQL: Enter mysql host address: ")
            dbase = input("MYSQL: Enter mysql database name: ")
            lastQ = input("MYSQL: Is the above information correct? (Yes:Y|No:N) ")
            if lastQ == 'Y' or 'y':
                print("MYSQL: Trying to connect your database...")
                config = {
                    'user': username,
                    'password': password,
                    'host': host,
                    'database': dbase,
                    'raise_on_warnings': True
                }
                cnx = mysql.connector.connect(**config)
                if cnx.is_connected():
                    print("Connection success.")
                    print("About database:")
                    print("   User Name: " + cnx.user)
                    print("   DBase: " + cnx.database)
                    print("   Host: " + cnx._host)
                    print(" ")
                    print("Commands: ")
                    print(" Commands for MySQL")
                    print(" > $db-list")
                    print(" ")
                    print(" Commands for SiriusSQL")
                    print(" > $databases")
                    print(" ")
                    command = input("MySQL Command Panel: ")
                    if command == '$db-list':
                        cursor = cnx.cursor()
                        databases = "show databases"
                        cursor.execute(databases)
                        print("Your mysql databases...")
                        for (databases) in cursor:
                            var = databases[0]
                            print(" #--> " + var)
                    elif command == '$enter-db':
                        databaseName = input("MYSQL: Enter your mysql database name: ")
                        cursor = cnx.cursor()
                        databases = "show databases"
                        cursor.execute(databases)
                        if databaseName.__contains__(databases):
                            print("MYSQL: Selected database: " + databaseName)
                            print("Commands for " + databaseName)
                            print("   -> $list-table")
                            print("   -> $insert")
                            print("   -> $delete")
                            print("")
                            enterDB_MYSQLDBCommand = input("MYSQL / " + databaseName + " | Command Panel: ")
                            if enterDB_MYSQLDBCommand == '$list-table':
                                cursor = cnx.cursor()
                                databases = "show tables;"
                                cursor.execute(databases)
                                result = cursor.fetchall()
                                for x in result:
                                    print(" |----> " + x)
                        else:
                            print("MYSQL: Unknow database name.")

                else:
                    print("Connection declined.")
                    cnx.close()
            if lastQ == "N" or "n":
                print("MYSQL: Transaction cancelled.")
                sys.exit()
