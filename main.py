import random
import os
g= open("sample_1.txt","a+")
g.close() 	

g= open("sample_2.txt","a+")
g.close() 	

g= open("sample_3.txt","a+")
g.close() 	

g= open("sample_4.txt","a+")
g.close()

g= open("sample_5.txt","a+")
g.close() 	
 	
g= open("sample_6.txt","a+")
g.close() 	

g= open("sample_7.txt","a+")
g.close() 	

g= open("sample_8.txt","a+")
g.close() 	

g= open("sample_10.txt","a+")
g.close() 	

g= open("sample_11.txt","a+")
g.close() 	

g= open("sample_12.txt","a+")
g.close() 	

id_game = int(input())

game = "sample_" + str(id_game) + ".txt"



f= open(game,'r')
f1 = f.readlines()	
for x in f1:
	temp = x
f.close()
r = open(game,"a+")
 	

	
chk=0
ini= []
for x in range(1023,9877):
	ini.append((x))

# to remove ones not required
ls=[]
co=0
for i in range(0,len(ini)):
	no= str(ini[i])
	for x in range(0,4):
		for y in range(0,4):
			if no[x]==no[y]:
				co+=1
	if co<5:
		ls.append(ini[i])
	co=0
	
#for x in range(0,len(ls)):
#		print(ls[x])
non=str(random.choice(ls))
print(non)

entry= int(input())

bulls = 0

if entry==1:
	if(os.stat(game).st_size):
		guess = temp
		if len(temp)==2 :
			guess=str(random.choice(ls))	
	else:	
		guess=str(random.choice(ls))
#	chk+=1
	print(int(guess))
	bulls = int(input())
	cows = int(input())
	danger_2=str(input())
	balls=0
	carts=0

	for x in range(0,4):
		found=0
		if danger_2 =='0':
			danger_2='0000'
		if danger_2[x]==non[x]:
			balls+=1
		for y in range(0,4):
			if danger_2[y]==non[x]:
				found+=1
		if found>0:
			carts+=1
			
	
	carts=carts-balls		
	print(balls)
	print(carts)
	carts=0
	balls=0


	
	if bulls!=4:
	# part 1
		b=int(0)
		c=int(0)
		new=[]

		for i in range(0,len(ls)):
			no= str(ls[i])
			for x in range(0,4):
				if guess[x]==no[x]:
					b+=1
				for y in range(0,4):
					if guess[x]==no[y]:
						c+=1
			c=c-b				

			if b==bulls and c==cows:
				new.append(ls[i])
			b=0
			c=0		
	while(bulls!=4):
		guess=str(random.choice(new))
		chk+=1
		print(int(guess))
		bulls = int(input())
		cows = int(input())
		danger_2=str(input())
		balls=0
		carts=0
		for x in range(0,4):
			found=0
			if danger_2 =='0':
				danger_2='0000'
			if danger_2[x]==non[x]:
				balls+=1
			for y in range(0,4):
				if danger_2[y]==non[x]:
					found+=1
			if found>0:
				carts+=1
			
	
		carts=carts-balls		
		print(balls)
		print(carts)
		carts=0
		balls=0	
		if(bulls!=4):
			r.write('5')
			r.write('\n')
		if bulls==4:
			r.write(guess)
			r.write('\n')
			r.close()	
		new_1=[]

		if bulls!=4:

			for i in range(0,len(new)):
				no= str(new[i])
				for x in range(0,4):
					if guess[x]==no[x]:
						b+=1
					for y in range(0,4):
						if guess[x]==no[y]:
							c+=1
				c=c-b				

				if b==bulls and c==cows:
					new_1.append(new[i])
				b=0
				c=0	
		new = new_1

if entry==0:
	danger_2= str(input())
	balls=0
	carts=0
	for x in range(0,4):
		found=0
		if danger_2 =='0':
			danger_2='0000'	
		if danger_2[x]==non[x]:
			balls+=1
		for y in range(0,4):
			if danger_2[y]==non[x]:
				found+=1
		if found>0:
			carts+=1
	carts=carts-balls		
	print(balls)
	print(carts)
	balls=0
	carts=0	
	if(os.stat(game).st_size):
		guess = temp
		if len(temp)==2:
			guess=str(random.choice(ls))
	else:
		guess=str(random.choice(ls))		
#	chk+=1
	print(int(guess))
	bulls = int(input())
	cows = int(input())
	
	
	if bulls!=4:
	# part 1
		b=int(0)
		c=int(0)
		new=[]

		for i in range(0,len(ls)):
			no= str(ls[i])
			for x in range(0,4):
				if guess[x]==no[x]:
					b+=1
				for y in range(0,4):
					if guess[x]==no[y]:
						c+=1
			c=c-b				

			if b==bulls and c==cows:
				new.append(ls[i])
			b=0
			c=0	
	while (bulls!=4):
		danger_2=str(input())
		balls=0
		carts=0
		for x in range(0,4):
			found=0
			if danger_2 =='0':
				danger_2='0000'
			if danger_2[x]==non[x]:
				balls+=1
			for y in range(0,4):
				if danger_2[y]==non[x]:
					found+=1
			if found>0:
				carts+=1
		carts=carts-balls		
		print(balls)
		print(carts)
		carts=0
		balls=0	
		guess=str(random.choice(new))
#		chk+=1
		print(int(guess))
		bulls = int(input())
		cows = int(input())		

		if(bulls!=4):
			r.write('5')
			r.write('\n')	
		if bulls==4:
			r.write(guess)
			r.write('\n')
			r.close()	
		new_1=[]
		
		if bulls!=4:

			for i in range(0,len(new)):
				no= str(new[i])
				for x in range(0,4):
					if guess[x]==no[x]:
						b+=1
					for y in range(0,4):
						if guess[x]==no[y]:
							c+=1
				c=c-b				

				if b==bulls and c==cows:
					new_1.append(new[i])
				b=0
				c=0	
		
		new = new_1
