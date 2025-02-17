"""
-------------------------------------------------------
Linked version of the Queue ADT.
-------------------------------------------------------

-------------------------------------------------------
"""
# pylint: disable=W0212
# pylint: disable=E2515
# pylint: disable=E0303
# pylint: disable=W0613
# pylint: disable=E1128

# Imports
from copy import deepcopy

from Priority_Queue_linked import Priority_Queue


class Queue:
    """
    A linked Queue class.
    """

    def to_priority_queue(self):
        """
        ---------------------------------------------------------
        Converts a linked Queue to a linked Priority Queue by moving all nodes
        to a new Priority Queue. source is empty when finished.
        Use: pq = source.to_priority_queue()
        ---------------------------------------------------------
        Parameters:
            None
        Returns‌​‌​​​​‌​​‌‌​‌​​​​‌‌​​​​‌‌‌​:
            pq - a linked Priority Queue. (Priority_Queue)
        ---------------------------------------------------------
        """
        pq = Priority_Queue()
        while self._front is not None:
            node = self._front
            self._front = self._front._next
            pq._move_node(node)

        return pq

    def sum_consecutive(self):
        """
        ---------------------------------------------------------
        Sums consecutive equal elements and replaces them with that sum.
        Use: queue.sum_consecutive()
        ---------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​‌​​​​‌‌​​​​‌‌‌​:
            None
        ---------------------------------------------------------
        """
        if self._front is None:
            return

        current = self._front
        prev = None
        sum_count = 1
        total_sum = current._value

        while current._next is not None:
            if current._value == current._next._value:
                sum_count += 1
                total_sum += current._next._value

            else:
                if sum_count > 1:
                    if prev is None:
                        self._front = _Queue_Node(total_sum, current._next)
                    else:
                        prev._next = _Queue_Node(total_sum, current._next)
                    total_sum = current._next._value
                    sum_count = 1
                else:
                    prev = current
                    total_sum = current._next._value
                    sum_count = 1

            current = current._next

        if sum_count > 1:
            if prev is None:
                self._front = _Queue_Node(total_sum, None)
            else:
                prev._next = _Queue_Node(total_sum, None)

        return


# DO NOT CHANGE CODE BELOW THIS LINE
# =======================================================================

    def __init__(self):
        """
        ---------------------------------------------------------
        Initializes an empty queue. Values are stored in a
        linked structure.
        Use: queue = Queue()
        ---------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​‌​​​​‌‌​​​​‌‌‌​:
            a new Queue object (Queue)
        ---------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the queue is empty.
        Use: b = queue.is_empty()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​‌​​​​‌‌​​​​‌‌‌​:
            True if queue is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._count == 0

    def insert(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the queue.
        Use: queue.insert(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns‌​‌​​​​‌​​‌‌​‌​​​​‌‌​​​​‌‌‌​:
            a copy of value is added to the rear of queue.
        -------------------------------------------------------
        """
        node = _Queue_Node(value, None)

        if self._front is None:
            self._front = node
        else:
            self._rear._next = node

        self._rear = node
        self._count += 1
        return

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the queue
        from front to rear.
        Use: for v in q:
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​‌​​​​‌‌​​​​‌‌‌​:
            value - the next value in the queue (?)
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            yield current._value
            current = current._next


class _Queue_Node:
    """
    A linked Queue Node class.
    """

    def __init__(self, value, next_):
        """
        ---------------------------------------------------------
        Initializes a queue node that contains a copy of value
        and a link to the next node in the queue.
        Use: node = _Queue_Node(value, _next)
        ---------------------------------------------------------
        Parameters:
            value - value for node (?)
            next_ - another Queue node (_Queue_Node)
        Returns‌​‌​​​​‌​​‌‌​‌​​​​‌‌​​​​‌‌‌​:
            a new _Queue_Node object (_Queue_Node)
        ---------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._next = next_
