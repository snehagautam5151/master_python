def tower_hanoi(disks, src, aux, target):
    if (disks == 1):
        print('Move disk 1 from rod{} to rod{}.'.format(src, target))
        return
    tower_hanoi(disks-1, src, aux, target)
    
    print('Move disk {} from rod {} to rod {}.'.format(src, target))
    tower_hanoi(disks-1, src, aux, target)
    
disks = int(input('Enter the number of disk:'))
tower_hanoi(disks,'A','B','C')
 
