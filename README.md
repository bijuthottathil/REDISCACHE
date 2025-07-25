# Implementation of Redis Cache to show  the performance improvement while accessing Postgres Data

<img width="624" height="768" alt="image" src="https://github.com/user-attachments/assets/0808bdb5-4c52-464a-9785-e28565d1a811" />


1. Using below table from Postgress for demo  
2. <img width="1609" height="990" alt="image" src="https://github.com/user-attachments/assets/c6891557-61ab-4036-8629-928ad4f1703c" />
3. Initiated redis server in docker  using
4. (venv) PS D:\Projects\DBT-Fusion\venv> docker run -d --name redis -p 6379:6379 redis
5.  Redis is running in Docker
6. <img width="1880" height="574" alt="image" src="https://github.com/user-attachments/assets/3ea5a067-9e3c-4dbe-b3ba-4a92482b8990" />

8. Below one is the Redis Cache key defined
9. query = "SELECT * FROM customers ;"
data = get_data(query, cache_key="employees_IT")
print(data)

10. I am running for the first time  "(venv) PS D:\Projects\DBT-Fusion\venv> python rediscache.py"
11. All data from Customer table loaded and showed <img width="1112" height="472" alt="image" src="https://github.com/user-attachments/assets/4c4eefdd-0cc3-402b-a008-a3ef2df8a204" />

12. Now we will see whether data is loaded in redis or not
13. I connected to Redis Server terminal and showing key value
14. <img width="1112" height="472" alt="image" src="https://github.com/user-attachments/assets/662ee490-3f21-45d9-8041-a0813ded4914" />
15. Clearly you can see data is cached in redis
16. Next time I executed same file, this time content is loaded from Redis Cache
17. <img width="1099" height="435" alt="image" src="https://github.com/user-attachments/assets/b39b1ec6-fcad-42f9-aacc-6462ec5b5856" />

18. <img width="797" height="161" alt="image" src="https://github.com/user-attachments/assets/a91802d7-03f0-46d8-8603-ef6da8aa811e" />

19. As soon I updated value of customer, cache became null
20. <img width="429" height="62" alt="image" src="https://github.com/user-attachments/assets/8705fe80-b348-496a-9f73-450b019b45f0" />
21. Next time I ran file again, in actual terminal, we can see modified data
22.  <img width="1094" height="100" alt="image" src="https://github.com/user-attachments/assets/0e18afae-3e60-49cf-92d0-e05b3bc85ba7" />
23.  Now see what is coming in cache key
24.  <img width="1131" height="177" alt="image" src="https://github.com/user-attachments/assets/34f62b13-cd08-474d-bb66-35b69ef1a9ca" />
25.  In cache also data reloaded after updates









