import sqlite3

def update_domoticz(statues, data, db_file='/opt/domoticz/domoticz.db'):
    try:
        conn = sqlite3.connect(db_file)
    except Exception as e:
        return False
    try:
        c = conn.cursor()
        for idx,value,date in data:
            idx = int(idx)
            value = float(value)
            date = "{:04}-{:02}-{:02} {:02}:{:02}:{:02}".format(
                date.year,date.month,date.day,
                date.hour,date.minute,date.second
            )
            sql_base = "INSERT INTO Percentage (DeviceRowID, Percentage, Date) VALUES ({}, {}, '{}');"
            sql = sql_base.format(idx,value,date)
            c.execute(sql)

        for idx,value,date in statues:
            idx = int(idx)
            value = float(value)
            date = "{:04}-{:02}-{:02} {:02}:{:02}:{:02}".format(
                date.year,date.month,date.day,
                date.hour,date.minute,date.second
            )
            sql_base = "UPDATE DeviceStatus SET sValue={}, LastUpdate='{}' WHERE id = {};"
            sql = sql_base.format(value,date,idx)
            c.execute(sql)
        conn.commit()
    except Exception as e:
        return False
    try:
        conn.close()
    except Exception as e:
        return False
    return True
