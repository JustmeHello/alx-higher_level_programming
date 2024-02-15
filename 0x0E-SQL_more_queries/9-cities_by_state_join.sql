-- script that lists all cities contained in the database hbtn_0d_usa.
SELECT id, name FROM cities WHERE state_id = (SELECTid FROM states WHERE name = 'California') ORDER BY id ASC;
