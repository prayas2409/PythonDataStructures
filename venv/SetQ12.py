try:
    s = {1, 2, 3, 4, 5, 5, 6, 7, -1, -3}
    print(s)
    print(min(s))
    print(max(s))

except Exception as e:
    print("process stopped because ", e)
