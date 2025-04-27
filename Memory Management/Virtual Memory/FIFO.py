def get_input():
    print("Nhap so frame: ")
    frames = int(input())

    print("Nhap cac page truy cap:")
    pages = [int(x) for x in input().split()]

    return frames, pages

def fifo(frames, pages):
    lst_frames = []
    page_faults = 0

    for page in pages:
        if page not in lst_frames:
            page_faults += 1
            if len(lst_frames) >= frames:
                lst_frames.pop(0)
            lst_frames.append(page)
        print(f"Page {page}: Frames = {lst_frames}, Page Fault = {page_faults}")

    return page_faults

def main():
    frames, pages = get_input()
    print(f"\nFrame: {frames}")
    print(f"Pages: {pages}")

    faults = fifo(frames, pages)
    print(f"\nTổng số page fault: {faults}")

main()
