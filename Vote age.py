# -*- coding: utf-8 -*-
month=int(input("Enter your month of birth : "))
year=int(input("Enter your year of birth : "))
age=2020-year
mon=9-month
vote="You are eligible for voting! Just use your power!" if age>=18 else "you are just ",age,"years And",mon,"months Old!.\n S0 you're not eligible for voting.\n S0, just calm down and wait until 18 to vote."
print(vote)
    