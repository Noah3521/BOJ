-- 코드를 입력하세요
-- SELECT MIN(shipment_id) as shipment_id, flavor, SUM(total_order) as total_order
-- FROM july
-- GROUP BY flavor;

select F.flavor
from FIRST_HALF F
join (SELECT MIN(shipment_id) as shipment_id, flavor, SUM(total_order) as total_order
FROM july
GROUP BY flavor) J
on F.shipment_id = J.shipment_id
order by F.total_order + J.total_order desc, F.total_order + J.total_order FETCH FIRST 3 ROWS ONLY