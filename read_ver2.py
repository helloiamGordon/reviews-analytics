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
good = []
for d in data:
	if 'good' in d :
		good.append(d)
print('一共有' ,len(good) ,'含有GOOD的留言')

wc = {}
for d in data :
	words = d.split(' ')
	for word in words :
		if word in wc :
			wc[word] += 1
		else :
			 wc[word] = 1
for word in wc :
	if wc[word] > 1000000:
		print(word, wc[word])
while True :
	word = input('請輸入查詢字: ')
	if word == 'q' :
		break
	if word in wc:
		print('您查詢的', word,'出現過',wc[word],'次')
	else :
		print('查無此字!')	
print('感謝您使用此功能')
