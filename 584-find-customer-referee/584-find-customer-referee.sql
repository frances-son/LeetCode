/* 헤맨 문제. 뭔가 고급스러운 표현이 있나 헀는데 그냥 OR로 IS NULL 인것까지 포함하는 거였다... 참고로 referee_id = NULL로 하면 오답이다. */

SELECT name FROM customer WHERE referee_id IS NULL OR referee_id <> 2;
