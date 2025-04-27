def get_input():
    print("Nhap so frame: ")
    frames = int(input())

    print("Nhap cac page truy cap")
    pages = [int(x) for x in input().split()]

    return frames, pages

def optimal(frames, pages):
    lst_frames = []
    page_faults = 0

    for i, page in enumerate(pages):
        if page not in lst_frames:
            page_faults += 1
            if len(lst_frames) >= frames:
                future_uses = {}
                for f in lst_frames:
                    future_uses[f] = float('inf')
                    for j in range(i+1, len(pages)):
                        if pages[j] == f:
                            future_uses[f] = j
                            break

                to_replace = max(future_uses, key=future_uses.get)
                lst_frames.remove(to_replace)
            lst_frames.append(page)
        print(f"Page {page}: Frames = {lst_frames}, Page Fault = {page_faults}")

    return page_faults

def main():
    frames, pages = get_input()
    print(f"\nFrame: {frames}")
    print(f"Pages: {pages}")

    total_faults = optimal(frames, pages)
    print(f"\nTotal Page Faults: {total_faults}")

main()
