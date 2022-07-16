import sqlite3


def get_db_connection():
    conn = sqlite3.connect('db/sgcallverify.db')
    conn.row_factory = sqlite3.Row
    return conn


def get_call_records(id):
    conn = get_db_connection()
    conn_query = f"SELECT * FROM call_record cr INNER JOIN caller c ON cr.caller_email = c.caller_email WHERE callee_id = '{id}' ORDER BY call_datetime DESC;"
    res = [dict(row) for row in conn.execute(conn_query).fetchall()]
    conn.close()
    return res


def login_caller(email):
    conn = get_db_connection()
    conn_query = f"SELECT * FROM caller WHERE caller_email = '{email}'"
    res = conn.execute(conn_query).fetchone()
    conn.close()
    return res != None


def has_ongoing_call(email):
    conn = get_db_connection()
    conn_query = f"SELECT * FROM call_record WHERE caller_email = '{email}' AND call_status='Ongoing';"
    res = conn.execute(conn_query).fetchone()
    conn.close()
    return res != None


def get_ongoing_call_details(email):
    conn = get_db_connection()
    conn_query = f"SELECT * FROM call_record WHERE caller_email = '{email}' AND call_status='Ongoing';"
    res = conn.execute(conn_query).fetchone()
    conn.close()
    return res


def mark_call_as_ongoing(email, nric):
    conn = get_db_connection()
    conn.execute(f"INSERT INTO call_record (caller_email, callee_id, call_status) VALUES (?, ?, ?);",
                 (email, nric, 'Ongoing'))
    conn.commit()
    conn.close()


def mark_call_as_ended(email):
    conn = get_db_connection()
    conn.execute(
        f"UPDATE call_record SET call_status = 'Ended' WHERE caller_email = '{email}' and call_status = 'Ongoing'")
    conn.commit()
    conn.close()
