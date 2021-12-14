#!/usr/bin/env python3

## create a dictionary
switch = {"hostname": "sw1", "ip": "10.0.1.1", "version": "1.2", "vendor": "cisco"}
print(switch["hostname"])
print(switch["ip"])
#print(switch["lynx"])

print("first test - .get()")
print(switch.get("lynx"))

print("Second test - .get()")
print(switch.get("lynx", "the key is in another catle"))

print( "Third test - .get()" )
print( switch.get("version") )

print( "Fourth test - .keys()" )
print( switch.keys() )

print( "Fifth test - .values()" )
print( switch.values() )

print( "sixth test - .pop()")
print( switch.pop("hostname"))

print("seventh test - add new value")
switch["admin login"] = "kar01"
print(switch.keys())
print(switch.values())


print("eighth test - add new value")
switch["password"] = "qwer"
print(switch.keys())
print(switch.values())


