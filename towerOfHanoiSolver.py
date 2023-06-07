TOTAL_DISKS = 6
TOWERS = {"A": list(reversed(range(1, TOTAL_DISKS + 1))), "B": [], "C": []}


def print_disk(disk_num: int):
    empty_space = " " * (TOTAL_DISKS - disk_num)
    if disk_num == 0:
        print(f"{empty_space}||{empty_space}", end="")

    else:

        disk_space = "@" * disk_num
        disk_num_label = str(disk_num).rjust(2, "_")
        print(f"{empty_space + disk_space + disk_num_label + disk_space + empty_space}", end="")


def print_towers():
    # Вывод на экран всех трех башен
    for level in range(TOTAL_DISKS, -1, -1):
        for tower in (TOWERS['A'], TOWERS['B'], TOWERS['C']):
            if level >= len(tower):
                print_disk(0)
            else:
                print_disk(tower[level])
        print()

    empty_space = " " * TOTAL_DISKS
    print(f"{empty_space} A{empty_space + empty_space} B{empty_space + empty_space} C")


def move_one_disk(start_tower: str, end_tower: str):
    disk = TOWERS[start_tower].pop()
    TOWERS[end_tower].append(disk)


def solve(number_of_disks: int, start_tower: str, end_tower: str, temp_tower: str):
    if number_of_disks == 1:
        # БАЗОВЫЙ СЛУЧАЙ
        move_one_disk(start_tower, end_tower)
        print_towers()
        return
    else:
        # РЕКУРСИВНЫЙ СЛУЧАЙ
        solve(number_of_disks - 1, start_tower, temp_tower, end_tower)
        move_one_disk(start_tower, end_tower)
        print_towers()
        solve(number_of_disks - 1, temp_tower, end_tower, start_tower)
        return


# print_towers()
solve(TOTAL_DISKS, 'A', 'B', 'C')