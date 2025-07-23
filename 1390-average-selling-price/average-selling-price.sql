# Write your MySQL query statement below
select e.product_id,iFNULL(ROUND(SUM(e.price*p.units)/SUM(p.units),2),0) as average_price
from Prices e left outer join unitsSold p on e.product_id=p.product_id AND p.purchase_date BETWEEN e.start_date AND e.end_date
group by product_id