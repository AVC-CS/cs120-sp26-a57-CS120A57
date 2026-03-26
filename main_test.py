import pytest
import re

def regex_test(expected, content):
    pos = 0
    for token in expected:
        res = re.search(token, content[pos:])
        if res is None:
            assert False, f'Expect: {token}'
        pos += res.start() + 1

@pytest.mark.T1
def test_main_1():
    # data1: n1=5, n2=8, N=3 -> 5 8 13
    content = open('result1.txt').read()
    print(content)
    regex_test([r'\b5\b', r'\b8\b', r'\b13\b'], content)

@pytest.mark.T2
def test_main_2():
    # data2: n1=5, n2=10, N=5 -> 5 10 15 25 40
    content = open('result2.txt').read()
    print(content)
    regex_test([r'\b5\b', r'\b10\b', r'\b15\b', r'\b25\b', r'\b40\b'], content)

@pytest.mark.T3
def test_main_3():
    # data3: n1=1, n2=1, N=7 -> 1 1 2 3 5 8 13
    content = open('result3.txt').read()
    print(content)
    regex_test([r'\b1\b', r'\b1\b', r'\b2\b', r'\b3\b', r'\b5\b', r'\b8\b', r'\b13\b'], content)

@pytest.mark.T4
def test_main_4():
    # data4: n1=0, n2=5, N=6 -> 0 5 5 10 15 25
    content = open('result4.txt').read()
    print(content)
    regex_test([r'\b0\b', r'\b5\b', r'\b5\b', r'\b10\b', r'\b15\b', r'\b25\b'], content)
