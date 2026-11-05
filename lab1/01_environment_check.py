import sys
import platform

print("Python version:", sys.version.split()[0])
print("Operating system:", platform.system())
print("Machine:", platform.machine())

try:
    import numpy
    print("NumPy:", numpy.__version__)
except ImportError:
    print("NumPy is not installed")

try:
    import pandas
    print("Pandas:", pandas.__version__)
except ImportError:
    print("Pandas is not installed")
