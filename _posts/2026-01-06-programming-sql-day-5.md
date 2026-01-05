---
title: "Programming SQL Practice – Day 4 (15 Problems)"
date: 2026-01-06
categories: [코드-기술력-자료]
tags: [sql, programmers, daily-practice]
---

## 📅 Today’s Goal
- Solve 15 SQL problems of SQL questions
- Focus on correctness and query structure
A
---

## Problem 66 — 조회수가 가장 많은 중고거래 게시판의 첨부파일 조회하기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/164671
**Difficulty:** Level 4

```sql
SELECT CONCAT("/home/grep/src/",GB.BOARD_ID,"/",FILE_ID,FILE_NAME,FILE_EXT) FILE_PATH
FROM USED_GOODS_BOARD GB
LEFT JOIN USED_GOODS_FILE GF
ON GB.BOARD_ID = GF.BOARD_ID
WHERE VIEWS = 
(SELECT MAX(VIEWS) FROM USED_GOODS_BOARD)
```
**Key Point**
- Firstly need to join the table, then select the records by selecting them from Where line.
- Then select the appropriate columns to select by using function CONCAT.

