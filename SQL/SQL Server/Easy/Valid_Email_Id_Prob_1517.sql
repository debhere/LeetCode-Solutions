select * from Users
where mail like '[a-zA-Z]%@leetcode.com'
and mail not like '%[#$%!~@^+></?{}()|=*&]%@leetcode.com'