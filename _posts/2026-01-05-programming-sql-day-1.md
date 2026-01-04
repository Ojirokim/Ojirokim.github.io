---
title: "Programming SQL Practice – Day 1 (15 Problems)"
date: 2026-01-05
categories: [코드-기술력-자료]
tags: [sql, programmers, daily-practice]
---

## 📅 Today’s Goal
- Solve 15 SQL problems of SQL questions
- Focus on correctness and query structure

---

## Problem 51 — 없어진 기록 찾기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/59042 
**Difficulty:** Level 4

```sql
SELECT ANIMAL_ID, NAME
FROM ANIMAL_OUTS
WHERE ANIMAL_ID NOT IN (
  SELECT ANIMAL_ID
  FROM ANIMAL_INS
)
ORDER BY ANIMAL_ID;
```
**Key Point**
- SubQuery can be used to create a list,
- I can compare that list to the Outerquery.


## Problem 52 — 과일로 만든 아이스크림 고르기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/133025 
**Difficulty:** Level 4

```sql
SELECT FH.FLAVOR
FROM FIRST_HALF FH
LEFT JOIN ICECREAM_INFO II
ON FH.FLAVOR = II.FLAVOR
WHERE TOTAL_ORDER >3000
AND INGREDIENT_TYPE = 'fruit_based'
ORDER BY TOTAL_ORDER DESC
```

**Key Point**
- Left join table in order to preserve FIRST_HALF table content
- Then give condition on the WHERE line.


## Problem 53 — 재구매가 일어난 상품과 회원 리스트 구하기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/131536
**Difficulty:** Level 4

```sql
SELECT DISTINCT USER_ID, PRODUCT_ID
FROM 
(
SELECT USER_ID, PRODUCT_ID, COUNT(*)OVER(PARTITION BY USER_ID, PRODUCT_ID) COUNT_MULT
FROM ONLINE_SALE
ORDER BY USER_ID, PRODUCT_ID
) BB
WHERE COUNT_MULT >1
ORDER BY USER_ID, PRODUCT_ID DESC
```

**Key Point**
- With a SubQuery create a temporary table that you can reference the multiple counts.
- Then give condition on the WHERE line.
- Type distinct on the Select line, so that you can see distinct IDs


## Problem 54 — 최댓값 구하기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/59415
**Difficulty:** Level 4

```sql
SELECT DATETIME `시간`
FROM ANIMAL_INS
WHERE DATETIME = (SELECT MAX(DATETIME) FROM ANIMAL_INS)
```

**Key Point**
- Subquery can exist on WHERE line so that I can reference the DATETIME
- Rename the column as `시간`


## Problem 55 — 조건에 맞는 사용자 정보 조회하기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/164670
**Difficulty:** Level 4

```sql
SELECT DISTINCT USER_ID, NICKNAME, CONCAT(CITY,' ', STREET_ADDRESS1,' ', STREET_ADDRESS2) `전체주소`, CONCAT(
  SUBSTRING(TLNO, 1, 3), '-', 
  SUBSTRING(TLNO, 4, 4), '-', 
  SUBSTRING(TLNO, 8, 4)) `전화번호`
FROM
(
SELECT *, COUNT(*)OVER(PARTITION BY WRITER_ID) CNT
FROM USED_GOODS_BOARD GB
LEFT JOIN USED_GOODS_USER GU
ON GB.WRITER_ID=GU.USER_ID
) BB
WHERE CNT>2
ORDER BY USER_ID DESC
```

**Key Point**
- `FORMAT()` in MySQL is for numeric formatting, not string masks
- Phone numbers should be handled as strings
- Use `SUBSTRING()` plus `CONCAT` for formatting


## Problem 56 — 특정 옵션이 포함된 자동차 리스트 구하기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/157343
**Difficulty:** Level 4

```sql
SELECT *
FROM CAR_RENTAL_COMPANY_CAR
WHERE OPTIONS LIKE '%네비게이션%'
ORDER BY CAR_ID DESC
```

**Key Point**
- Easily done with LIKE to see if the string is inside.


## Problem 57 — 조건에 부합하는 중고거래 상태 조회하기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/164672
**Difficulty:** Level 4

```sql
SELECT BOARD_ID, WRITER_ID, TITLE,
PRICE, CASE WHEN STATUS='DONE' THEN '거래완료'
WHEN STATUS='SALE' THEN '판매중' 
ELSE '예약중' END STATUS
FROM USED_GOODS_BOARD
WHERE CREATED_DATE='2022-10-05'
ORDER BY BOARD_ID DESC
```

**Key Point**
- Specify the Date in the WHERE Line
- Use CASE WHEN in order to divide STATUS column into 3 parts.
- Always don't forget to use END after finishing CASE WHEN phrase


## Problem 58 — 취소되지 않은 진료 예약 조회하기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/132204
**Difficulty:** Level 4

```sql
SELECT APNT_NO, PT_NAME, A.PT_NO, A.MCDP_CD, DR_NAME, APNT_YMD
FROM APPOINTMENT A
LEFT JOIN PATIENT P
ON A.PT_NO = P.PT_NO
LEFT JOIN DOCTOR D
ON A.MDDR_ID = D.DR_ID
WHERE APNT_YMD LIKE '2022-04-13%'
AND APNT_CNCL_YN = 'N'
ORDER BY  APNT_YMD
```

**Key Point**
- Left Join both PATIENT Table and DOCTOR Table in order to preserve data from APPOINTMENT Table
- Give condition in WHERE line and Order them by APNT_YMD as the question requests.


## Problem 59 — 자동차 대여 기록에서 대여중 / 대여 가능 여부 구분하기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/157340
**Difficulty:** Level 4

```sql
SELECT CAR_ID,
 CASE
    WHEN MAX(AVAILABILITY = '대여중') = 1 THEN '대여중'
    ELSE '대여 가능'
  END AS AVAILABILITY
FROM (
SELECT  CAR_ID,
CASE WHEN  START_DATE <= '2022-10-16' AND END_DATE >= '2022-10-16' THEN  '대여중'
ELSE '대여 가능' END AVAILABILITY
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
) BB
GROUP BY CAR_ID
ORDER BY CAR_ID DESC
```

**Key Point**
- This was the hardest question so far.
- Wrapping a query preserves original thinking
- `MAX(condition)` is a useful to divide the situation where you have multiple Key values.
- Needs to GROUP in order to combine them with MAX function.


## Problem 60 — 년, 월, 성별 별 상품 구매 회원 수 구하기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/131532
**Difficulty:** Level 4

```sql
SELECT SUBSTR(SALES_DATE,1,4) YEAR ,SUBSTR(SALES_DATE,6,2)*1 MONTH, GENDER, COUNT(distinct UI.USER_ID) USERS
FROM USER_INFO UI
JOIN ONLINE_SALE OS
ON OS.USER_ID = UI.USER_ID
WHERE GENDER IS NOT NULL
GROUP BY YEAR,MONTH, GENDER
ORDER BY  YEAR,MONTH, GENDER
```

**Key Point**
- `COUNT(*)` counts rows, not users
- User-based statistics require `COUNT(DISTINCT USER_ID)`
- Always check whether the problem wants “events” or “people”


## Problem 61 — 서울에 위치한 식당 목록 출력하기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/131118
**Difficulty:** Level 4

```sql
SELECT RI.REST_ID, REST_NAME, FOOD_TYPE, FAVORITES, ADDRESS, SCORE
FROM REST_INFO RI
JOIN (
SELECT REST_ID, ROUND(AVG(REVIEW_SCORE),2) SCORE
FROM REST_REVIEW
GROUP BY REST_ID
) BB
ON RI.REST_ID= BB.REST_ID
WHERE ADDRESS LIKE '서울%'
ORDER BY SCORE DESC, FAVORITES DESC
```

**Key Point**
- `LIKE '%서울%'` and `LIKE '서울%'` have very different meanings
- Small pattern differences can cause wrong answers


## Problem  62— 자동차 대여 기록에서 장기/단기 대여 구분하기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/151138
**Difficulty:** Level 4

```sql
SELECT HISTORY_ID, CAR_ID, DATE_FORMAT(START_DATE,'%Y-%m-%d') START_DATE, DATE_FORMAT(END_DATE,'%Y-%m-%d') END_DATE, CASE WHEN DATEDIFF(END_DATE,START_DATE)+1>=30 THEN '장기 대여'
ELSE '단기 대여' END RENT_TYPE
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE DATE_FORMAT(START_DATE,'%Y-%m-%d') BETWEEN '2022-09-01' and '2022-09-30'
ORDER BY HISTORY_ID DESC
```

**Key Point**
- `DATE_FORMAT()` is for display, not calculation
- `DATEDIFF()` is the safest way to compare durations
- `DATEDIFF()` excludes the start date
- Add `+ 1` when calculating inclusive durations


## Problem 63 — 자동차 평균 대여 기간 구하기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/157342
**Difficulty:** Level 4

```sql
SELECT CAR_ID, AVERAGE_DURATION
FROM (
SELECT CAR_ID,ROUND(AVG(DATEDIFF(END_DATE, START_DATE))+1,1) AVERAGE_DURATION
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
GROUP BY CAR_ID
) BB
WHERE AVERAGE_DURATION>=7
ORDER BY AVERAGE_DURATION DESC, CAR_ID DESC;
```

**Key Point**
- `DATEDIFF()` excludes the start date
- Add `+ 1` when calculating inclusive durations

## Problem 64 — 헤비 유저가 소유한 장소
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/77487
**Difficulty:** Level 4

```sql
SELECT ID, NAME,HOST_ID
FROM (
SELECT ID, NAME, HOST_ID, COUNT(HOST_ID)OVER(PARTITION BY HOST_ID) COUNT
FROM PLACES
) BB
WHERE COUNT >=2
ORDER BY ID
```

**Key Point**
- In order to preserve the lines I used Window Function
- Instead of Group by, which folds the groups.

## Problem 65 — 우유와 요거트가 담긴 장바구니
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/62284
**Difficulty:** Level 4

```sql
SELECT DISTINCT CART_ID
FROM CART_PRODUCTS
WHERE CART_ID IN
(SELECT CART_ID FROM CART_PRODUCTS
WHERE NAME ='Milk')
AND CART_ID IN
(SELECT CART_ID FROM CART_PRODUCTS
WHERE NAME ='Yogurt')
ORDER BY CART_ID
```

**Key Point**
- Use IN() to make a list where I can reference the CART_ID
- DISTINCT TO MAKE CART_ID DISTINCT in the result
