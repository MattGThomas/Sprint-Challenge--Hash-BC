#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        # hash_table_remove,
                        hash_table_retrieve,
                        # hash_table_resize)
                        )


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    function finds two items whose sum equals the weight limit
    returns answer as a tuple ie (zero, one)

    """

    for i in range(0, len(weights)):
        # checks the value of limit - weights
        value = hash_table_retrieve(ht, limit - weights[i])
        if value != None:
            return (i, value)
        else:
            hash_table_insert(ht, weights[i], i)

    # for i in range(length):
    #     hash_table_insert(ht, weights[i], i)
    # for i in range(length):
    #     checked_weight = hash_table_retrieve(ht, (limit-weights[i]))
    #     if checked_weight:
    #         if checked_weight > 1:
    #             return [checked_weight, i]
    #         else:
    #             return [i, checked_weight]

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
