import os

#定义复制单个文件的函数
def mycopy(file1,file2):
	'''
	这个函数实现单个文件的复制
	将file1文件复制到file2文件中
	'''
	#打开文件
	f1 = open(file1,"rb")
	f2 = open(file2,"wb")
	#读取并复制文件
	content = f1.readline()
	while len(content)>0:
		f2.write(content)
		content = f1.readline()
	#关闭文件
	f1.close()
	f2.close()

#定义复制目录的函数
def copydir(dir1,dir2):
	'''
	这个函数实现将dir1中的所有文件（包括目录）复制到dir2中
	'''
	#获取源目录中的文件列表
	a = os.listdir(dir1)
	#创建目标目录
	os.mkdir(dir2)
	#遍历源目录并复制
	for i in a:
		#获取源文件和目标文件目录路径
		file1 = os.path.join(dir1,i)  #源文件
		file2 = os.path.join(dir2,i)  #目标文件
		#判断是文件还是目录，分别进行相应的操作
		if os.path.isfile(file1):
			mycopy(file1,file2)        #是文件，直接调用文件复制函数
		elif os.path.isdir(file1):
			copydir(file1,file2)       #是目录，递归调用copydir()函数即可

#测试
copydir("./mydir","./copy_mydir")

