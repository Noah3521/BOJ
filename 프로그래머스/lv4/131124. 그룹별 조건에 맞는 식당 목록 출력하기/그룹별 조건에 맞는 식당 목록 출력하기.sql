-- 코드를 입력하세요 
-- select a.* from rest_review a
-- join (select * from (SELECT MEMBER_ID,sum(review_score) as score
-- from REST_REVIEW 
-- group by (member_ID)
-- order by score desc)
-- where rownum < 2) b
-- on a.MEMBER_ID = b.MEMBER_ID;

select memb.member_name, review.review_text, to_char(review.review_date, 'yyyy-mm-dd') as review_date
from (select a.* from rest_review a
join (select * from (SELECT MEMBER_ID,sum(review_score) as score
from REST_REVIEW 
group by (member_ID)
order by score desc)
where rownum < 2) b
on a.MEMBER_ID = b.MEMBER_ID) review
join member_profile memb
on review.member_id = memb.member_id
order by review.review_date,review.review_text;