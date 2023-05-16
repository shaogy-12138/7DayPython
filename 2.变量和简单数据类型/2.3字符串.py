# 数据类型： 字符串
# 字符串： 一系列字字符。 单引号、双引号引起的都是字符串
# 'xxx', "xxx" 等都是字符串  '''XXX XXXX ''' 可以存储多行字符串
str1 = 'abcd'
str2 = "efgh"
str3 = '''
123
456
'''

#print(str1, str2, str3)

# 字符串的相关操作  字符串.方法()
# 1. 修改字符串中的大小写: 将首字符大写， 其余均为小写
name = "ada love aBc"
print("====================================") # 会自动换行
print(name.title()) # Ada Love Abc

# 2. 全部转大写 upper
print("====================================") # 会自动换行
print(name.upper()) # ADA LOVE ABC

# 3. 全部转小写 lower
print("====================================") # 会自动换行
print(name.lower()) # ada love abc

# 4. 字符串拼接:  str1 + str2 + ...
girl_friend = "dmm"
name = "jason"
con_info = girl_friend.title()+" is "+name.title()+" girl friend"
print("====================================") # 会自动换行
print(con_info) # Dmm is Jason girl friend

# 5. 删除字符串中的空白 rstrip-删除最右边的空白  lstrip-删除左边的空白  strip-删除两端的空白
# 这些操作都不对原字符串进行修改， 只是暂时的 不会影响原字符串值
print("====================================") # 会自动换行
strip_test = "    1234    "
print("|"+strip_test+"|")
print("|"+strip_test.rstrip()+"|")
print("|"+strip_test.lstrip()+"|")
print("|"+strip_test.strip()+"|")
print("====================================") # 会自动换行



# 制表符或换行符添加空白
print("====================================") # 会自动换行
print(name)
print("\t"+name) # 	___jason (_表示空白)
print(name+"\n"+girl_friend+"\n========")
print(name+"\n\t"+girl_friend+"\n========")
print("====================================") # 会自动换行

# 2-3 个性化消息
name = "eric"
print("Hello "+name.title()+", would you like to learn some Python today?")
print("====================================") # 会自动换行

# 2-4  调整名字大小写
print(name)
print(name.lower())
print(name.upper())
print(name.title())
print("====================================") # 会自动换行

# 2-5 名言
my = 'Albert Einstein once said, "A person who never made a mistake never tried anything new"'
print(my)
print("====================================") # 会自动换行

# 2-6 名言2
famous_person = "Einstein"
message = 'Albert {} once said, "A person who never made a mistake never tried anything new"'.format(famous_person)
print(message)
print("====================================") # 会自动换行

# 2-7 剔除人名中的空白
famous_person = "\t\tEinsten\t\t\n\t"
print(famous_person.strip())
print(famous_person.lstrip())
print(famous_person.rstrip())
print("====================================") # 会自动换行
