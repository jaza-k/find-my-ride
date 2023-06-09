import dsn 
import psycopg2
import dbfuncs 



def test_checking_matches():
    conn = psycopg2.connect(dsn.DSN)
    
    dbfuncs.check_matches_against_user_searches(conn)
    
    curs = conn.cursor()
    
    check_q = "SELECT * FROM matches_with;"
    curs.execute(check_q)
    res = curs.fetchall()
    
    print("got back: ", res)
    
    
    conn.commit()
    conn.close()


if __name__ == "__main__":
    test_checking_matches()