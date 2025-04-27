def get_input():
    print("Nhap kick thuoc cac khoi bo nho")
    blocks=input().split()
    blocks = [int(x) for x in blocks]

    print("Nhap kick thuoc cac tien trinh")
    processes = input().split()
    processes = [int(x) for x in processes]

    return blocks, processes

def first_fit(blocks, process):
    for i in range(len(blocks)):
        if blocks[i] >= process:
            info = f"khoi {i+1}, kick thuoc : {blocks[i]}"
            blocks[i] -= process
            return blocks, info
    return blocks, None
def show(blocks, info):
    if info:
        print(f"Da cap phat vao {info}")
    else:
        print(f"Khong tim duoc khoi nao")
    print("cac khoi bo nho hien tai: ",blocks)

def main():
    blocks = [2,3]
    processes = [5,1,2]
    print("Cac khoi bo nho ban dau:", blocks)
    print("Cac tien trinh ban dau:", processes)

    for process in processes:
        blocks, info = first_fit(blocks, process)
        show(blocks,info)

main()