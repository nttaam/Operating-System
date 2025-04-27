def get_input():
    print("Nhap kick thuoc cac khoi bo nho")
    blocks=input().split()
    blocks = [int(x) for x in blocks]

    print("Nhap kick thuoc cac tien trinh")
    processes = input().split()
    processes = [int(x) for x in processes]

    return blocks, processes

def best_fit(blocks, process):
    smallest = 9999999
    index = -1

    for i in range(len(blocks)):
        if blocks[i] >= process and blocks[i] < smallest:
            smallest = blocks[i]
            index = i

    if index != -1:
        info = f"Khoi {index +1}, Kich thuoc: {blocks[index]}"
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
    blocks = [3,2,1]
    processes = [4,1,1]
    print("Cac khoi bo nho ban dau:", blocks)
    print("Cac tien trinh ban dau:", processes)
    for process in processes:
        blocks, info = best_fit(blocks, process)
        show(blocks,info)

main()