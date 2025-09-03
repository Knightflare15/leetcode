# Write your MySQL query statement below
select e.reports_to as employee_id, m.name as name, count(*) as reports_count,round(avg(e.age)) as average_age
from employees e JOIN employees m 
    ON e.reports_to = m.employee_id
where e.reports_to is not null
group by e.reports_to,m.name
order by employee_id