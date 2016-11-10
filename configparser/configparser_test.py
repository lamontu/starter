# -*- coding: utf-8 -*-

import configparser

cf = configparser.ConfigParser()
cf.read("configparser_test.conf")

# return all seciton
s = cf.sections()
print("section:", s)

print("*" * 70)
o1 = cf.options("mysql")
print("options:mysql", o1)
o2 = cf.options("personal information")
print("options:personal information", o2)
o3 = cf.options("add")
print("options:add", o3)
o4 = cf.options("del")
print("options:del", o4)

print("*" * 70)
v1 = cf.items("mysql")
print("items:mysql", v1)
v2 = cf.items("personal information")
print("items:personal information", v2)
v3 = cf.items("add")
print("items:add", v3)
v4 = cf.items("del")
print("items:del", v4)

print("*" * 70)
db_host = cf.get("mysql", "db_host")
db_port = cf.getint("mysql", "db_port")
db_user = cf.get("mysql", "db_user")
db_pass = cf.get("mysql", "db_pass")

my_name = cf.get("personal information", "name")
my_age = cf.get("personal information", "age")
my_address = cf.get("personal information", "address")
my_tel = cf.get("personal information", "address")

print("db_host", db_host)
print("db_port", db_port)
print("db_user", db_user)
print("db_pass", db_pass)
print("")
print("my_name", my_name)
print("my_age", my_age)
print("my_address", my_address)
print("my_tel", my_tel)

print("*" * 70)
# add a section
# cf.add_section("addd")
# cf.write(open(configparser_test.conf", "w"))

if cf.has_section("addd"):
    print("[addd] has already existed!")
else:
    print("[addd] does not exist, now write in:")
    cf.add_section("addd")
    cf.set("addd", "addd1", "value of addd1")
    cf.set("addd", "addd2", "value of addd2")
    cf.write(open("configparser_test.conf", "w"))
    print("writing [addd]  in has completed!")

print("")
# delete a section
# cf.remove_section("dele")
# cf.write(open("configparser_test.conf", "w"))

if cf.has_section("dele"):
    print("[dele] exists, start to remove:")
    cf.remove_section("dele")
    cf.write(open("configparser_test.conf", "w"))
    print("removing [dele] has completed!")
else:
    print("[dele] does not exist, don't have to process.")

print("")
# delete a option
# cf.remove_option("del", "del2")
# cf.write(open("configparser_test.py", "w")

if cf.has_option("del", "del2"):
    print("del2 exists, start to remove:")
    cf.remove_option("del", "del2")
    cf.write(open("configparser_test.conf", "w"))
    print("del2 of [del] has been removed!")
else:
    print("[del] does not have del2.")

# change an option
# cf.set("section", "option", "new value")


