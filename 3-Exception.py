# handling Exception
try:
    file = open('app.py')
    age = int(input('Age: '))
except (ValueError, ZeroDivisionError):
    print("Please enter valid age")
else:
    print("Please enter valid age")
finally:
    file.close()
