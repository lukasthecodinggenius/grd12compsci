def main():
    unsort_list = ['max', 'adam', 'zak', 'lukas', 'prabhnoor', 'arjun', 'naveed', 'alex', 'timmy', 'mark']
    sortlist = sort_names(unsort_list)
    print(f'sorted list: {sortlist}')
    search = input('check for name: ')
    binary_search(search, sort_names(unsort_list))

def sort_names(unsort_list):

    for i in range(len(unsort_list) - 1):
        for j in range(i + 1, len(unsort_list)):
            if unsort_list[i] > unsort_list[j]:
                temp = unsort_list[i]
                unsort_list[i] = unsort_list[j]
                unsort_list[j] = temp

    return unsort_list
def binary_search(search,list):

    count = -1
    if search in list:
        for i in list:
            count += 1
            if i == search:
                print(f'name is at index {count}')

main()






