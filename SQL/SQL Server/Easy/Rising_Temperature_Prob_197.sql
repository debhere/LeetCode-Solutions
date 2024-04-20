select w1.id from weather w1, weather w2
where w1.temperature > w2.temperature
and w1.recorddate = DATEADD(DAY,1,w2.recorddate)