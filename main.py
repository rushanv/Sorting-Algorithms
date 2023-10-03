import time
import pygame
import random
pygame.init()


def updateDisplay(heightsArray, left, right, cmd):
    running = True
    screen.fill((255, 255, 255))
    pygame.display.set_caption("hello chatters")
    pygame.font.init()
    fontVar = pygame.font.SysFont('Comic Sans MS', 30)
    comparisonString = "Comparisons: " + str(comparison)
    fontObj = fontVar.render(comparisonString, False, (0, 0, 0), (255, 255, 255))
    limit = 0.8 * sizeY
    width = int(0.75 * sizeX / len(heightsArray))
    xCoordL = (sizeX-len(heightsArray)*width)/2
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for i in range(len(heightsArray)):
            drawHeight = (heightsArray[i] / max(heightsArray)) * limit
            color = (heightsArray[i] / max(heightsArray)) * 100
            pygame.draw.rect(screen, (255, color, 80), (xCoordL, sizeY-drawHeight, width, sizeY))
            xCoordL += width

        pygame.draw.rect(screen, (0, 0, 0), (0, 0, sizeX, sizeY), 5)
        screen.blit(fontObj, (50, 50))
        pygame.display.flip()
        delay = 1/number
        match cmd:
            case 'm':
                delay = (right-left)/(right+left)
        time.sleep(delay)
        return


def bubbleSort(heightArray, nrPersons):
    global comparison
    while True:
        completeTest = 1
        for i in range(1, nrPersons, 1):
            if heightArray[i-1] > heightArray[i]:
                temp = heightArray[i]
                heightArray[i] = heightArray[i-1]
                heightArray[i-1] = temp
                completeTest = 0
                print("after swapping:", heightArray)
                comparison += 1
                updateDisplay(heightArray, 0, nrPersons-1, 'b')
        if completeTest == 1:
            return


def insertionSort(heightArray, nrPersons):
    global comparison
    for i in range(1, nrPersons, 1):
        if heightArray[i-1] > heightArray[i]:
            temp = heightArray[i]
            heightArray[i] = heightArray[i-1]
            heightArray[i-1] = temp
            print("after swapping:", heightArray)
            comparison += 1
            updateDisplay(heightArray, 0, nrPersons-1, 's')
            for j in range(i-1, 0, -1):
                if heightArray[j-1] > heightArray[j]:
                    temp = heightArray[j]
                    heightArray[j] = heightArray[j-1]
                    heightArray[j-1] = temp
                    print("after swapping:", heightArray)
                    comparison += 1
                    updateDisplay(heightArray, 0, nrPersons-1, 's')


comparison = 0


def merge(heightArray, left, right, mid):
    global comparison
    interim = list(range(0, right-left+1, 1))
    rhs = mid+1
    lhs = left
    for i in range(0, right-left+1, 1):
        if rhs > right or (lhs <= mid and heightArray[lhs] < heightArray[rhs]):
            interim[i] = heightArray[lhs]
            lhs += 1
        elif lhs > mid or (rhs <= right and heightArray[lhs] > heightArray[rhs]):
            interim[i] = heightArray[rhs]
            rhs += 1
        comparison += 1
    for j in range(0, right-left+1, 1):
        heightArray[left+j] = interim[j]
    updateDisplay(heightArray, left, right, 'm')


def mergeSort(heightArray, left, right):
    left = int(left)
    right = int(right)
    mid = int((right+left)/2)
    if right > left:
        print("need to sort     ", heightArray[left:right+1])

        mergeSort(heightArray, left, mid)
        print("after sorting lhs", heightArray[left:mid+1])

        mergeSort(heightArray, mid+1, right)
        print("after sorting rhs", heightArray[mid+1:right+1])

        merge(heightArray, left, right, mid)
        print("after merging    ", heightArray[left:right+1])


def main():
    global sizeX, sizeY, screen, comparison
    sizeX = 1920
    sizeY = 1080

    print("--Command Help--")
    print("\ti - initializes an array of specified size")
    print("\tp - prints out the array")
    print("\th - shows the minimum, maximum and range of the array")
    print("\tr - lets you replace any value in the array")
    print("\tf - shuffles the array")
    print("\tb - bubble sort")
    print("\ts - insertion sort")
    print("\tm - merge sort")
    print("\tx - bogosort !")
    print("\tq - quit")

    while True:
        command = input("Command? ")
        match command:
            case 'i':
                global number, heights
                number = int(input("Number of people? "))
                heights = list(range(number, 0, -1))
            case "q":
                break
            case 'x':
                comparison = 0
                screen = pygame.display.set_mode([sizeX, sizeY])
                while True:
                    random.shuffle(heights)
                    updateDisplay(heights, 0, number-1, 'x')
                    comparison += 1
                    if heights == sorted(heights):
                        break
                comparison = 0
                time.sleep(2)
                pygame.quit()
            case 'p':
                try:
                    print(heights)
                except:
                    print("Heights has not been initialized.")
                    continue
            case 'h':
                print("Min:", min(heights))
                print("Max:", max(heights))
                print("Range:", max(heights)-min(heights))
            case 'r':
                index = int(input("Index? "))
                heightReplacement = int(input("Height? "))
                heights[index] = heightReplacement
            case 'f':
                random.shuffle(heights)
            case 'b':
                comparison = 0
                screen = pygame.display.set_mode([sizeX, sizeY])
                bubbleSort(heights, number)
                time.sleep(2)
                pygame.quit()
            case 's':
                comparison = 0
                screen = pygame.display.set_mode([sizeX, sizeY])
                insertionSort(heights, number)
                time.sleep(2)
                pygame.quit()
            case 'm':
                comparison = 0
                screen = pygame.display.set_mode([sizeX, sizeY])
                mergeSort(heights, 0, number-1)
                time.sleep(2)
                pygame.quit()
            case _:
                print("Invalid command.")
                continue
    pygame.quit()


main()
