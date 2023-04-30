# Write your MySQL query statement below
SELECT ROUND(SUM(tiv_2016),2) AS tiv_2016 FROM Insurance a
WHERE EXISTS (SELECT * FROM Insurance WHERE pid <> a.pid AND tiv_2015 = a.tiv_2015)
AND NOT EXISTS (SELECT * FROM Insurance WHERE pid <> a.pid AND (lat,lon) = (a.lat,a.lon));