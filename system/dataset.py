# Copyright (C) 2017
# Author: Cesar Roman
# Contact: thecesrom@gmail.com
"""Dataset Functions
The following functions give you access to view and interact with
datasets."""

__all__ = ['getColumnHeaders', 'toDataSet', 'toPyDataSet']


def getColumnHeaders(dataset):
    """Takes in a dataset and returns the headers as a python list.

    Args:
        dataset (Dataset): The input dataset.

    Returns:
        list[str]: A list of column header strings.
    """
    print dataset
    return []


def toDataSet(*args):
    """This function is used to
    1) convert PyDataSets to DataSets, and
    2) create new datasets from raw Python lists.

    When creating a new dataset, headers should have unique names.

    1) system.dataset.toDataSet(dataset)
    2) system.dataset.toDataSet(headers, data)

    Args:
        args: A variable-length argument list.

    Returns:
        Dataset: The newly created dataset.
    """
    return BasicDataset(*args)


def toPyDataSet(dataset):
    """This function converts from a normal DataSet to a PyDataSet,
    which is a wrapper class which makes working with datasets more
    Python-esque.

    Args:
        dataset (Dataset): A DataSet object to convert into a
            PyDataSet.

    Returns:
        PyDataSet: The newly created PyDataSet.
    """
    return PyDataset(dataset)


class BasicDataset(object):
    """
        Representation of result of system.dataset.toDataSet
    """

    def __init__(self, headers, data):
        self.headers = headers
        self.data = data

    def getColumnCount(self):
        return len(self.headers)

    def getColumnName(self, idx):
        return self.headers[idx]

    def getRowCount(self):
        return len(self.data)


class PyDataset(BasicDataset):
    """
        Representation of result of system.dataset.toPydataset
    """

    def __init__(self, dataset):
        self.data = dataset.data
        self.headers = dataset.headers
        super(BasicDataset, self).__init__(dataset.headers, dataset.data)

    def __iter__(self):
        return _PyDatasetIterator(self)


class _PyDatasetIterator():

    def __init__(self, pydataset):
        self.__pydataset = pydataset
        self.__index = 0

    def next(self):
        if self.__index < self.__pydataset.getRowCount():
            final_result = {}
            result = self.__pydataset.data[self.__index]
            for idx, header in enumerate(self.__pydataset.headers):
                final_result[header] = result[idx]
            self.__index = self.__index + 1
            return final_result
        raise StopIteration
