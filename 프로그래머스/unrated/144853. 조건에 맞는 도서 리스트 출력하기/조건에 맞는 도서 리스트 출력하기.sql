-- 코드를 입력하세요
select BOOK_ID	, date_format(PUBLISHED_DATE, '%Y-%m-%d') from book where year(published_date)=2021 and category = '인문' order by date_format(PUBLISHED_DATE, '%Y-%m-%d') asc