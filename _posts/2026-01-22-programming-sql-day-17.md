---
title: "Programming SQL Practice – Day 17 (5 Problems)"
date: 2026-01-22
categories: [코드-기술력-자료]
tags: [sql, programmers, daily-practice]
---

## 📅 Today’s Goal
- Solve 5 SQL problems of SQL questions
- Focus on correctness and query structure
A
---

## Problem 171 — The Report
🔗 https://www.hackerrank.com/challenges/the-report/problem?isFullScreen=true
**Difficulty:** Level 6

```sql
SELECT
  CASE WHEN g.grade >= 8 THEN s.name ELSE NULL END AS name,
  g.grade,
  s.marks
FROM students s
JOIN grades g
  ON s.marks BETWEEN g.min_mark AND g.max_mark
ORDER BY
  g.grade DESC,
  name ASC,
  s.marks ASC; 
```
**Key Point**
- Using between operator for grade range check in Join condition


## Problem 172 — Top Competitors
🔗 https://www.hackerrank.com/challenges/full-score/problem?isFullScreen=true
**Difficulty:** Level 6

```sql
SELECT h.hacker_id, h.name
FROM hackers h
JOIN submissions s ON s.hacker_id = h.hacker_id
JOIN challenges c  ON c.challenge_id = s.challenge_id
JOIN difficulty d  ON d.difficulty_level = c.difficulty_level
WHERE s.score = d.score
GROUP BY h.hacker_id, h.name
HAVING COUNT(DISTINCT s.challenge_id) > 1
ORDER BY COUNT(DISTINCT s.challenge_id) DESC, h.hacker_id ASC;
```
**Key Point**
- Used group by and having clause to filter out the top competitors


## Problem 173 — Ollivander's Inventory
🔗 https://www.hackerrank.com/challenges/harry-potter-and-wands/problem?isFullScreen=true
**Difficulty:** Level 6

```sql
SELECT
  w.id,
  wp.age,
  w.coins_needed,
  w.power
FROM wands w
JOIN wands_property wp
  ON w.code = wp.code
JOIN (
  SELECT
    w2.power,
    wp2.age,
    MIN(w2.coins_needed) AS min_coins
  FROM wands w2
  JOIN wands_property wp2
    ON w2.code = wp2.code
  WHERE wp2.is_evil = 0
  GROUP BY w2.power, wp2.age
) m
  ON m.power = w.power
 AND m.age = wp.age
 AND m.min_coins = w.coins_needed
WHERE wp.is_evil = 0
ORDER BY w.power DESC, wp.age DESC;
```
**Key Point**
- Created a subquery to find the minimum coins needed for each wand
- Then joined the subquery with the main query


## Problem 174 — Challenges
🔗 hackerrank.com/challenges/challenges?isFullScreen=true
**Difficulty:** Level 6

```sql
SELECT hc.hacker_id, hc.name, hc.cnt
FROM (
    SELECT h.hacker_id, h.name, COUNT(c.challenge_id) AS cnt
    FROM hackers h
    JOIN challenges c
      ON c.hacker_id = h.hacker_id
    GROUP BY h.hacker_id, h.name
) hc
JOIN (
    SELECT cnt, COUNT(*) AS freq
    FROM (
        SELECT h.hacker_id, COUNT(c.challenge_id) AS cnt
        FROM hackers h
        JOIN challenges c
          ON c.hacker_id = h.hacker_id
        GROUP BY h.hacker_id
    ) x
    GROUP BY cnt
) f
  ON f.cnt = hc.cnt
WHERE hc.cnt = (
    SELECT MAX(cnt)
    FROM (
        SELECT COUNT(*) AS cnt
        FROM challenges
        GROUP BY hacker_id
    ) m
)
OR f.freq = 1
ORDER BY hc.cnt DESC, hc.hacker_id ASC;
```
**Key Point**
- Counted the number of challenges each hacker has completed
- Then joined the subquery with the main query
- Filtered out the hackers with the maximum number of challenges or those with unique challenge counts


## Problem 175 — Contest Leaderboard
🔗 https://www.hackerrank.com/challenges/contest-leaderboard/problem?isFullScreen=true
**Difficulty:** Level 6

```sql
SELECT ms.hacker_id, h.name, SUM(ms.max_score) AS total_score
FROM (
    SELECT hacker_id, challenge_id, MAX(score) AS max_score
    FROM Submissions
    GROUP BY hacker_id, challenge_id
) AS ms
JOIN Hackers h
  ON h.hacker_id = ms.hacker_id
GROUP BY ms.hacker_id, h.name
HAVING SUM(ms.max_score) > 0
ORDER BY total_score DESC, ms.hacker_id ASC;

```

**Key Point**
- Used a subquery to find the maximum score for each hacker and challenge
- Joined the subquery with the Hackers table to get hacker names
- Grouped by hacker_id and name to aggregate scores
- Filtered out hackers with total score of 0
