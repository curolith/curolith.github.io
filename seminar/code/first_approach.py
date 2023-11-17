import unittest


def increment(n_ary_counter: list, base: int):
    incremented = False
    index = len(n_ary_counter) - 1
    while not incremented:
        if n_ary_counter[index] == base - 1:
            index -= 1
            if index < 0:
                return
        else:
            n_ary_counter[index] += 1
            for i in range(index + 1, len(n_ary_counter)):
                n_ary_counter[i] = 0
            incremented = True
    return


def probability_for_item(item, box):
    return box.count(item) / len(box)


def first_approach(box: list, combination_length: int, collector=None):
    if collector is None:
        collector = []
    different_types = list(set(box))
    results = []
    n_ary_counter = [0] * combination_length
    base = len(different_types)
    while len(results) < (base ** combination_length):
        combination = [different_types[i] for i in n_ary_counter]
        combination_probability = 1
        for item in combination:
            combination_probability *= probability_for_item(item, box)
        item = [combination, combination_probability]
        collector.append(item)
        results.append(item)
        increment(n_ary_counter, base)
    return collector


class TestFirstApproach(unittest.TestCase):

    def test_count_adds_up_4(self):
        for i in range(1, 4):
            assert len(first_approach(['b', 'r', 'r', 't', 'k'], i)) == 4 ** i, "Number of combinations did not match " \
                                                                                "for length: " + str(i)

    def test_count_adds_up_7(self):
        for i in range(1, 4):
            assert len(first_approach(['b', 'r', 'r', 't', 'k', 'x', 'y', 'z'], i)) == 7 ** i, "Number of " \
                                                                                               "combinations did not " \
                                                                                               "match " \
                                                                                               "for length: " + str(i)

    def test_first_approach(self):
        print("testing first approach...\n")
        for line in first_approach(['b', 'r', 'r', 't', 'k'], 3):
            print(line)
