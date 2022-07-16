DROP TABLE IF EXISTS caller;

CREATE TABLE caller (
    caller_email VARCHAR(255) NOT NULL,
    caller_name VARCHAR(255) NOT NULL,
    caller_num VARCHAR(255) NOT NULL,
    caller_ministry VARCHAR(255) NOT NULL,
    PRIMARY KEY(caller_email)
);

DROP TABLE IF EXISTS call_record;

CREATE TABLE call_record (
    caller_email VARCHAR(255) NOT NULL,
    callee_id VARCHAR(9) NOT NULL,
    call_status VARCHAR(20) NOT NULL,
    call_datetime TIMESETAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (caller_email, callee_id, call_datetime)
);