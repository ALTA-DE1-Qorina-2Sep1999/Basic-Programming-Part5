def muncul_sekali(angka):
    number = list(str(angka))
    resultTemp, result = [], []
    
    frequency = {}
    for item in number:
        if item not in frequency:
            frequency[item] = 1
        else:
            frequency[item] += 1
    
    for index in frequency:
        if frequency[index] == 1:
            temp = int(index)
            resultTemp.append(temp)
    
    for i in range(len(number)):
        for j in range(len(resultTemp)):
            if number[i] == str(resultTemp[j]):
                result.append(resultTemp[j])
                break
    
    return result

if __name__ == '__main__':
    print(muncul_sekali("1234123")) # [4]
    print(muncul_sekali("76523752")) # [6, 3]
    print(muncul_sekali("12345")) # [1, 2, 3, 4, 5]
    print(muncul_sekali("1122334455")) # []
    print(muncul_sekali("0872504")) # [8, 7, 2, 5, 4]