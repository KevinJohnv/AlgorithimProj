import time

def seperate(data, frontOfData, tail, drawData, sleepTime):
    edge = frontOfData
    pivot = data[tail]
    drawData(data, getColorArray(len(data), frontOfData, tail, edge, edge))
    time.sleep(sleepTime)

    
    
    for j in range(frontOfData, tail):
        if data[j] < pivot:
            drawData(data, getColorArray(len(data), frontOfData, tail, edge, j, True))
            time.sleep(sleepTime)

            data[edge], data[j] = data[j], data[edge]
            edge += 1

        drawData(data, getColorArray(len(data), frontOfData, tail, edge, j))
        time.sleep(sleepTime)


    #swap pivot with edge value
    drawData(data, getColorArray(len(data), frontOfData, tail, edge, tail, True))
    time.sleep(sleepTime)

    data[edge], data[tail] = data[tail], data[edge]
    
    return edge

def quick_sort(data, frontOfData, tail, drawData, sleepTime):
    if frontOfData < tail:
        seperateIdx = seperate(data, frontOfData, tail, drawData, sleepTime)

        #LEFT seperate
        quick_sort(data, frontOfData, seperateIdx-1, drawData, sleepTime)

        #RIGHT seperate
        quick_sort(data, seperateIdx+1, tail, drawData, sleepTime)


def getColorArray(dataLen, frontOfData, tail, edge, currIdx, isSwaping = False):
    colorArray = []
    for i in range(dataLen):
        #base coloring
        if i >= frontOfData and i <= tail:
            colorArray.append('purple')
        else:
            colorArray.append('orange')

        if i == tail:
            colorArray[i] = 'blue'
        elif i == edge:
            colorArray[i] = 'red'
        elif i == currIdx:
            colorArray[i] = 'yellow'

        if isSwaping:
            if i == edge or i == currIdx:
                colorArray[i] = 'green'

    return colorArray