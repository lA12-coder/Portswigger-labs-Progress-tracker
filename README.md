# PortSwigger Web Security Academy - Solved Labs

![Total Labs](https://img.shields.io/badge/Total%20Labs%20Solved-0-blue) ![Last Updated](https://img.shields.io/badge/Last%20Updated-2026--00--00-yellow) ![Level](https://img.shields.io/badge/Level-NEWBIE-green) ![Vulnerability labs](https://img.shields.io/badge/Completed-0%25-purple)

This file tracks my progress through [PortSwigger Web Security Academy](https://portswigger.net/web-security) labs. I focus on web app pentesting, documenting key labs as full writeups (linked below) and logging all solves here for reference. Full writeups are reserved for first-time techniques, complex exploits, or custom tools.

## Level progress
- **Apprentice**: 8 of 61
- **Practitioner**: 18 of 174
- **Expert**: 0 of 39

## Categories Covered

- **SQL injection**: 10/18 lab
- **Authentication**: 4/13 lab
- **Path Traversal**: 6/6 lab
- **Access Control**: 6/13

## Notes
- **Full Writeups**: Only for significant labs (e.g., chained exploits or scripted solutions). See `platforms/portswigger/` for details.
- **Tools Used**: Burp Suite

## How to Read
- **Columns**: 
  - `No`: Sequential lab number.
  - `Date`: When I solved it (YYYY-MM-DD).
  - `Topic`: Vulnerability category (e.g., API Testing, XSS).
  - `Lab Title`: Exact name from PortSwigger.
  - `Difficulty`: Apprentice, Practitioner, or Expert.
  - `Writeup Link`: Links to full writeup (if exists) or "N/A" for quick solves.

---

## Solved Labs

| No | Date       | Topic          | Lab Title                                   | Difficulty  | Writeup Link |
|----|------------|----------------|---------------------------------------------|-------------|--------------|
| 1  | 2026-06-17 | SQL-Injection    |  SQL injection vulnerability in WHERE clause allowing retrieval of hidden data| Apprentice | N/A |
| 2  | 2026-06-17 |    SQL Injection | SQL injection vulnerability allowing login bypass  | Apprentice | N/A |
| 3  | 2026-06-19 | SQL injection attack  | querying the database type and version on MySQL and Microsoft | Practitioner | N/A |
| 4  | 2026-06-19 | SQL Injection  | Querying-database-version-oracle |Practitioner  | N/A |
| 5  | 2026-06-19| SQL injection attack    | listing the database contents on non-Oracle databases |Practitioner  | N/A |
| 6  | 2026-06-19| SQL injection attack    | listing the database contents on Oracle |Practitioner  | N/A |
| 7  | 2026-06-19| SQL injection attack    | SQL injection UNION attack, determining the number of columns returned by the query |Practitioner  | N/A |
| 8  | 2026-06-19| SQL injection attack    | SQL injection UNION attack, finding a column containing text |Practitioner  | N/A |
| 9  | 2026-06-19| SQL injection attack    | SQL injection UNION attack, retrieving data from other tables |Practitioner  | N/A |
| 10  | 2026-06-19| SQL injection attack    | SQL injection UNION attack, retrieving multiple values in a single column |Practitioner  | N/A |
| 11  |2026-06-27 |  Authentication  |Username enumeration via different responses |APPRENTICE | N/A  |
| 12  |2026-06-27 |  Authentication  |Username enumeration via subtly different responses |Practitioner |N/A  |
| 13  |2026-06-28 |  Authentication  |Username enumeration via response timing |Practitioner |N/A  |
| 14  |2026-06-27 |  Authentication  |Broken brute-force protection, IP block |Practitioner |N/A  |
| 15  |2026-07-01 |  Path Traversal  |File Path traversal simple case |Apprentice | N/A |
| 16  |2026-07-03 |  Path Traversal  |Traversal Sequence blocked with absolute path bypass |Practitioner |N/A  |
| 17  |2026-07-03 |  Path Traversal  |Traversal Sequence stripped non-recursively |Practitioner |N/A  |
| 18  |2026-07-03 |  Path Traversal  |Traversal Sequence stripped with superfluous URL-decode |Practitioner |N/A  |
| 19  |2026-07-03 |  Path Traversal  |File path traversal, validation of start of path |Practitioner |N/A  |
| 20  |2026-07-03 |  Path Traversal  |Validation of file extension with null byte bypass |Practitioner|N/A  |
| 21  |2026-07-11 | Access Control   | Unprotected admin functionality |Apprentice |N/A  |
| 22  |2026-07-11 |Access Control    |Unprotected admin functionality with unpredictable URL |Apprentice |N/A  |
| 23  |2026-07-11 |Access Control    |User role controlled by request |Apprentice |N/A  |
| 24  |2026-07-11 |Access Control    |User role can be modified in the user profile |Apprentice |N/A |
| 25  |2026-07-11 |Access Control    |URL Based access control can be circumvented  |Practitioner |N/A  |
| 26  |2026-07-11 |Access Control    |Method Based access control can be circumvented  |Practitioner |N/A  |
| 27  |2026-07-19 | File Upload   |Remote web execution via web shell upload |Apprentice |N/A  |
| 28  |2026-07-19 | File Upload   |Web Shell upload via content-type bypass restriction bypass |Apprentice |N/A  |
| 29  |2026-07-22 | Race Conditions|Limit overrun race conditions |Apprentince |N/A |
| 30  |2026-07-25 | Race Conditions|Multi-endpoint race conditions |Practioner |N/A  |
| 31  | |    | | |  |
| 32  | |    | | |  |







