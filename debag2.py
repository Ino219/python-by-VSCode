#debag2

import random

cmpNameList=["c12","c13","c14","c15","c16"]
PinNameList=["c12_1","c12_2","c13_1","c13_2","c14_1","c14_2","c15_1","c15_2","c16_1","c16_2"]

tempX=[]
tempY=[]

c16_X=[]
c16_Y=[]

c16_1_loc=[3,4]
c16_2_loc=[8,4]
c16_pin=[c16_1_loc,c16_2_loc]


#2要素で乱数リストを返すメソッド
def randomList(pinName):
    x=random.randrange(20)
    y=random.randrange(20)
    xy=[x,y]
    return xy
#部品リストとピンを照合し、部品の座標を書き付ける処理
outputFile=open("sample.txt","w")
for cmpName in cmpNameList:
    tempX=[]
    tempY=[]
    for PinName in PinNameList:
        tempPin=[]
        
        if cmpName in PinName:
            tempPin.append(PinName)
            #ピン名の登録
            tempXY=randomList(PinName)
            tempX.append(tempXY[0])
            tempY.append(tempXY[1])
    xMAX=max(tempX)
    xMIN=min(tempX)
    yMAX=max(tempY)
    yMIN=min(tempY)
    line=cmpName+","+str(xMAX)+","+str(xMIN)+","+str(yMAX)+","+str(yMIN)
    print(line)
    outputFile.writelines(line)
outputFile.close()
        
#create rectangle
#座標取得
#一つのコンポーネントからピンを抽出し、それぞれのピンの座標をリストに収める
for pinName in c16_pin:
    print(pinName)
    tempX=pinName[0]
    tempY=pinName[1]
    c16_X.append(tempX-2)
    c16_X.append(tempX+2)
    c16_Y.append(tempY-2)
    c16_Y.append(tempY+2)

#出来上がったリストから最小最大値を取得
c16_xMax=max(c16_X)
c16_xMin=min(c16_X)
c16_yMax=max(c16_Y)
c16_yMin=min(c16_Y)

#出来上がったrectangleの中点に線引き
StartCenterX=(c16_xMax+c16_xMin)/2
StartCenterY=c16_yMax
EndCenterX=StartCenterX
EndCenterY=c16_yMin

print("start:["+str(StartCenterX)+","+str(StartCenterY)+"]")
print("end:["+str(EndCenterX)+","+str(EndCenterY)+"]")