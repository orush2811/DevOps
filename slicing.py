# slicing - creating a sub string by slicing or extracting elements from another string
# we can use indexing[] or slice()
# [start:stop:step]
name = "Or Itach"
first_name = name[0:2]
last_name = name[3:8]
funny_name = name[0:7:2] # or [::2] will give the same result
reversed_name = name[::-1]
print(first_name)
print(last_name)
print(funny_name)
print(reversed_name)