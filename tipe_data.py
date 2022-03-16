# Tipe Data

# tipe data angka satuan (integer)
data_integer = 1500
print("Data", data_integer, "bertipe", type(data_integer))

# tipe data angka desimal (float)
data_float = 15.25
print("Data", data_float, "bertipe", type(data_float))

# tipe data kumpulan karakter (string)
data_string = "Saya"
print("Data", data_string, "bertipe", type(data_string))

# tipe data biner (boolean)
data_bool1 = True
data_bool2 = False
print("Data", data_bool1, "bertipe", type(data_bool1))
print("Data", data_bool2, "bertipe", type(data_bool2))


## Tipe Data Khusus

# bilangan kompleks
data_com = complex(15,35)
print("Data", data_com, "bertipe", type(data_com))


## Tipe Data C
from ctypes import c_double

data_double = c_double (12345.12345)
print("Data", data_double, "bertipe", type(data_double))