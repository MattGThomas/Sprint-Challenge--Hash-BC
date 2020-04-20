#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length
    """
    function takes Ticket class, and unscrambles trip based on 
    where the source and destination 'NONE' are both located
    """
    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)

    # change route to empty array to append destination
    route = []

    destination = hash_table_retrieve(hashtable, 'NONE')

    while destination != 'NONE':
        # route.hash_table_insert(destination)
        route.append(destination)
        # flights.append(destination)
        destination = hash_table_retrieve(hashtable, destination)
    # return flights
    return route

    # destination = hash_table_retrieve(hashtable, 'NONE')
    # while destination != 'NONE':
    #     route.append(destination)
    #     destination = hash_table_retrieve(hashtable, destination)
    # return route

    # pass
