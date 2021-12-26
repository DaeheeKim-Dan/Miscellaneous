'''
Solidworks slddrw 작업시
풍선번호 배열 이후, BOM 테이블 조작할 때, 숨겨야할 번호를 빨리 파악하기 위해
나열된 풍선번호를 모두 입력하면,
정렬된 set를 반환시켜, 나머지 숫자들만 숨겨 작업을 빠르게 진행하도록 하는 프로그램
Programmed by Dan Kim @2021-12-26
'''


def get_number():
    i = 1
    bom = []
    while i:
        part_number = input("Part Number?: ")
        if part_number == '0' or part_number == "":
            i = False        
        else:
            bom.append(int(part_number))
    return bom


def print_out(result):
    print("-"*50)
    print(f"\nInput number of data: {result['input']}")
    print(f"\nNumber set: {result['bom']}, Total {result['set_element']} elements exist.")

    
if __name__ == "__main__"    :

    bom = get_number()
    data_number = len(bom)
    bom_set = sorted(set(bom))
    set_number = len(bom_set)

    result = {"input":data_number, "bom":bom_set, "set_element":set_number}
    print_out(result)
    


        
