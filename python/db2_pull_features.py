import ibm_db

conn = ibm_db.connect(
    "DATABASE=BBGDATA;"
    "HOSTNAME=localhost;"
    "PORT=50000;"
    "PROTOCOL=TCPIP;"
    "UID=db2inst1;"
    "PWD=password;",
    "", ""
)

sql = """
SELECT RETURN, TREND_STRENGTH, VOLATILITY
FROM QUANTUM_FEATURES
ORDER BY TRADE_DATE DESC
FETCH FIRST 1 ROW ONLY
"""

stmt = ibm_db.exec_immediate(conn, sql)
row = ibm_db.fetch_assoc(stmt)

features = {k: float(v) for k, v in row.items()}
print(features)
