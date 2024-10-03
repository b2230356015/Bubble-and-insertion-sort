import sys

# An insertion sort function so that I can check later if list is sorted
def basic_sort(list_so):
    for i in range(1, len(list_so)):
        place = i
        while place > 0:
            if list_so[place] < list_so[place - 1]:
                list_so[place], list_so[place - 1] = list_so[place - 1], list_so[place]
            place -= 1
    return list_so

# Bubble sort function that also writes on output text
def bubble(list_bub, file, count, sorted_two):
    for i in range(len(list_bub) - 1):
        swap = False
        for y in range(0, len(list_bub) - i - 1):
            if list_bub[y] > list_bub[y + 1]:
                list_bub[y], list_bub[y + 1] = list_bub[y + 1], list_bub[y]
                swap = True
        new_list = []
        for y in range(len(list_bub)):
            new_list.append(str(list_bub[y]))
        kinda_sorted = " ".join(new_list)
        if swap:
            if list_bub != sorted_two:
                file.write("Pass {}: {}\n".format(count, kinda_sorted))
            else:
                file.write("Pass {}: {}".format(count, kinda_sorted))
                break
        count += 1

# Insertion function that also writes on output text
def insertion(list_ins, file, count, sorted_one):
    for i in range(1, len(list_ins)):
        place = i
        while place > 0:
            if list_ins[place] < list_ins[place - 1]:
                list_ins[place], list_ins[place - 1] = list_ins[place - 1], list_ins[place]
            place -= 1
        new_list = []
        for y in range(len(list_ins)):
            new_list.append(str(list_ins[y]))
        kinda_sorted = " ".join(new_list)
        if list_ins != sorted_one:
            file.write("Pass {}: {}\n".format(count, kinda_sorted))
        else:
            file.write("Pass {}: {}".format(count, kinda_sorted))
            break
        count += 1


def main():
    inp_file = open(sys.argv[1], 'r')
    b_out_file = open(sys.argv[2], 'w')
    i_out_file = open(sys.argv[3], 'w')
    string_file = inp_file.read()
    list_file = string_file.split(" ")
    # Checking if input has more than 2 elements
    # if not, ends the main function here because its creating more problems otherwise
    if len(list_file) < 2:
        b_out_file.write("Already sorted!")
        i_out_file.write("Already sorted!")
        return
    for i in range(len(list_file)):
        list_file[i] = int(list_file[i])
    list_file1 = list_file.copy()
    list_file2 = list_file.copy()
    sorted_list = basic_sort(list_file2)
    # Checks if the list is already sorted or not and if it's not it runs the functions
    if sorted_list != list_file:
        insertion(list_file1, i_out_file, 1, sorted_list)
        bubble(list_file, b_out_file, 1, sorted_list)
    else:
        b_out_file.write("Already sorted!")
        i_out_file.write("Already sorted!")


if __name__ == "__main__":
    main()
