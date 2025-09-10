def sort(width, height, length, mass):
    IsBulky = False
    IsHeavy = False
    
    if width >= 150 or height >= 150 or length >= 150:
        IsBulky = True     
    else:
        volume = width * height * length
        if volume >= 1000000 :
            IsBulky = True
    if mass >= 20:
        IsHeavy = True 

    answer = 'STANDARD'
    if  IsHeavy or IsBulky:
        answer = 'SPECIAL'
        if IsBulky and IsHeavy:
            answer = 'REJECTED'

    return answer

if __name__ == '__main__':
    
    test1 = sort(100,30,90,19)
    print('case of a non bulky, non heavy package')
    print('sort(100,30,90,19) --> LABEL:',test1)
    test2_1 = sort(100,130,90,19)
    print('case of a bulky but non heavy package')
    print('sort(100,130,90,19) --> LABEL:',test2_1)
    test2_2 = sort(100,30,90,20)
    print('case of a non bulky but heavy package')
    print('sort(100,30,90,20) --> LABEL:',test2_2)
    test3 = sort(100,130,90,20)
    print('case of a bulky and heavy package')
    print('sort(100,130,90,20) --> LABEL:',test3)