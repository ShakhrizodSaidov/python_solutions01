
ranglar = {'qizil', 'oq', 'yashil'}
ranglar.add('sariq')
ranglar.update(["ko'k", 'qora', 'pushti'])

# Umumiy elementlar
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set3 = set1 & set2
# # `print(set3)

# To'plamlar orasida farq
print(set1.difference(set2))
print(set2.difference(set1))

# Simmetrik farq
print(set1.symmetric_difference(set2))