data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 10000 == 0 :
			print(len(data))
print('檔案讀取完了,總共有', len(data), '筆資料')	

sum_len = 0
for d in data:
	L=len(d)
	sum_len = sum_len + L
print('平均字數是',sum_len/len(data))

new = []
for d in data:
	if len(d) < 100 :
		new.append(d)
print(new[0])	
