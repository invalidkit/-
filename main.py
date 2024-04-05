result = []
other = []

a = None
b = None
'''def divider(a, b):
  if a < b:
    raise ValueError
  if b > 100:
    raise IndexError
  return a/b
data = {10: 2, 2: 5, 123: 4, 18: 0, 8 : 4}
for key in data:
  res = divider(key, data[key])
  result.append(res)'''

try:
    a = 10
    b = 2
    other.append(a/b)
except ValueError as v:
    result.append(v)
except IndexError as r:
    result.append(r)
except TypeError as r:
    result.append(r)
except ZeroDivisionError as r:
    result.append(r)

try:
    a = 2
    b = 5
    other.append(a/b)
except ValueError as v:
    result.append(v)
except IndexError as r:
    result.append(r)
except TypeError as r:
    result.append(r)
except ZeroDivisionError as r:
    result.append(r)

try:
    a = "123"
    b = 4
    other.append(a/b)
except ValueError as v:
    result.append(v)
except IndexError as r:
    result.append(r)
except TypeError as r:
    result.append(r)
except ZeroDivisionError as r:
    result.append(r)

try:
    a = []
    b = 15
    other.append(a/b)
except ValueError as v:
    result.append(v)
except IndexError as r:
    result.append(r)
except TypeError as r:
    result.append(r)
except ZeroDivisionError as r:
    result.append(r)

try:
    a = 18
    b = 0
    other.append(a/b)
except ValueError as v:
    result.append(v)
except IndexError as r:
    result.append(r)
except TypeError as r:
    result.append(r)
except ZeroDivisionError as r:
    result.append(r)

try:
    a = 8
    b = 4
    other.append(a/b)
except ValueError as v:
    result.append(v)
except IndexError as r:
    result.append(r)
except TypeError as r:
    result.append(r)
except ZeroDivisionError as r:
    result.append(r)


print(result)