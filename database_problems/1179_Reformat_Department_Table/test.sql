/* 
Table: Department

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| revenue     | int     |
| month       | varchar |
+-------------+---------+
In SQL,(id, month) is the primary key of this table.
The table has information about the revenue of each department per month.
The month has values in ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"].
 

Reformat the table such that there is a department id column and a revenue column for each month.

Return the result table in any order.

The result format is in the following example.

 

Example 1:

Input: 
Department table:
+------+---------+-------+
| id   | revenue | month |
+------+---------+-------+
| 1    | 8000    | Jan   |
| 2    | 9000    | Jan   |
| 3    | 10000   | Feb   |
| 1    | 7000    | Feb   |
| 1    | 6000    | Mar   |
+------+---------+-------+
Output: 
+------+-------------+-------------+-------------+-----+-------------+
| id   | Jan_Revenue | Feb_Revenue | Mar_Revenue | ... | Dec_Revenue |
+------+-------------+-------------+-------------+-----+-------------+
| 1    | 8000        | 7000        | 6000        | ... | null        |
| 2    | 9000        | null        | null        | ... | null        |
| 3    | null        | 10000       | null        | ... | null        |
+------+-------------+-------------+-------------+-----+-------------+
Explanation: The revenue from Apr to Dec is null.
Note that the result table has 13 columns (1 for the department id + 12 for the months).
*/
-- Final SQL command --
select distinct id, sum(if(month="Jan", revenue, null)) as Jan_Revenue,
sum(if(month="Feb", revenue, null)) as Feb_Revenue,
sum(if(month="Mar", revenue, null)) as Mar_Revenue,
sum(if(month="Apr", revenue, null)) as Apr_Revenue,
sum(if(month="May", revenue, null)) as May_Revenue,
sum(if(month="Jun", revenue, null)) as Jun_Revenue,
sum(if(month="Jul", revenue, null)) as Jul_Revenue,
sum(if(month="Aug", revenue, null)) as Aug_Revenue,
sum(if(month="Sep", revenue, null)) as Sep_Revenue,
sum(if(month="Oct", revenue, null)) as Oct_Revenue,
sum(if(month="Nov", revenue, null)) as Nov_Revenue,
sum(if(month="Dec", revenue, null)) as Dec_Revenue
from department
group by id;
