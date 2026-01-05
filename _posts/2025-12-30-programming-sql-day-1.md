---
title: "Programming SQL Practice – Day 1 (20 Problems)"
date: 2025-12-30
categories: [코드-기술력-자료]
tags: [sql, programmers, daily-practice]
---

## 📅 Today’s Goal
- Solve 20 SQL problems of SQL questions
- Focus on correctness and query structure

---

## Problem 1 — 이름이 있는 동물의 아이디
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/59407
**Difficulty:** Level 1

```sql
select ANIMAL_ID
from ANIMAL_INS
where NAME is not null
order by ANIMAL_ID
```
**Key Points**
- Records where the animal’s name is missing are represented as NULL, so to find those that have a name, you use IS NOT NULL in the WHERE line.


## Problem 2 — 역순 정렬하기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/59035
**Difficulty:** Level 1

```sql
select NAME, DATETIME
from ANIMAL_INS
order by ANIMAL_ID desc
```
**Key Points**
- Since we need to output NAME and DATETIME, select them in the SELECT line, and sort in descending order based on ANIMAL_ID.


## Problem 3 — 중복 제거하기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/59408
**Difficulty:** Level 1

```sql
select count(distinct NAME)
from ANIMAL_INS
```
**Key Points**
- You can count the number of names without duplicates by using COUNT(DISTINCT column).


## Problem 4 — 동물의 아이디와 이름
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/59403
**Difficulty:** Level 1

```sql
select COUNT(*)
from ANIMAL_INS
order by ANIMAL_ID
```
**Key Points**
- List the animals’ IDs and names in ID order, using the default ascending (ASC) sort.


## Problem 5 — 동물 수 구하기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/59406
**Difficulty:** Level 1

```sql
select COUNT(*)
from ANIMAL_INS
order by ANIMAL_ID
```
**Key Points**
- To find how many animals came in, you can use COUNT, and assuming all records are included, you use COUNT(*).


## Problem 6 — 동명 동물 수 찾기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/59041
**Difficulty:** Level 1

```sql
select NAME, COUNT(name) COUNT
from ANIMAL_INS
where NAME is not NULL
group by Name
having COUNT>=2
order by name
```
**Key Points**
- Use COUNT() with GROUP BY to count records by each name, and give the count an alias (e.g., COUNT as a column name). Then use the WHERE line to exclude NULL values.


## Problem 7 — 아픈 동물 찾기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/59036
**Difficulty:** Level 1

```sql
select ANIMAL_ID , NAME
from ANIMAL_INS
where INTAKE_CONDITION = 'sick'
order by ANIMAL_ID
```
**Key Points**
- Use COUNT() with GROUP BY to count records by each name, and give the count an alias (e.g., COUNT as a column name). Then use the WHERE line to exclude NULL values.


## Problem 8 — 상위 n개 레코드
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/59405
**Difficulty:** Level 1

```sql
select NAME
from ANIMAL_INS
order by DATETIME
limit 1
```
**Key Points**
- Error: I tried using Oracle’s FETCH line, then realized it doesn’t work in MySQL, so I used LIMIT instead.
- Approach: I sorted by DATETIME and used LIMIT to output only one record.


## Problem 9 — 최솟값 구하기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/59038
**Difficulty:** Level 1

```sql
select DATETIME '시간'
from ANIMAL_INS
order by DATETIME
limit 1
```
**Key Points**
- If you modify Problem 8 above by changing the column being selected to DATETIME, you can find the date and time when the earliest entry.


## Problem 10 — 어린 동물 찾기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/59037#fn1
**Difficulty:** Level 1

```sql
select ANIMAL_ID, name
from ANIMAL_INS
where INTAKE_CONDITION != 'aged'
order by ANIMAL_ID
```
**Key Points**
- Issue / Concern: I really don’t like this problem. It says that animals whose intake_condition is not aged are considered “young,” but the actual data includes values like sick and normal. That makes me wonder: couldn’t there be cases where an animal is both sick and aged?
- Approach: Select rows where the intake_condition value is not aged.


## Problem 11 — 여러 기준으로 정렬하기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/59404
**Difficulty:** Level 1

```sql
select animal_id,
NAME,
DATETIME
from animal_ins
order by NAME, datetime desc
```
**Key Points**
- Sort by NAME, and if there are duplicate names, apply a secondary sort using DATETIME.


## Problem 12 — 이름에 el이 들어가는 동물 찾기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/59047
**Difficulty:** Level 1

```sql
select ANIMAL_ID, NAME
from animal_ins
where name like '%el%'
and ANIMAL_TYPE = 'Dog'
order by NAME
```
**Key Points**
- Rather than an actual error, I didn’t realize that the LIKE operator is case-insensitive, so I initially wrote both el and EL. In the end, I kept only el.
- I used the LIKE operator to find names containing el, and added a condition for dog


## Problem 13 — 나이 정보가 없는 회원 수 구하기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/131528
**Difficulty:** Level 1

```sql
select count(USER_ID) USERS
from USER_INFO
where AGE is NULL
```
**Key Points**
- Task was to find cases where AGE is NULL and count them.


## Problem 14 — 가장 비싼 상품 구하기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/131697
**Difficulty:** Level 1

```sql
SELECT max(price) MAX_PRICE
from product
```
**Key Points**
- To find the highest price, you can use the MAX function.


## Problem 15 — NULL 처리하기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/59410
**Difficulty:** Level 1

```sql
SELECT ANIMAL_TYPE,
        IFNULL(NAME,'No name') NAME,
        SEX_UPON_INTAKE
FROM ANIMAL_INS
ORDER BY ANIMAL_ID
```
**Key Points**
- Since NULL values should be displayed as “No name”, you can use IFNULL to replace the NULL values.


## Problem 16 — 경기도에 위치한 식품창고 목록 출력하기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/131114
**Difficulty:** Level 1

```sql
SELECT
    WAREHOUSE_ID,
    WAREHOUSE_NAME,
    ADDRESS,
    ifnull(FREEZER_YN,'N') FREEZER_YN
from FOOD_WAREHOUSE
WHERE WAREHOUSE_NAME LIKE '%경기%'
Order by WAREHOUSE_ID
```
**Key Points**
- As in problem 15, when the value is NULL, use IFNULL to output 'N'


## Problem 17 — 강원도에 위치한 생산공장 목록 출력하기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/131112
**Difficulty:** Level 1

```sql
SELECT FACTORY_ID,
        FACTORY_NAME,
        ADDRESS
FROM FOOD_FACTORY
WHERE ADDRESS LIKE '강원도%'
ORDER BY FACTORY_ID
```
**Key Points**
- Error: I made the mistake of not noticing that the problem specified locations in '강원도', and ended up retrieving all records.
- Approach: Since '강원도' always appears at the beginning of the ADDRESS, I used the LIKE operator with '강원도%'.


## Problem 18 — DATETIME에서 DATE로 형 변환
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/59414
**Difficulty:** Level 1

```sql
SELECT ANIMAL_ID,
        NAME,
        DATE_FORMAT(DATETIME, '%Y-%m-%d') '날짜'   
FROM ANIMAL_INS
```
**Key Points**
- Error: I kept getting errors because I didn’t understand the arguments that come after DATE_FORMAT. Using '%Y-%m-%d' resolved the issue.
- Approach: I used DATE_FORMAT to change the date format.
- Insight: The DATE_FORMAT function returns a STRING, not a DATE/DATETIME type.


## Problem 19 — 흉부외과 또는 일반외과 의사 목록 출력하기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/132203
**Difficulty:** Level 1

```sql
SELECT
        DR_NAME,
        DR_ID,
        MCDP_CD,
        DATE_FORMAT(HIRE_YMD, '%Y-%m-%d') HIRE_YMD 
FROM DOCTOR
WHERE MCDP_CD IN ('CS','GS')
ORDER BY HIRE_YMD DESC, DR_NAME
```
**Key Points**
- Since the department is either CS or GS, you can apply the condition using IN. 
- Sort first by hire date in descending order, and if there is a tie, sort by name in ascending order.


## Problem 20 — 가격이 제일 비싼 식품의 정보 출력하기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/131115
**Difficulty:** Level 1

```sql
SELECT *
FROM FOOD_PRODUCT 
WHERE PRICE= (SELECT MAX(PRICE) FROM FOOD_PRODUCT);
```
**Key Points**
- Because you can’t use aggregate functions directly in the WHERE line, you need to write a subquery 
- or alternatively use HAVING, depending on the case.


