import sqlite3

def raw_domoticz_put(data, db_file='/opt/domoticz/domoticz.db'):
    try:
        conn = sqlite3.connect(db_file)
    except Exception as e:
        return False
    try:
        c = conn.cursor()
        for idx,value,date in data:
            idx = int(idx)
            value = float(value)
            date = "{}-{}-{} {}:{}:{}".format(
                date.year,date.month,date.day,
                date.hour,date.minute,date.second
            )
            sql_base = "INSERT INTO Percentage (DeviceRowID, Percentage, Date) VALUES ({}, {}, '{}');"
            sql = sql_base.format(idx,value,date)
            c.execute(sql)
        conn.commit()
    except Exception as e:
        return False
    try:
        conn.close()
    except Exception as e:
        return False
    return True
