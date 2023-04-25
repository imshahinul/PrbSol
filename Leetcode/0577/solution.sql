# Write your MySQL query statement below
select e.name,b.bonus from Employee e
left join Bonus b
on b.empId = e.empId
where COALESCE(b.bonus,0) < 1000