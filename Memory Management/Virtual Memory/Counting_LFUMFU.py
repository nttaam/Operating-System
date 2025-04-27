def get_input():
    print("Nhap so frame: ")
    frames = int(input())

    print("Nhap cac page truy cap:")
    pages = [int(x) for x in input().split()]

    return frames, pages

def lfu(frames, pages):
    lst_frames = []
    page_faults = 0
    frequency = {}

    for page in pages:
        frequency[page] = frequency.get(page, 0) + 1
        if page not in lst_frames:
            page_faults += 1
            if len(lst_frames) >= frames:
                min_freq = min(frequency[f] for f in lst_frames)
                lfu_pages = [f for f in lst_frames if frequency[f] == min_freq]
                lst_frames.remove(lfu_pages[0])
            lst_frames.append(page)
        print(f"Page {page}: Frames = {lst_frames}, Page Fault = {page_faults}")

    return page_faults

def main():
    frames, pages = get_input()
    print(f"\nFrame: {frames}")
    print(f"Pages: {pages}")

    faults = lfu(frames, pages)
    print(f"\nTổng số page fault: {faults}")

main()
