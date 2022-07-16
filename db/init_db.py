import sqlite3

conn = sqlite3.connect('db/sgcallverify.db')

with open('db/schema.sql') as f:
    conn.executescript(f.read())

conn.execute("""INSERT INTO caller (
    caller_name, caller_num, caller_email, caller_ministry
    ) 
    VALUES 
    ('Bob', '+65 96891917', 'bob@moh.gov.sg', 'Ministry of Health'),
    ('Jerry', '+65 96891917', 'jerry@mom.gov.sg', 'Ministry of Manpower'),
    ('Tom', '+65 96891917', 'tom@moe.gov.sg', 'Ministry of Education'),
    ('James', '+65 96891917', 'james@moh.gov.sg', 'Ministry of Health');""")

conn.execute("""INSERT INTO call_record (
    caller_email, callee_id, call_status, call_datetime
    ) 
    VALUES
    ('bob@moh.gov.sg', 'S****252G', 'Ended', '2022-07-15 13:23:44'), 
    ('jerry@mom.gov.sg', 'S****252G', 'Ended', '2022-07-08 15:05:30'),
    ('james@moh.gov.sg', 'S****252G', 'Ended', '2022-06-18 16:45:23'),
    ('james@moh.gov.sg', 'S****252G', 'Ended', '2022-06-18 16:30:02'),
    ('tom@moe.gov.sg', 'S****252G', 'Ended', '2022-06-15 09:56:42');""")

conn.commit()
conn.close()
