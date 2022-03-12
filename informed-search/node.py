from typing import Union

numeric = Union[int, float]     # Set union of numeric data type


"""
    This class represents graph Node contains heuristic score and node value
"""
class Node:
    """
        This method will create new Node with the given value and heuristic score

        @:param value: value of the node
        @:param heuristic_score: heuristic score

        @:return void
    """
    def __init__(self, value, heuristic_score: numeric):
        self.heuristicScore = heuristic_score
        self.value = value

    """
        This method will check if this node has lower value than other node
        By comparing their heuristic value
        
        @:param other: other node
        
        @:return true if this heuristic value is lower than others
    """
    def __lt__(self, other):
        return self.heuristicScore < other.heuristicScore

    """
        This method will check if this node has lower than or equal value to other node
        By comparing their heuristic value

        @:param other: other node

        @:return true if this heuristic value is lower than or equal to others
    """
    def __le__(self, other):
        return self.heuristicScore <= other.heuristicScore

    """
        This method will check if this node has greater value than other node
        By comparing their heuristic value

        @:param other: other node

        @:return true if this heuristic value is greater than others
    """
    def __gt__(self, other):
        return self.heuristicScore > other.heuristicScore

    """
        This method will check if this node has greater than or equal value to other node
        By comparing their heuristic value

        @:param other: other node

        @:return true if this heuristic value is greater than or equal to others
    """
    def __ge__(self, other):
        return self.heuristicScore >= other.heuristicScore

    """
        This method will check if this node has equal value to other node
        By comparing their heuristic score and their value

        @:param other: other node

        @:return true if its heuristic value and its value is the same as others 
    """
    def __eq__(self, other):
        return self.heuristicScore == other.heuristicScore and self.value == other.value

    """
        This method will check if this node has not equal value to other node
        By comparing their heuristic score and their value

        @:param other: other node

        @:return true if its heuristic value and its value is not the same as others 
    """
    def __ne__(self, other):
        return not self.__eq__(other)

    """
        This method will return key of the node
        
        @:returns its heuristic score, its value
    """
    def __key(self):
        return self.heuristicScore, self.value

    """
        This method will return hashcode of its key
        
        @:return hashed key of the node
    """
    def __hash__(self):
        return hash(self.__key())

    """
        This method will return string representation of this node
        
        @:return "{value} {heuristicScore}"
    """
    def __str__(self):
        return self.value.__str__() + ' ' + self.heuristicScore.__str__()
