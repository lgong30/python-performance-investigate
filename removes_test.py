import unittest
import numpy as np
from copy import deepcopy
import time
from removes import remove_with_move, remove, efficient_remove


class FooTest(unittest.TestCase):
    """Sample test case"""


    # preparing to test
    def setUp(self):
        """ Setting up for the test """
        print "FooTest:setUp_:begin"
        ## do something...
        self.N = 10000
        self.K = 0
        self.myList = []
        self.removalIndices = []
        self.test_num = 100
        self.startTime = time.time()
        print "FooTest:setUp_:end"

    # ending the test
    def tearDown(self):
        """Cleaning up after the test"""
        print "FooTest:tearDown_:begin"
        ## do something...
        t = time.time() - self.startTime
        print "%s: %.3f" % (self.id(), t)
        print "FooTest:tearDown_:end"

    # test routine A
    def testCorrectness(self):
        """Correctness test"""
        for test_id in range(self.test_num):
            self.myList = range(self.N)
            self.K = np.random.randint(1, high=int(0.9 * self.N))
            removalIndices = np.random.permutation(self.N).tolist()[::self.K]
            self.removalIndices = sorted(removalIndices)
            myListA = deepcopy(self.myList)
            myListB = deepcopy(self.myList)
            myListC = deepcopy(self.myList)
            myListA = remove_with_move(myList=myListA, removalIndices=self.removalIndices)
            myListB = remove(myList=myListB, removalIndices=self.removalIndices, inplace=True)
            myListC = efficient_remove(myList=myListC, removalIndices=self.removalIndices, inplace=True)

            self.assertEquals(len(myListA), len(myListB), len(myListC))
            for a,b,c in zip(myListA, myListB, myListC):
                self.assertEquals(a, b, c)

    def testRunningTimeSparseA(self):
        for test_id in range(self.test_num):
            self.myList = range(self.N)
            self.K = np.random.randint(1, high=int(0.2 * self.N))
            removalIndices = np.random.permutation(self.N).tolist()[::self.K]
            self.removalIndices = sorted(removalIndices)
            myListA = self.myList
            remove_with_move(myList=myListA, removalIndices=self.removalIndices)
            self.assertTrue(True)

    def testRunningTimeSparseB(self):
        for test_id in range(self.test_num):
            self.myList = range(self.N)
            self.K = np.random.randint(1, high=int(0.2 * self.N))
            removalIndices = np.random.permutation(self.N).tolist()[::self.K]
            self.removalIndices = sorted(removalIndices)
            myListA = self.myList
            remove(myList=myListA, removalIndices=self.removalIndices, inplace=True)
            self.assertTrue(True)

    def testRunningTimeSparseC(self):
        for test_id in range(self.test_num):
            self.myList = range(self.N)
            self.K = np.random.randint(1, high=int(0.2 * self.N))
            removalIndices = np.random.permutation(self.N).tolist()[::self.K]
            self.removalIndices = sorted(removalIndices)
            myListA = self.myList
            efficient_remove(myList=myListA, removalIndices=self.removalIndices, inplace=True)
            self.assertTrue(True)

    # # test routine A
    # def testSparseRemoval(self):
    #     """Test routine A"""
    #     print "FooTest:testSparseRemoval"


    # test routine B
    # def testB(self):
    #     """Test routine B"""
    #     print "FooTest:testB"


if __name__ == '__main__':
    unittest.main()