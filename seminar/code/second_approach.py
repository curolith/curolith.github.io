import unittest


def probability_for_item(item, box):
    return box.count(item) / len(box)


def second_approach(box, combination_length, probability=1, combination=None, collector=None):
    toplevel = False
    if collector is None:
        collector = []
        toplevel = True
    if combination is None:
        combination = []
    if len(combination) == combination_length:
        collector.append([list(combination), probability])
        return

    for x in set(box):
        subcombination = []
        subcombination.extend(combination)
        subcombination.append(x)
        second_approach(box, combination_length, probability * probability_for_item(x, box), subcombination, collector)
    if toplevel:
        return collector


class TestSecondApproach(unittest.TestCase):

    def test_count_adds_up_4(self):
        for i in range(1, 4):
            assert len(second_approach(['b', 'r', 'r', 't', 'k'], i)) == 4 ** i, "Number of combinations did not match " \
                                                                                 "for length: " + str(i)

    def test_count_adds_up_7(self):
        for i in range(1, 4):
            assert len(second_approach(['b', 'r', 'r', 't', 'k', 'x', 'y', 'z'], i)) == 7 ** i, "Number of " \
                                                                                                "combinations did not " \
                                                                                                "match " \
                                                                                                "for length: " + str(i)

    def test_second_approach(self):
        print("testing second approach...\n")
        for line in second_approach(['b', 'r', 'r', 't', 'k'], 3):
            print(line)
