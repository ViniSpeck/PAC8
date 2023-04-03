import pytest, requests
from merge_sort import MergeSort

@pytest.fixture
def sorter():
    return MergeSort()

def test_sort_empty_list(sorter):
    arr = []
    assert sorter.sort(arr) == []

def test_sort_single_element_list(sorter):
    arr = [5]
    assert sorter.sort(arr) == [5]

def test_sort_sorted_list(sorter):
    arr = [1, 2, 3, 4, 5]
    assert sorter.sort(arr) == [1, 2, 3, 4, 5]

def test_sort_reverse_sorted_list(sorter):
    arr = [5, 4, 3, 2, 1]
    assert sorter.sort(arr) == [1, 2, 3, 4, 5]

def test_sort_random_list(sorter):
    arr = [64, -34, 25, 12, -22, 11, 90]
    assert sorter.sort(arr) == [-34, -22, 11, 12, 25, 64, 90]

# def test_sort_endpoint():
#     unsorted_arr = [3, 1, 4, 2, 5]
#     payload = {'arr': unsorted_arr}

#     response = requests.post('http://localhost:5000/sort', json=payload)
#     assert response.status_code == 200

#     expected_result = [1, 2, 3, 4, 5]
#     assert response.json()['sorted_arr'] == expected_result