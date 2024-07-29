now = Practice.datetime.now()
print("Current date and time:")
print(now)
print(" ")
print("specific format:")
# Print the current date and time in a specific format
print(now.strftime("%m/%y/%d %H:%M:%S"))
print(now.strftime("%m-%y-%d %H:%M:%S"))

#Output:
'''Current date and time:
2024 - 07 - 27
19: 22:04.869297

specific format:
07 / 24 / 27
19: 22:04
07 - 24 - 27
19: 22:04'''