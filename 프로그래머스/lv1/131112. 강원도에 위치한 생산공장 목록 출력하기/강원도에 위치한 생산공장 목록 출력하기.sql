-- 코드를 입력하세요
SELECT FACTORY_ID, FACTORY_NAME, ADDRESS from FOOD_FACTORY 
where ADdRESS like '강원도%'
order by FACTORY_ID