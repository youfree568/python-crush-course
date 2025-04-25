name1 = ' Nick '
name2 = '\tNick'
name3 = '\nNick'
name4 = '\n\tNick '
print(f'Варіант 1 з пробілами _{name1}_.')
print(f'Варіант 1 без пробілів зліва _{name1.lstrip()}_.')
print(f'Варіант 1 без пробілів зправа_{name1.rstrip()}_.')
print(f'Варіант 2 з пробілами _{name2}_.')
print(f'Варіант 2 без пробілів _{name2.strip()}_.')
print(f'Варіант 3 з пробілами _{name3}_.')
print(f'Варіант 3 без пробілів зправа _{name3.rstrip()}_.')
print(f'Варіант 3 без пробілів зліва _{name3.lstrip()}_.')
print(f'Варіант 4 з пробілами _{name4}_.')
print(f'Варіант 4 без пробілів зправа _{name4.rstrip()}_.')
print(f'Варіант 4 без пробілів _{name4.rstrip().lstrip()}_.')
