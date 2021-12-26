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
    print("*"*120)
    print(f"\nInput number of data: {result['input']}")
    print(f"\nNumber set: {result['bom']}, Total {result['set_element']} elements exist.")
    print("\n")
    print("*"*120)
    print("\n"*5)

    
if __name__ == "__main__" :

    bom = get_number()
    data_number = len(bom)
    bom_set = sorted(set(bom))
    set_number = len(bom_set)

    result = {"input":data_number, "bom":bom_set, "set_element":set_number}
    print_out(result)
    




        
