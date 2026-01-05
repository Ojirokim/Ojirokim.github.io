---
title: "Programming SQL Practice – Day 3 (15 Problems)"
date: 2026-01-02
categories: [코드-기술력-자료]
tags: [sql, programmers, daily-practice]
---

## 📅 Today’s Goal
- Solve 15 SQL problems of SQL questions
- Focus on correctness and query structure

---

## Problem 36 — 보호소에서 중성화한 동물
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/59045
**Difficulty:** Level 3

```sql
SELECT outs.ANIMAL_ID,
        outs.ANIMAL_TYPE,
        outs.NAME
from animal_outs outs
left join 
animal_ins ins
on outs.animal_id = ins.animal_id
where SEX_UPON_INTAKE like 'Intact%'
and (SEX_UPON_OUTCOME like 'Spayed%' or SEX_UPON_OUTCOME LIKE 'Neutered%')
order by ANIMAL_ID
```
**Key Points**
- At first, I did not group the conditions after `AND`. Since `AND` has higher precedence, the query was evaluated differently than expected, which led to incorrect results.
- After joining the tables, I applied separate conditions for the entry date and the exit date to clearly define the rental period.


## Problem 37 — 조건에 맞는 도서와 저자 리스트 출력하기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/144854
**Difficulty:** Level 3

```sql
SELECT BOOK_ID, AUTHOR_NAME, date_format(PUBLISHED_DATE,'%Y-%m-%d') PUBLISHED_DATE
from book b
left join author a
on b.author_id = a.author_id
where category = '경제'
order by PUBLISHED_DATE
```
**Key Points**
- The date values were formatted using `DATE_FORMAT` to ensure a consistent date format.
- The tables were joined based on the `BOOK` table, and only records belonging to the 경제(Economy) category were selected.


## Problem 38 — 조건별로 분류하여 주문상태 출력하기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/131113
**Difficulty:** Level 3

```sql
SELECT ORDER_ID, PRODUCT_ID, date_format(OUT_DATE,'%Y-%m-%d') OUT_DATE,
case when OUT_DATE <= "2022-05-01" then '출고완료'
        when OUT_DATE > "2022-05-01" then '출고대기'
        else '출고미정' end `출고여부`
from FOOD_ORDER
order by ORDER_ID
```
**Key Points**
- Used a `CASE` statement to classify records as 출고완료, 출고대기, or 출고 미정 based on the date.
- Reminder When writing a `CASE` statement, always remember to close it with `END`.


## Problem 39 — 성분으로 구분한 아이스크림 총 주문량
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/133026
**Difficulty:** Level 3

```sql
SELECT INGREDIENT_TYPE,
        sum(TOTAL_ORDER) TOTAL_ORDER
from First_half f
left join icecream_info i
on f.flavor = i.flavor
group by ingredient_type
order by TOTAL_ORDER
```
**Key Points**
- Initially, I grouped the data by both `FLAVOR` and `INGREDIENT_TYPE`, assuming both were required. However, I realized that the problem only required grouping by `INGREDIENT_TYPE`, so `FLAVOR` was removed from the `GROUP BY` LINE.
- The tables were joined using the `FLAVOR` column, and the total values were calculated by grouping the results based on `INGREDIENT_TYPE`.


## Problem 40 — 루시와 엘라 찾기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/59046
**Difficulty:** Level 3

```sql
SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE
from animal_ins
where NAME in ('Lucy', 'Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty')
```
**Key Points**
- Very simple, Just make a list of Names and search it in WHERE


## Problem 41 — 조건에 맞는 도서 리스트 출력하기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/144853
**Difficulty:** Level 3

```sql
SELECT BOOK_ID, date_format(PUBLISHED_DATE, '%Y-%m-%d') PUBLISHED_DATE
from book
where date_format(PUBLISHED_DATE, '%Y')= '2021'
and CATEGORY = '인문'
order by PUBLISHED_DATE;
```
**Key Points**
- An error occurred because the date values were output without explicitly formatting them.
- Applied both date and category conditions together in the `WHERE` LINE using `AND`, and formatted the date values properly in the `SELECT` statement.


## Problem 42 — 평균 일일 대여 요금 구하기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/144853
**Difficulty:** Level 3

```sql
SELECT round(avg(DAILY_FEE),0) AVERAGE_FEE
from CAR_RENTAL_COMPANY_CAR
where CAR_TYPE ='SUV'
```
**Key Points**
- Filtered the data in the `WHERE` LINE to include only car type SUV, calculated the average value using `AVG`, and then applied `ROUND` to control the number of decimal places.


## Problem 43 — 조건에 맞는 사용자와 총 거래금액 조회하기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/164668
**Difficulty:** Level 3

```sql
SELECT USER_ID,NICKNAME, sum(price) TOTAL_SALES
from USED_GOODS_BOARD BO
left join USED_GOODS_USER US
ON BO.WRITER_ID = US.USER_ID
where STATUS = 'DONE'
Group by WRITER_ID
having TOTAL_SALES >= 700000
order by TOTAL_SALES
```
**Key Points**
- I initially forgot to include the condition for completed sales in the `WHERE` LINE, which produced incorrect results.
- First, joined the two tables. Since the problem asks for completed transactions, I added `WHERE STATUS = 'DONE'`. Then I grouped the results by user. Because the filtering condition applies to the grouped total, I used `HAVING` to apply the condition on `TOTAL_SALES`.


## Problem 44 — 가격대 별 상품 개수 구하기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/131530
**Difficulty:** Level 3

```sql
SELECT CATEG, COUNT(*) PRODUCTS
FROM
(
SELECT CASE WHEN PRICE <10000 THEN 0
        WHEN PRICE >= 10000 AND PRICE < 20000 THEN 10000
        WHEN PRICE >= 20000 AND PRICE < 30000 THEN 20000 
        WHEN PRICE >= 30000 AND PRICE < 40000 THEN 30000
        WHEN PRICE >= 40000 AND PRICE < 50000 THEN 40000
        WHEN PRICE >= 50000 AND PRICE < 60000 THEN 50000
        WHEN PRICE >= 60000 AND PRICE < 70000 THEN 60000
        WHEN PRICE >= 70000 AND PRICE < 80000 THEN 70000
        WHEN PRICE >= 80000 AND PRICE < 90000 THEN 80000
        WHEN PRICE >= 90000 AND PRICE < 100000 THEN 90000
        WHEN PRICE >= 100000 AND PRICE < 110000 THEN 100000
        END CATEG
FROM PRODUCT
) BB
GROUP BY CATEG
ORDER BY CATEG;
```
**Key Points**
- Initially tried to solve the problem by manually defining each price category using multiple `CASE WHEN` conditions.
- After reviewing another solution, I realized that using `TRUNC` allows the problem to be solved much more simply and elegantly.
- By grouping prices with `TRUNC(price, -4)`, price ranges can be categorized automatically, making the query shorter and easier to maintain.
```sql
SELECT
  TRUNC(price, -4) AS price_group,
  COUNT(*) AS products
FROM product
GROUP BY TRUNC(price, -4)
ORDER BY 1 ASC;
```
- This approach is very effective because it allows price categories to be created effortlessly without explicitly defining each range.


## Problem 45 — 3월에 태어난 여성 회원 목록 출력하기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/131120
**Difficulty:** Level 3

```sql
SELECT MEMBER_ID,
        MEMBER_NAME,
        GENDER,
        date_format(DATE_OF_BIRTH,'%Y-%m-%d') DATE_OF_BIRTH
FROM MEMBER_PROFILE
WHERE DATE_FORMAT(DATE_OF_BIRTH,'%m') = '03'
and TLNO is not null
and GENDER='W'
order by MEMBER_ID
```
**Key Points**
- The query returned incorrect results because I forgot to include the condition that filters for female users.
- Extracted the month from the date to create the filtering condition, and added all required filters in the `WHERE` LINE, including `IS NOT NULL` and the condition for female users.


## Problem 46 — 대여 기록이 존재하는 자동차 리스트 구하기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/157341
**Difficulty:** Level 3

```sql
SELECT distinct his.CAR_ID
from CAR_RENTAL_COMPANY_RENTAL_HISTORY HIS
left join CAR_RENTAL_COMPANY_CAR CAR
ON HIS.CAR_ID = CAR.CAR_ID
WHERE CAR_TYPE = '세단'
AND DATE_FORMAT(START_DATE,'%m') = '10'
order by CAR_ID desc
```
**Key Points**
- The results were incorrect because the final sorting was applied in ascending order instead of descending order.
- Since all records from the `HISTORY` table needed to be preserved, a `LEFT JOIN` was used. The sedan condition and the date range condition were then applied in the `WHERE` LINE.


## Problem 47 — 모든 레코드 조회하기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/59034
**Difficulty:** Level 3

```sql
SELECT *
from ANIMAL_INS
```
**Key Points**
- Used `*` to select all records and retrieve the entire dataset.


## Problem 48 — 즐겨찾기가 가장 많은 식당 정보 출력하기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/131123
**Difficulty:** Level 3

```sql
SELECT  FOOD_TYPE, REST_ID, REST_NAME, FAVORITES
FROM
(
SELECT FOOD_TYPE, REST_ID, REST_NAME, FAVORITES, rank()over(partition by FOOD_TYPE order by favorites desc) ranks
from REST_INFO
) BB
WHERE ranks =1
order by  FOOD_TYPE desc
```
**Key Points**
- Using `RANK` as an alias caused an error, so the alias was changed to `RANKS`.
- Ranked each `FOOD_TYPE` using a subquery and selected only the records with a rank of 1.


## Problem 49 — 식품분류별 가장 비싼 식품의 정보 조회하기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/131116
**Difficulty:** Level 3

```sql
Select CATEGORY, price MAX_PRICE, PRODUCT_NAME
from(
SELECT *, rank()over(partition by CATEGORY order by price desc) ranks
from FOOD_PRODUCT
) BB
where ranks =1
and CATEGORY in ('과자', '국', '김치', '식용유')
order by MAX_PRICE desc
```
**Key Points**
- A common mistake I keep making is forgetting to sort in descending order (`DESC`). I need to pay close attention to the required sort direction.
- Created a ranking in a subquery, then used a `WHERE` condition to select the highest-ranked result. Also restricted the results to the required category.


## Problem 50 — 5월 식품들의 총매출 조회하기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/131117
**Difficulty:** Level 3

```sql
SELECT FP.PRODUCT_ID, FP.PRODUCT_NAME, 
    amount*PRICE TOTAL_SALES
FROM FOOD_PRODUCT FP
JOIN
(
select product_id, sum(amount) amount, PRODUCE_DATE, IN_DATE, OUT_DATE
from food_order
WHERE DATE_FORMAT(PRODUCE_DATE,'%Y-%m') = '2022-05'
group by product_id
) BB
ON FP.PRODUCT_ID = BB.PRODUCT_ID
order by TOTAL_SALES desc, 1
```
**Key Points**
- Putting the time filter in the outer query caused incorrect results. The condition needs to be applied in the inner query so the data is filtered before grouping.
- First, grouped the `FOOD_ORDER` table by `PRODUCT_ID` (as a subquery `BB`). Then joined `BB` with the product information table so `AMOUNT` and `PRICE` are available together, making it possible to calculate `TOTAL_SALES`.
