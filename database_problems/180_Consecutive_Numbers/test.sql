/* 
Table: Logs

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| num         | varchar |
+-------------+---------+
In SQL, id is the primary key for this table.
id is an autoincrement column starting from 1.
 

Find all numbers that appear at least three times consecutively.

Return the result table in any order.

The result format is in the following example.

 

Example 1:

Input: 
Logs table:
+----+-----+
| id | num |
+----+-----+
| 1  | 1   |
| 2  | 1   |
| 3  | 1   |
| 4  | 2   |
| 5  | 1   |
| 6  | 2   |
| 7  | 2   |
+----+-----+
Output: 
+-----------------+
| ConsecutiveNums |
+-----------------+
| 1               |
+-----------------+
Explanation: 1 is the only number that appears consecutively for at least three times.
*/
-- Final SQL command --
select distinct l1.num as ConsecutiveNums
from logs l1,
logs l2,
logs l3
where l1.id=l2.id-1
and l1.id=l3.id-2
and l1.num=l2.num
and l2.num=l3.num


-- Another solution --
select distinct l1.num as ConsecutiveNums 
from Logs l1
where l1.num in (select l2.num from Logs l2 
where l2.num = l1.num and (l2.id = l1.id -1 or l2.id = l1.id or l2.id = l1.id + 1)
group by num
having count(*) >= 3)