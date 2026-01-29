# list1
# a = [1, 2, 3, 3]
# a.count(2)
#
# list2
# a = [1, 2, 3]
# a = sum(a)
#
# list3
# a = [1, 2, 3]
# b = max(a)
#
# list4
# a = [1, 2, 3]
# b = min(a)
#
# list5
# a = [1, 2, 3]
# print(7 in a)
#
# list6
# royxat = []
# if royxat:
#     print(royxat[0])
# else:
#     print("Ro‘yxat bo‘sh")
#
# list7
# royxat = []
# if royxat:
#     print(royxat[-1])
# else:
#     print("Ro‘yxat bo‘sh")
#
# list8
#
# s = [1,1021, 14, 32, 45]
# a = s[:3]
#
# list9
# s = []
# a = s.reverse()
#
# list10
# s = []
# a = sorted(s)
#
# list11
# s = []
# a = list(set(s))
#
# list12
# s = [1,45, 12, 2]
# s = s.insert(0,1)
#
# list13
# s = [2, 45, 4, 7]
# a = 7
# print(s.index(a))
#
# list14
# s = ["a", "b", "c"]
# print(s == [])
#
# list15
# numbers = [1, 2, 3, 4, 5, 6, 8]
# count = 0
# for n in numbers:
#     if n % 2 == 0:
#         count += 1
# print(count)
#
# list16
# numbers = [1, 2, 3, 4, 5, 6, 8]
# count = 0
# for n in numbers:
#     if n % 2 != 0:
#         count += 1
# print(count)
#
# list17
# s = []
# a = []
# b = a + s
#
# list18
# s = []
# sublist = []
# print(sublist in s)
#
# list19
# a = 4
# s = [12, 45, 4, 10]
# index = s.index(4)
# s[index] = "k"
#
# list20
# s = [1, 15, 4, 7]
# a = max(s)
# s.remove(a)
# print(max(s))
#
# list21
# s = [1, 15, 4, 7]
# a = min(s)
# s.remove(a)
# print(min(s))
#
# list22
# s = [1, 54, 13, 4, 7]
# for item in s:
#     if item % 2 ==0:
#         s.append(item)
#     else:
#         s.remove(item)
# print(s)
#
# list23
# s = [1, 54, 13, 4, 7]
# for item in s:
#     if item % 2 !=0:
#         s.append(item)
#     else:
#         s.remove(item)
# print(s)
#
# list24
# s = []
# print(len(s))
#
# list25
# s = []
# a = s[:]
#
# list26
# s = [14, 21, 4, 7, 8]
# length = len(s)
#
# if length % 2 != 0:
#     mid = length // 2
#     print(s[mid])
# else:
#     mid1 = length // 2 - 1
#     mid2 = length // 2
#     print(s[mid1], s[mid2])
#
# list27
# def subroyxat_max(royxat, start, end):
#
#     if not royxat or start < 0 or end > len(royxat) or start >= end:
#         return None
#     subroyxat = royxat[start:end]
#     return max(subroyxat)
#
# list28
# def subroyxat_min(royxat, start, end):
#
#     if not royxat or start < 0 or end > len(royxat) or start >= end:
#         return None
#     subroyxat = royxat[start:end]
#     return min(subroyxat)
#
# list29
# s = []
# index = "*"
# if index + 1 < len(s):
#     s.remove(s[index])
#     print(s)
# else:
#     print("Son aniqlanmadi")
#
#
# list30
# s = []
# print(s == sorted(s))
#
# list31
# def elementlarni_takrorlash(royxat, n):
#     natija = []
#     for element in royxat:
#         natija.extend([element] * n)
#     return natija
# print(elementlarni_takrorlash([1, 45, 4], 3))
#
# list32
# s = [1, 5, 8]
# a = [1, 5, 2]
# s.extend(a)
# d = sorted(s)
# print(d)
#
# list33
# s = [45, 41, 4, 7, 41, 8]
# a = 41
# index = []
# for i, item in enumerate(s):
#     if item == a:
#         index.append(i)
# print(index)
#
# list34
# s = [1, 2, 3, 4]
# rotated = s[-1:] + s[:-1]
# print(rotated)
#
# list35
# s = []
# a= int(input("enter a: "))
# b = int(input("enter b: "))
# for i in range(b):
#     if a <= i <= b:
#         s.append(i)
# print(s)
#
# list36
# s = [14, 15, -21, 8, -7]
# f = 0
# for item in s:
#     if item>0:
#         f += item
# print(f)
#
# list37
# s = [14, 15, -21, 8, -7]
# f = 0
# for item in s:
#     if item<0:
#         f += item
# print(f)
#
# list38
# s = []
# print(s == s.reverse())
#
#
# list39
# def create_nested_list(lst, size):
#     nested = [lst[i:i+size] for i in range(0, len(lst), size)]
#     return nested
#
# list40
# def get_unique_in_order(lst):
#     seen = set()
#     result = []
#     for item in lst:
#         if item not in seen:
#             seen.add(item)
#             result.append(item)
#     return result
#
# tuple1
# s = ()
# a = "*"
# print(s.count(a))
#
# tuple2
# s = ()
# a = list(s)
# print(max(a))
#
# tuple3
# s = (14, 45, 1, 8)
# a = list(s)
# print(min(a))
#
# tuple4
# s = (45, 8, 74, 4, 9)
# a = 8
# print(a in s)
#
# tuple5
# s = (1, 5)
# if s:
#     print(s[0])
# else:
#     print("set is empty")
#
#
# tuple6
# s = (1, 5)
# if s:
#     print(s[-1])
# else:
#     print("set is empty")
#
# tuple7
# s = ()
# print(len(s))
#
# tuple8
# s = (1, 2, 5, 4, 4,5)
# a = (list(s))[0:3]
# print(tuple(a))
#
# tuple9
# s = ()
# a = ()
# n = list(a) + list(s)
# print(tuple(n))
#
# tuple10
# s = ()
# print(s == ())

# tuple11
# s = (45, 41, 4, 7, 41, 8)
# a = 41
# index = []
# for i, item in enumerate(s):
#     if item == a:
#         index.append(i)
# print(index)
#
# tuple12
# s = (1, 15, 4, 7)
# m = list(s)
# a = max(m)
# m.remove(a)
# print(max(m))
#
# tuple13
# s = (1, 15, 4, 7)
# m = list(s)
# a = min(m)
# m.remove(a)
# print(min(m))
#
# tuple14
# s = (1,)
#
# tuple15
# s = []
# a = tuple(s)
#
# tuple16
# s = (1,45,2,3)
# sorted_s = sorted(s)
# print(tuple(sorted_s) == s)
#
# tuple17
# def max_of_subtuple(tpl, start, end):
#     if not tpl or start < 0 or end > len(tpl) or start >= end:
#         return None
#     subtuple = tpl[start:end]
#     return max(subtuple)
#
# tuple18
# def max_of_subtuple(tpl, start, end):
#     if not tpl or start < 0 or end > len(tpl) or start >= end:
#         return None
#     subtuple = tpl[start:end]
#     return min(subtuple)
#
# tuple19
# s = (12, 4, 8, 1, 10, 4, 8)
# n = 8
# a = list(s)
# a.remove(n)
# print(tuple(a))
#
# tuple20
# def create_nested_tuple(tpl, size):
#     nested = tuple(tpl[i:i+size] for i in range(0, len(tpl), size))
#     return nested
#
# tuple21
# def repeat_elements_tuple(tpl, n):
#     result = tuple(item for item in tpl for _ in range(n))
#     return result
#
# tuple22
# s = []
# a= int(input("enter a: "))
# b = int(input("enter b: "))
# for i in range(b):
#     if a <= i <= b:
#         s.append(i)
# print(tuple(s))
#
# tuple23
# s = ()
# a = list(s).reverse()
# print(tuple(a))
#
# tuple24
# s = ()
# a = list(s).reverse()
# print(tuple(a) == s)

# tuple25
# def get_unique_in_order(lst):
#     seen = set()
#     result = []
#     for item in lst:
#         if item not in seen:
#             seen.add(item)
#             result.append(item)
#     return tuple(result)
#
#
# set1
# set1. ={14, 4, 5}
# set2. = {14, 2, 3}
# set3 = set1. | set2.
# print(set3)
#
# set2
# s = {4, 5, 7, 9}
# b = {14, 41, 5, 8, 4}
# print(s & b)
#
# set3
# s = {4, 5, 7, 9}
# b = {14, 41, 5, 8, 4}
# print(s - b)
#
# set4
# s = {4, 5, 7, 9}
# b = {14, 41, 5, 8, 4}
# print(s.issubset(b))
#
# set5
# s = {14, 5, 9}
# a = 8
# print(a in s)
#
# set6
# s = {4, 8, 9, 10}
# print(len(s))
#
# set7
# s = [45, 7, 9, 7, 1]
# print(set(s))
#
# set8
# s = {5, 4, 3, 2, 1}
# a = 8
# if a in s:
#     s.remove(a)
# else:
#     print("Not found")
# print(s)
#
# set9
# s = {}
# print(s.clear())
#
# set10
# s = {}
# print(s == {})

# set11
# s = {1,2,30,4,5}
# a = {14,2,34,4,5}
# print(s.symmetric_difference(a))
#
# set12
# s = {45, 85,0}
# a = 8
# s.add(a)
# print(s)
#
# set13
# s = {4, 8, 9}
# s.pop()
# print(s)
#
# set14
# s = {}
# a = max(s)
# print(a)
#
# set15
# s = {}
# a = min(s)
# print(a)
#
# set16
# s = {45, 8, 9, 4, 23}
# a = set()
# for i in s:
#     if i % 2 == 0:
#         a.add(i)
# print(a)
#
# set17
# s = {45, 8, 9, 4, 23}
# a = set()
# for i in s:
#     if i % 2 != 0:
#         a.add(i)
# print(a)
#
# set18
# s = []
# a= int(input("enter a: "))
# b = int(input("enter b: "))
# for i in range(b):
#     if a <= i <= b:
#         s.append(i)
# print(set(s))
#
# set19
# s = set()
# a = set()
# print(s.update(a))
#
# set20
# s = {1, 54, 8}
# a = {25, 8, 9}
# print(a == s)
#
# set21
# s = []
# a = set(s)
# print(list(a))
#
# set22
# s = []
# a = set(s)
# d = 0
# for i in a:
#     d += 1
# print(d)
#
# set23
# a = int(input("Enter a number: "))
# b = int(input("Enter b number: "))
# b = int(input())
# my_set = set(range(a, b))
# print(my_set)
#
# dict1
# s = dict()
# key = "*"
# if key in s:
#     print(s[key])
# else:
#     print("key not found")
#
# dict2
# s = dict()
# key = "*"
# print(key in s)
#
# dict3
# s = dict()
# print(len(s))
#
# dict4
# s = dict()
# print(list(s.keys()))
#
# dict5
# s = dict()
# print(list(s.values()))
#
# dict6
# s = dict()
# a = dict()
# s.update(a)
# print(a)
#
# dict7
# s = dict()
# key = "*"
# if key in s:
#     s.pop(key)
#     print(s)
# else:
#     print("key not found")
#
# dict8
# s = dict()
# print(s.clear())
#
# dict9
# s = dict()
# print(s == {})
#
# dict10
# s= dict()
# key = "*"
# if key in s:
#     print((key,s[key]))
# else:
#     print("key not found")
#
# dict11
# s= dict()
# key = "*"
#s[key] = 215
#print(s)

# dict12
# s = dict({"asd":14, "asb":"value"})
# v = "value"
# a = list(s.values())
# print(a.count(v))
#
# dict13
# s = {"a": 1, "b": 2, "c": 3}
# inverted = {}
# for k, v in s.items():
#     inverted[v] = k
# print(inverted)
#
# dict14
# s = {"as":45,"q":4,"s":4}
# c = []
# value = 4
# for i in s:
#     if value == s[i]:
#         c.append(i)
# print(c)
#
# dict15
# a = []
# keys = ["a", "b", "c"]
# values = [1, 2, 3]
# my_dict = dict(zip(keys, values))
# print(my_dict)
#
# dict16
# s = {}
# for k, v in s.items():
#     if isinstance(v, dict):
#         print(f"Key '{k}' nested dictionaryga ega:", v)
#
# dict17
# student = {
#     "name": "Ali",
#     "grades": {
#         "math": 90,
#         "physics": 85
#     }
# }
# print(student["grades"]["math"])
# print(student["grades"]["physics"])
#
# dict18
# from collections import defaultdict
# my_dict = defaultdict(int)
# my_dict["a"] = 5
# print(my_dict["b"])

# dict19
# s = {"a":45,"b":47,"c":40,"d":45}
# a = set(s.values())
# print(len(a))
#
# dict20
# s = {"b": 2, "a": 1, "c": 3}
# sorted_dict = dict(sorted(s.items()))
# print(sorted_dict)
#
# dict21
# s = {"b": 2, "a": 5, "c": 1}
# sorted_dict = dict(sorted(s.items(), key=lambda item: item[1]))
# print(sorted_dict)

# dict22
# s = {"a": 5, "b": 12, "c": 7, "d": 20}
# filtered = {k: v for k, v in s.items() if v > 10}
# print(filtered)
#
# dict23
# dict1 = {"a": 1, "b": 2, "c": 3}
# dict2 = {"c": 4, "d": 5, "e": 6}
# common_keys = set(dict1.keys()) & set(dict2.keys())
# print(common_keys)
#
# dict24
# t = (("name", "Umidbek"), ("age", 25))
# d = {}
# for k, v in t:
#     d[k] = v
# print(d)
#
# dict25
# s = {"x": 10, "y": 20, "z": 30}
# first_pair = list(s.items())[0]
# print(first_pair)






