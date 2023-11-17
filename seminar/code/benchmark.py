import glob
import os
import re
import timeit

# READ ME




def bench(b, t):
    result = []
    result.append(timeit.timeit(f"""import first_approach_revisited as fa
size = {t}
box = {str(b)}
fa.first_approach(box, size)
    """, number=1))
    result.append(timeit.timeit(f"""import second_approach_revisited as sa
size = {t}
box = {str(b)}
sa.second_approach(box, size)
    """, number=1))
    return result


def dump(tracker):
    print("dumping...")
    files = glob.glob(os.path.join('./benchmark_dumps', '*'))
    current = 0
    if len(files) > 0:
        numbers = [int(re.search(r'dump_(\d+)', file).group(1)) for file in files if re.search(r'dump_(\d+)', file)]
        current = max(numbers) + 1
    with open(f'./benchmark_dumps/dump_{current}.csv', 'w') as dump:
        for line in tracker:
            content = str(line[0])
            content += ","
            content += str(line[1])
            content += "\n"
            dump.write(content)


def do_benchs():
    tracker = []
    alph = list("abcdeflmnopqaaaabbbbccccddddeeeehhhhiiiijjjjkkkk")
    for i in range(1,7):
        sub = alph
        print(i, " : ")
        current = bench(sub, i)
        tracker.append(current)
        print(current)
        files = glob.glob(os.path.join('./benchmark_dumps', '*'))
    return tracker


print("starting benchmark...")
dump(do_benchs())
