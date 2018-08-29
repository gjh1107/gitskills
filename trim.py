def trim(s):
	while(s[:1]==' '):
		s=s[1:]
	while(s[-1:]==' '):
		s=s[:-1]
	return s
	

#addTest add add
# 测试: 
#add feature1 and test1
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
