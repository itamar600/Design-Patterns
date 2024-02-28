from abc import ABC, abstractmethod

class FilterStrategy(ABC):
    """
    Abstract base class defining the interface for filter strategies.
    """
    @abstractmethod
    def removeValue(self, val):
        """
        Abstract method to determine if a value should be removed based on the strategy.

        Args:
            val: The value to be evaluated.

        Returns:
            bool: True if the value should be removed, False otherwise.
        """
        pass

class RemoveNegativeStrategy(FilterStrategy):
    """
    Concrete implementation of FilterStrategy to remove negative values.
    """
    def removeValue(self, val):
        """
        Implementation of removeValue method for removing negative values.

        Args:
            val: The value to be evaluated.

        Returns:
            bool: True if the value is negative, False otherwise.
        """
        return val < 0
    
class RemoveOddStrategy(FilterStrategy):
    """
    Concrete implementation of FilterStrategy to remove odd values.
    """
    def removeValue(self, val):
        """
        Implementation of removeValue method for removing odd values.

        Args:
            val: The value to be evaluated.

        Returns:
            bool: True if the value is odd, False otherwise.
        """
        return abs(val) % 2
    
class Values:
    def __init__(self, vals):
        """
        Constructor for Values class.

        Args:
            vals (list): List of values.
        """
        self.vals = vals

    def filter(self, strategy):
        """
        Method to filter values based on the provided strategy.

        Args:
            strategy (FilterStrategy): The filter strategy to be applied.

        Returns:
            list: Filtered list of values.
        """
        res = []
        for n in self.vals:
            if not strategy.removeValue(n):
                res.append(n)
        return res

# Creating an instance of Values with a list of values
values = Values([-7, -4, -1, 0, 2, 6, 9])

# Using RemoveNegativeStrategy to filter out negative values
print(values.filter(RemoveNegativeStrategy())) # [0, 2, 6, 9]

# Using RemoveOddStrategy to filter out odd values
print(values.filter(RemoveOddStrategy())) # [-4, 0, 2, 6]
