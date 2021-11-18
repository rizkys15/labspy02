#!/usr/bin/python3
a = int(input("masukan bilangan A: "))
b = int(input("masukan bilangan B: "))
c = int(input("masukan bilangan C: "))

if a > b and b > c:
    print("A yang terbesar")
elif b > a and b > c:
    print("B yang terbesar")
else:
    print("B yang terbesar")