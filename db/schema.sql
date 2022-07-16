DROP TABLE IF EXISTS caller;

CREATE TABLE caller (
    caller_name VARCHAR(255) NOT NULL,
    caller_num VARCHAR(255), NOT NULL,
    caller_email VARCHAR(255) NOT NULL,
    caller_ministry VARCHAR(255) NOT NULL,
    PRIMARY KEY(caller_name, caller_num)
)

DROP TABLE IF EXISTS call_record;

CREATE TABLE call_record (
    caller_name VARCHAR(255) NOT NULL,
    caller_num VARCHAR(255) NOT NULL,
    callee_id VARCHAR(9) NOT NULL,
    call_status VARCHAR(20) NOT NULL
    PRIMARY KEY (caller_name, caller_num, callee_id)
)