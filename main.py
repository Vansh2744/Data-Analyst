scores = [12,34,56,78,90,100]

res = (score for score in scores if score > 50)

print(next(res))
print(next(res))
print(next(res))