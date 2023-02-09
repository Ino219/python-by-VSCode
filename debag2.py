#debag2

c16_X=[]
c16_Y=[]

c16_1_loc=[3,4]
c16_2_loc=[8,4]
c16_pin=[c16_1_loc,c16_2_loc]

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