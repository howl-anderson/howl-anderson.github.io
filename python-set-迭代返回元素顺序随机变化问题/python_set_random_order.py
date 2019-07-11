# -*- coding: utf-8 -*-
data = ['人之初', '性本善', '性相近', '习相远', '苟不教', '性乃迁']

def generate_a_set(data):
  a_set = set()
  for i in data:
    a_set.add(i)
    
  return a_set

def print_hash(data):
  for i in data:
    print(hash(i))

print_hash(data)
a_set = generate_a_set(data)
print(list(a_set))

