def main():

    list = ['task one', 'task two', 'task three']
    print_tasks(list)
    newtask = input('Adding Task: ')
    add_task(list, newtask)
    print_tasks(list)

def add_task(list, task):
    list.append(task)
    return list

def print_tasks(list):
    count = 1
    for i in list:
        print(f'{count}. {i}')
        count += 1



main()
