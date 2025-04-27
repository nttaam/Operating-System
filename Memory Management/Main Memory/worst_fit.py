def get_input():
    print("Nhap kick thuoc cac khoi bo nho")
    blocks=input().split()
    blocks = [int(x) for x in blocks]

    print("Nhap kick thuoc cac tien trinh")
    processes = input().split()
    processes = [int(x) for x in processes]

    return blocks, processes

def worst_fit(blocks, process):
    largest = -1
    index = -1

    for i in range(len(blocks)):
        if blocks[i] >= process and blocks[i] > largest:
            largest = blocks[i]
            index = i

    if index != -1:
        info = f"Khoi {index +1}, kick thuoc: {blocks[index]}"
        blocks[index] -= process
        return blocks, info
    
    return blocks, None
def show(blocks, info):
    if info:
        print(f"Da cap phat vao {info}")
    else:
        print(f"Khong tim duoc khoi nao")
    print("cac khoi bo nho hien tai: ",blocks)

def main():
    blocks = [1,4,2]
    processes = [1,2,2]
    print("Cac khoi bo nho ban dau:", blocks)
    print("Cac tien trinh ban dau:", processes)

    for process in processes:
        blocks, info = worst_fit(blocks, process)
        show(blocks,info)

main()