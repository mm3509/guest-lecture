import numpy


def distance(x, y):
    """Euclidean distance.
    """
    return numpy.sum(numpy.square(x - y))


def kNN1(x, training_X, training_y):
    """Simple 1-nearest neighbor algorithm.
    """

    # TODO: implement 1-nearest neighbor here.

    # Return a tuple, with the label of the nearest neighbor, and its position
    # in the training data (for plotting).

    return training_y[nearest], nearest


def kNN(x, k, training_X, training_y):
    """
    Nearest-neighbors for the general case of k.
    """
    # TODO (at home, if interested): implement k-nearest-neighbors here.

    # Also return a tuple, as above.
    
    return 
