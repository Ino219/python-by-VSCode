#検証データ
lplList=["VSSLPL1_Port1","VDDLPL2_Port1","VSSLPL1_Port2","VDDLPL2_Port2"]
lifYmin=0.02
lpl1Ymin=1.78
lpl2Ymin=1.54
lifYmax=0.023
lpl1Ymax=1.95
lpl2Ymax=1.73

#Yの最小値を求める間に合わせの関数
def Ymin(portlist):
	if portlist=="VSSLPL1_Port":
		return lpl1Ymin
	elif portlist=="VDDLPL2_Port":
		return lpl2Ymin
	else:
		return lifYmin

def Ymax(portlist):
	if portlist=="VSSLPL1_Port":
		return lpl1Ymax
	elif portlist=="VDDLPL2_Port":
		return lpl2Ymax
	else:
		return lifYmax


#ポート名を正規化する関数
def Normalize(port):
	flag=False
	while flag==False:
		if port[-1].isdecimal():
			port=port[:-1]
		else:
			flag=True
	return port
def Normalize2(port):
	while True:
		if port[-1].isdecimal():
			port=port[:-1]
		else:
			break
	return port
#データ型の準備
lplsList=[]
lpl_dict=dict()
normalList=[]
#lplリストから正規化したポート名をもとにグループ分け
for lpl in lplList:
	checkList=[]
	checkList.append(lpl)
	normal=Normalize2(lpl)
	for lpl2 in lplList:
		if lpl==lpl2:
			continue
		elif normal==Normalize2(lpl2):
			checkList.append(lpl2)
			checkList.sort()
	if len(checkList) >1 and checkList not in lplsList:
		lplsList.append(checkList)
		lpl_dict[normal]=checkList
		normalList.append(normal)
print(lplsList)
print(lpl_dict)
print(normalList)

#正規化したポート名をキーにして、そのグループのポートのY最小値を値として辞書型に格納
port_Ymin_dict=dict()
port_Ymin_dict["LIF"]=lifYmin
for normal1 in normalList:
	port_Ymin_dict[normal1]=Ymin(normal1)
#上記の辞書型をY最小値でソート
port_Ymin_dict_sort=sorted(port_Ymin_dict.items(),key=lambda i:i[1])

print(port_Ymin_dict)
print(dict(port_Ymin_dict_sort))
print(list(dict(port_Ymin_dict_sort).keys()))
#ポートグループ名のリストを取得
keysList=list(dict(port_Ymin_dict_sort).keys())
#上記リストから先頭の項目削除
tmpkeysList=keysList[1:]
print(tmpkeysList)
#双方のリストをzipでまとめて取得
k_kList=list(zip(keysList,tmpkeysList))
print(k_kList)

for kk in k_kList:
	Ymaxs=Ymax(kk[0])
	Ymins=Ymin(kk[1])
	height_=Ymins-Ymaxs
	print(Ymaxs)
	print(Ymins)
	print(height_)
	#この二つからCreateRectangleでRectangleを作成
	#Rectangleを切り離して、次のループへ移行

print(Normalize("VDDLPL2_Port189"))
print(Normalize2("VSSLPL2_Port229"))