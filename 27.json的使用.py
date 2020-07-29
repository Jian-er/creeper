import json

str = '{"name":"盗梦空间"}'
obj = json.loads(str)

# print(type(obj))

obj_str = json.dumps(obj, ensure_ascii=False)
print(obj_str)


# 把对象保存成文件

json.dump(obj, open('movie.txt', 'w', encoding='utf-8'), ensure_ascii=False)

# 把文件的内容转到python
obj2 = json.load(open("movie.txt", encoding='utf-8'))
print(obj2)