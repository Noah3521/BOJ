-- 코드를 입력하세요

SELECT A.Name, A.DateTime
from Animal_ins a
left outer join Animal_outs b
on a.ANIMAL_ID = b.ANIMAL_ID 
where b.animal_id is NULL
order by a.DateTime
limit 3;
