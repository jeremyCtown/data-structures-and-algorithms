import pytest
# import shift-array
from shift_array import ShiftArray as SA

@pytest.fixture
def empty_sa():
    return SA(test_list, test_num)


test_list = [1, 2, 4, 5, 6]
test_num = 3


def test_sa_counter(empty_sa):
    """
    function that tests to see if counter adds up based on list length
    """

    assert empty_sa.counter == 0
    # old_list = [1, 2, 3]
    # assert test_increment_counter == 3


def test_sa_new_list_empty(empty_sa):
    """
    function to ensure empty list to populate is available
    """
    assert empty_sa.new_list == ['']


def test_increment_counter(empty_sa):
    """
    function to ensure counter is increasing
    """
    assert empty_sa.increment_counter.counter == 5


# def test_if_add_first_half():
#     """
#     function that checks to see if the first half of the old list is added
#     to the new list
#     """
#     assert shift-array.new_list/2



# def test_if_not_add_first_half():
#     """
#     function that purposely doesn't add first half
#     """


# def test_elif_add_middle_index():
#     """
#     function that checks to see if middle index has element added in
#     """


# def test_elif_not_add_middle_index():
#     """
#     function that checks if it doesn't have middle index in place
#     """


# def test_else_add_back_half():
#     """
#     function that checks to see if back half is added to list
#     """


# def test_else_not_add_back_half():
#     """
#     function that checks to see if back half isn't added to list
#     """

# def test_length_of_final_list():
#     """
#     function that checks final list length
#     """

