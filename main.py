# Import the necessary libraries

import numpy as np
import cv2
from PIL import Image
from numpy import asarray

def secretMessageInBinary():
    a_string = input("Enter a secret message: ")
    ASCII = [ord(character) for character in a_string]
    print()
    print(f'Secret message -> ASCII Values:- \n{ASCII}')
    ASCII.reverse()
    i = 0
    num = []
    for i in ASCII:
        binary = []
        n = i
        while n > 0:
            binary.append(n % 2)
            n = n // 2
        while len(binary) < 8:
            binary.append(0)
        num = num + binary
    num.reverse()
    return num

def binaryToSecretMessage(binMsg):
    print()
    print(f'Decrypted Binary Message:- \n{binMsg}')
    asciiMsg = []
    print()

    start = 0
    end = 8
    while start <= len(binMsg) and end <= len(binMsg):
        binaryMsg = []
        for i in range(start,end):
            binaryMsg.append(binMsg[i])
        binaryMsg.reverse()
        asciiMsg.append(binaryToDecimal(binaryMsg))
        start = start + 8
        end = end + 8

    print(f'Decrypted Binary Message -> ASCII Values:- \n{asciiMsg}')

    message = ''

    for i in range(len(asciiMsg)):
        message = message + chr(asciiMsg[i])

    print()
    print(f'ASCII Values -> Retrieved Secret Message:- \n{message}')

def binaryToDecimal(binValue):
    decValue = 0
    base = 1
    #print(f'Length of Binary list: {len(binValue)}')
    for i in range(len(binValue)):
        decValue += binValue[i] * base
        base = base * 2
    return decValue

def matrixEncryptionOperation(matrix, num, ctr):

    R = 3
    C = 3

    seedPixel = matrix[int(R / 2)][int(C / 2)]

    print()
    print(f'Matrix {ctr+1}')
    print()
    print('Original Matrix')
    print(matrix)
    print()

    if ctr<=len(num):
        if seedPixel % 2 == 0:
            print('The encryption will take place in the bottommost row of the matrix')
            i = 2
            j = 0
            diff1 = abs(matrix[i][j] - matrix[i][j + 1])
            print('Diff1 ', diff1)
            diff2 = abs(matrix[i][j + 1] - matrix[i][j + 2])
            print('Diff2 ', diff2)
            mainDiff = abs(diff1 - diff2)
            print('Diff1 - Diff2 = ', mainDiff)

            if ((mainDiff % 2 == 0) and (num[ctr] == 1)) or ((mainDiff % 2 == 1) and (num[ctr] == 0)):
                matrix[R - 1][C - 1] = matrix[R - 1][C - 1] + 1

        elif seedPixel % 2 == 1:
            print('The encryption will take place in the topmost row of the matrix')
            i = 0
            j = 0
            diff1 = abs(matrix[i][j] - matrix[i][j + 1])
            print('Diff1 ', diff1)
            diff2 = abs(matrix[i][j + 1] - matrix[i][j + 2])
            print('Diff2 ', diff2)
            mainDiff = abs(diff1 - diff2)
            print('Diff1 - Diff2 = ', mainDiff)

            if ((mainDiff % 2 == 0) and (num[ctr] == 1)) or ((mainDiff % 2 == 1) and (num[ctr] == 0)):
                matrix[0][C - 1] = matrix[0][C - 1] + 1

    print()

    print('Modified Matrix')
    print(matrix)

def matrixDecryptionOperation(matrix, ctr):
    R = 3
    C = 3

    seedPixel = matrix[int(R / 2)][int(C / 2)]
    print()
    print(f'Matrix {ctr+1}')
    print()
    print(matrix)
    print()
    if seedPixel % 2 == 0:
        print('The decryption will take place from the bottommost row of the matrix')
        i = 2
        j = 0
        diff1 = abs(matrix[i][j] - matrix[i][j + 1])
        print('Diff1 ', diff1)
        diff2 = abs(matrix[i][j + 1] - matrix[i][j + 2])
        print('Diff2 ', diff2)
        mainDiff = abs(diff1 - diff2)
        print('Diff1 - Diff2 = ', mainDiff)

        print()
        if mainDiff % 2 == 0:
            bit = 0
            return bit
        elif mainDiff % 2 == 1:
            bit = 1
            return bit

    elif seedPixel % 2 == 1:
        print('The decryption will take place from the topmost row of the matrix')
        i = 0
        j = 0
        diff1 = abs(matrix[i][j] - matrix[i][j + 1])
        print('Diff1 ', diff1)
        diff2 = abs(matrix[i][j + 1] - matrix[i][j + 2])
        print('Diff2 ', diff2)
        mainDiff = abs(diff1 - diff2)
        print('Diff1 - Diff2 = ', mainDiff)

        print()
        if mainDiff % 2 == 0:
            bit = 0
            return bit
        elif mainDiff % 2 == 1:
            bit = 1
            return bit

def main():
    print()
    num = secretMessageInBinary()

    print()
    print(f'ASCII Values -> Binary Message:- \n{num}')

    print()
    print(f'Length of secret message in binary form: {len(num)}')
    stegoKey = len(num)

    print()
    imageFileName = input("Enter the image name with absolute path: ")
    img1 = cv2.imread(imageFileName)
    numpydata = asarray(img1)
    cv2.imshow('Original Cover Image',img1)

    print()
    h, w, _ = img1.shape
    print('Width of Image:  ', w)
    print('Height of Image: ', h)

    count = 0

    print()
    print()
    print('--MATRIX ENCRYPTION--')
    for i in range(0, stegoKey):
        matrixEncryptionOperation(numpydata[i][0:3], num, count)
        count = count + 1

    image = Image.fromarray(numpydata, 'RGB')
    image.save('StegoImage.jpg')

    img2 = np.array(image)
    numpydata1 = asarray(img2)
    cv2.imshow('Stego Image',img2)

    count1 = 0
    binMsg = []

    print()
    print()
    print('--MATRIX DECRYPTION--')
    for i in range(0, stegoKey):
        binMsg.append(matrixDecryptionOperation(numpydata1[i][0:3], count1))
        count1 = count1 + 1

    binaryToSecretMessage(binMsg)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()