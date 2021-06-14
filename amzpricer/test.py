import os

pw1 = os.getenv('GAPPPW')
print(pw1)

pw2 = os.environ.get('GAPPPW')
print(pw2)

pw3 = os.environ['GAPPPW']
print(pw3)

