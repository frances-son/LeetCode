/* 더 짧은 solution. union all 을 사용하는 것이 훨씬 빠르다.
* 이유
* Strictly speaking, Using UNION is faster when it comes to cases like scan two different column like this.
* (Of course using UNION ALL is much faster than UNION since we don't need to sort the result. But it violates the requirements)
* 참고 링크 : https://leetcode.com/problems/big-countries/discuss/103561/Union-and-OR-and-the-Explanation
*/


SELECT name, population, area
FROM World
WHERE area > 3000000 

UNION

SELECT name, population, area
FROM World
WHERE population > 25000000
