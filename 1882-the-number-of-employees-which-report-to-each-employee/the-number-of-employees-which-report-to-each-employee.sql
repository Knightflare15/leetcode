# Write your MySQL query statement below
select e.reports_to as employee_id, (select name from employees where employee_id = e.reports_to) as name, count(*) as reports_count,round(avg(age)) as average_age
from employees e
where e.reports_to is not null
group by e.reports_to
having count(*)>=1
order by employee_id