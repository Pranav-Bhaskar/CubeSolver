from PIL import Image

'''
RED = R
BLUE = B
GREEN = G
WHITE = W
YELLOW = Y
ORRANGE = O
'''

f1 = 'final.combi'
RGBval = {'R':(255,0,0),'B':(0,0,255),'G':(0,255,0),'W':(255,255,255),'Y':(255,255,0),'O':(255,128,0),'X':(0,0,0)}
emp = [['X','X','X'],['X','X','X'],['X','X','X']]

def transp(arr):										#TRANSPOSE FUNCTION
	res = [list(i) for i in zip(*arr)]
	return res
	
def inc(make):
	carr = 1
	ekam = make[::-1]
	mun = ''
	for x in ekam:
		temp = int(x)+carr
		carr = 0
		if temp == 6:
			carr = 1
			temp = 0
		mun = str(temp) + mun
	if carr:
		mun = '0' + mun
	return mun
		
def dup(make):
	for x in ['02','15','34','6','7','8','9','0000','1111','2222','3333','4444','5555']:
		if x in make:
			return 1
	return 0

def checker(make):
	jum = 1
	while jum:
		make = inc(make)
		jum = dup(make)
	return make




def summer(R,B,G,Y,W,O):
	s = str()
	s = s+''.join([str(item) for sublist in R for item in sublist])
	s = s+''.join([str(item) for sublist in B for item in sublist])
	s = s+''.join([str(item) for sublist in G for item in sublist])
	s = s+''.join([str(item) for sublist in Y for item in sublist])
	s = s+''.join([str(item) for sublist in W for item in sublist])
	s = s+''.join([str(item) for sublist in O for item in sublist])
	return s

def distb(s):
	R = []
	R.append(list(s[:3]))
	s = s[3:]
	R.append(list(s[:3]))
	s = s[3:]
	R.append(list(s[:3]))
	s = s[3:]
	B = []
	B.append(list(s[:3]))
	s = s[3:]
	B.append(list(s[:3]))
	s = s[3:]
	B.append(list(s[:3]))
	s = s[3:]
	G = []
	G.append(list(s[:3]))
	s = s[3:]
	G.append(list(s[:3]))
	s = s[3:]
	G.append(list(s[:3]))
	s = s[3:]		
	Y = []
	Y.append(list(s[:3]))
	s = s[3:]
	Y.append(list(s[:3]))
	s = s[3:]
	Y.append(list(s[:3]))
	s = s[3:]
	W = []
	W.append(list(s[:3]))
	s = s[3:]
	W.append(list(s[:3]))
	s = s[3:]
	W.append(list(s[:3]))
	s = s[3:]
	O = []
	O.append(list(s[:3]))
	s = s[3:]
	O.append(list(s[:3]))
	s = s[3:]
	O.append(list(s[:3]))
	return R,B,G,Y,W,O
	
	
def printer(R,B,G,Y,W,O):
	cube.append(emp)
	cube.append(Y)
	cube.append(emp)
	cube.append(emp)
	cube.append(R)
	cube.append(G)
	cube.append(O)
	cube.append(B)	
	cube.append(emp)
	cube.append(W)
	cube.append(emp)	
	cube.append(emp)
	
	
	rez = [[cube[j][i] for j in range(len(cube))] for i in range(len(cube[0]))]

	img = []
	rez[2][11][2]
	
	for k in range(3):
		for x in range(3):
			for j in range(99):
				for y in range(4):
					for z in range(3):
						for i in range(99):
							img.append(RGBval[rez[x][(y+(k*4))][z]])
						img.append((0,0,0))
			for l in range(1200):
				img.append((0,0,0))
		
	im = Image.new('RGB',(1200,900))
	im.putdata(img)
	im.show()
	
def front(R,B,G,Y,W,O):											#FRONT ROTATION
	T = O[0][0]
	O[0][0] = Y[2][0]
	K = W[0][2]
	W[0][2] = T
	Y[2][0] = R[2][2]
	R[2][2] = K
	
	T = O[1][0]
	O[1][0] = Y[2][1]
	K = W[0][1]
	W[0][1] = T
	Y[2][1] = R[1][2]
	R[1][2] = K
	
	T = O[2][0]
	O[2][0] = Y[2][2]
	K = W[0][0]
	W[0][0] = T
	Y[2][2] = R[0][2]
	R[0][2] = K
	
	T = G[0][2]
	G[0][2] = G[0][0]
	K = G[2][2]
	G[2][2] = T
	G[0][0] = G[2][0]
	G[2][0] = K
	
	T = G[1][2]
	G[1][2] = G[0][1]
	K = G[2][1]
	G[2][1] = T
	G[0][1] = G[1][0]
	G[1][0] = K
	return R,B,G,Y,W,O

def right(R,B,G,Y,W,O):										#RIGHT ROTATION
	k = transp(B)
	l = transp(W)
	i = l[2]
	k[0] = k[0][::-1]
	l[2] = k[0]
	W = transp(l)
	l = transp(G)
	n=l[2]
	l[2]=i
	G = transp(l)
	l = transp(Y)
	l[2] = l[2][::-1]
	k[0]=l[2]
	B = transp(k)
	l[2] = n
	Y = transp(l)
	
	T = O[0][2]
	O[0][2] = O[0][0]
	K = O[2][2]
	O[2][2] = T
	O[0][0] = O[2][0]
	O[2][0] = K
	
	T = O[1][2]
	O[1][2] = O[0][1]
	K = O[2][1]
	O[2][1] = T
	O[0][1] = O[1][0]
	O[1][0] = K
	
	return R,B,G,Y,W,O
	
def left(R,B,G,Y,W,O):
	k = transp(B)
	l = transp(W)
	i = l[0]
	k[2] = k[2][::-1]
	l[0] = k[2]
	W = transp(l)
	l = transp(G)
	n=l[0]
	l[0]=i
	G = transp(l)
	l = transp(Y)
	l[0] = l[0][::-1]
	k[2]=l[0]
	B = transp(k)
	l[0] = n
	Y = transp(l)
	
	L = R[0][0]
	R[0][0] = R[0][2]
	R[0][2] = R[2][2]
	R[2][2] = R[2][0]
	R[2][0] = L
	
	L = R[0][1]
	R[0][1] = R[1][2]
	R[1][2] = R[2][1]
	R[2][1] = R[1][0]
	R[1][0] = L
	
	return R,B,G,Y,W,O
	

def upper(R,B,G,Y,W,O):
	L = G[0]
	G[0] = O[0]
	O[0] = B[0]
	B[0] = R[0]
	R[0] = L
	
	T = Y[0][2]
	Y[0][2] = Y[0][0]
	K = Y[2][2]
	Y[2][2] = T
	Y[0][0] = Y[2][0]
	Y[2][0] = K
	
	T = Y[1][2]
	Y[1][2] = Y[0][1]
	K = Y[2][1]
	Y[2][1] = T
	Y[0][1] = Y[1][0]
	Y[1][0] = K
	
	return R,B,G,Y,W,O
	
def down(R,B,G,Y,W,O):
	L = G[2]
	G[2] = R[2]
	R[2] = B[2]
	B[2] = O[2]
	O[2] = L
	
	T = W[0][2]
	W[0][2] = W[0][0]
	K = W[2][2]
	W[2][2] = T
	W[0][0] = W[2][0]
	W[2][0] = K
	
	T = W[1][2]
	W[1][2] = W[0][1]
	K = W[2][1]
	W[2][1] = T
	W[0][1] = W[1][0]
	W[1][0] = K
	
	return R,B,G,Y,W,O

def bottom(R,B,G,Y,W,O):
	T = Y[0][2]
	Y[0][2] = O[2][2]
	O[2][2] = W[2][0]
	W[2][0] = R[0][0]
	R[0][0] = T
	
	T = Y[0][1]
	Y[0][1] = O[1][2]
	O[1][2] = W[2][1]
	W[2][1] = R[1][0]
	R[1][0] = T
	
	T = Y[0][0]
	Y[0][0] = O[0][2]
	O[0][2] = W[2][2]
	W[2][2] = R[2][0]
	R[2][0] = T
	
	T = B[0][2]			#CLOCKWISE
	B[0][2] = B[0][0]
	K = B[2][2]
	B[2][2] = T
	B[0][0] = B[2][0]
	B[2][0] = K
	
	T = B[1][2]
	B[1][2] = B[0][1]
	K = B[2][1]
	B[2][1] = T
	B[0][1] = B[1][0]
	B[1][0] = K
	
	return R,B,G,Y,W,O
	

cube = list()

R = []
B = []
G = []
Y = []
W = []
O = []

'''
#test case 1
R = [['Y','W','W'],['Y','R','G'],['R','W','O']]
B = [['B','B','B'],['B','B','B'],['B','B','B']]
G = [['G','G','Y'],['Y','G','W'],['W','Y','G']]
Y = [['O','R','O'],['R','Y','Y'],['R','O','O']]
W = [['G','R','Y'],['G','W','G'],['W','W','Y']]
O = [['G','O','W'],['O','O','O'],['R','R','R']]
'''
'''
#test case 2
R = [['W','B','R'],['G','R','Y'],['Y','W','Y']]
B = [['R','O','B'],['W','B','O'],['Y','W','R']]
G = [['W','G','G'],['B','G','R'],['B','R','W']]
Y = [['R','B','Y'],['R','Y','W'],['G','Y','O']]
W = [['O','G','B'],['R','W','Y'],['G','G','O']]
O = [['W','B','B'],['Y','O','O'],['O','O','G']]
'''
'''
#TEST CASE 0
R = [['G','G','G'],['R','R','R'],['R','R','R']]
B = [['R','R','R'],['B','B','B'],['B','B','B']]
G = [['O','O','O'],['G','G','G'],['G','G','G']]
Y = [['Y','Y','Y'],['Y','Y','Y'],['Y','Y','Y']]
W = [['W','W','W'],['W','W','W'],['W','W','W']]
O = [['B','B','B'],['O','O','O'],['O','O','O']]
'''
'''
#TEST CASE 3
R = [['G','G','G'],['R','R','R'],['R','R','R']]
B = [['Y','R','R'],['Y','B','B'],['Y','B','B']]
G = [['O','O','W'],['G','G','W'],['G','G','W']]
Y = [['Y','Y','O'],['Y','Y','G'],['Y','Y','G']]
W = [['W','W','B'],['W','W','B'],['W','W','R']]
O = [['O','O','B'],['O','O','B'],['O','O','B']]
'''
'''
#TEST CASE 4 - failed
R = [['Y','B','B'],['R','R','R'],['G','G','Y']]
B = [['O','O','O'],['Y','B','B'],['Y','R','R']]
G = [['R','R','W'],['G','G','W'],['G','O','W']]
Y = [['G','G','G'],['Y','Y','Y'],['Y','Y','O']]
W = [['R','W','R'],['W','W','B'],['W','W','B']]
O = [['B','G','W'],['B','O','O'],['B','O','O']]
'''
'''
#TEST CASE 5
R = [['B','R','B'],['B','R','B'],['Y','R','G']]
B = [['Y','O','Y'],['Y','B','Y'],['O','O','G']]
G = [['W','R','B'],['W','G','B'],['O','R','R']]
Y = [['R','G','R'],['G','Y','W'],['R','Y','W']]
W = [['W','W','W'],['B','W','W'],['O','Y','Y']]
O = [['O','O','G'],['O','O','G'],['G','G','B']]
'''
'''
#test case 6
R = [['O','G','O'],['R','R','R'],['R','R','R']]
B = [['W','W','W'],['Y','B','Y'],['Y','B','Y']]
G = [['Y','Y','Y'],['W','G','W'],['W','G','W']]
Y = [['G','G','G'],['R','Y','Y'],['G','G','G']]
W = [['B','O','B'],['B','W','B'],['B','W','B']]
O = [['R','B','R'],['O','O','O'],['O','O','O']]
'''
while len(R+B+G+Y+W+O) != 18:
	print(len(R+B+G+Y+W+O))
	m = list(input('Enter side : ').strip())
	l=[]
	l.append(m[:3])
	l.append(m[3:-3])
	l.append(m[-3:])
	if l[1][1] == 'R':
		R = l
		print(R)
	elif l[1][1] == 'B':
		B = l
		print(B)
	elif l[1][1] == 'G':
		G = l
		print(G)
	elif l[1][1] == 'Y':
		Y = l
		print(Y)
	elif l[1][1] == 'W':
		W = l
		print(W)
	elif l[1][1] == 'O':
		O = l
		print(O)
	else:
		print('Retry')
def printed(t):
	t = list(t)
	print(t)
	t = t[::-1]
	ans = ''.join(t)
	for x in ['0000','1111','2222','3333','4444','5555']:
		ans = ans.replace(x,'')
	print('1.Check if the image matches your cube')
	print('2.May the center of green be facing you')
	print('3.Red on the left and yellow on top')
	for x in ans:
		if x == '0':
			print('~Right')
		elif x == '1':
			print('~Face')
		elif x == '2':
			print('~Left')
		elif x == '3':
			print('~Top')
		elif x == '4':
			print('~Down')
		elif x == '5':
			print('~Back')

def exten(k,num):
	made = ''
	temp_file = open('temp.comb','w')
	temp_file.close()
	if num == 0:
		temp_file = open('temp.comb','a+')
		sumed = k + '-' + '9\n'
		temp_file.write(sumed)
		temp_file.close()
		return
	while True:
		made = checker(made)
		if len(made) < num:
			continue
		if len(made) > num:									#The Depth Of Search
			return 
		R,B,G,Y,W,O = distb(k)
		for x in made:
			if x == '0':
				R,B,G,Y,W,O = right(R,B,G,Y,W,O)
			elif x == '1':
				R,B,G,Y,W,O = front(R,B,G,Y,W,O)
			elif x == '2':
				R,B,G,Y,W,O = left(R,B,G,Y,W,O)
			elif x == '3':
				R,B,G,Y,W,O = upper(R,B,G,Y,W,O)
			elif x == '4':
				R,B,G,Y,W,O = down(R,B,G,Y,W,O)
			elif x == '5':
				R,B,G,Y,W,O = bottom(R,B,G,Y,W,O)
			else:
				print ("Error"*100)
				continue
		temp_file = open('temp.comb','a+')
		sumed = summer(R,B,G,Y,W,O) + '-' + made + '\n'
		temp_file.write(sumed)
		temp_file.close()

s = []
k = summer(R,B,G,Y,W,O)
print(k)
#k = 'BGYBRORYOOBORBOGGYRRRGGWBBBYRGWYYGGGWWWOWWBYYWBWOOYRRO'
printer(R,B,G,Y,W,O)
num = 0
while num <= 8:
	print('Preparing Data ' + str(num) + '.')
	exten(k,num)
	num += 1
	temp_file = open('temp.comb','r')
	ext = list(temp_file)
	temp_file.close()
	print('Starting Search ' + str(num-1) + '.')
	for kut in ext:
		sup = kut.strip().split('-')
		with open(f1) as f:
			for line in f:
				s = line.strip().split('-')
				if s[0] == sup[0]:
					printed(s[1]+sup[1])
					exit()
print('Prog Ended')
