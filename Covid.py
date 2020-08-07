from covid import Covid
covid = Covid()


print("Total Case are ")
print(covid.get_total_confirmed_cases())
print("total Active Cases are")
print(covid.get_total_active_cases())
print("Total Recovered cases are ")
print(covid.get_total_recovered())