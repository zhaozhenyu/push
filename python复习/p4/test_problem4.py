# -*- coding: utf-8 -*-

from testing import ModuleTestBase, FunctionTestOnMutableArgs, StagedTest

class Problem4Test (ModuleTestBase):

    fun_name = 'unnest'

    s1_tests = (
        (([2, 1, 3, [0, 4]],), [2, 1, 3, 0, 4]),
        (([1, [3], [2, 4], 0],), [1, 3, 2, 4, 0]),
        (([[[3, 0], 1], 4, 2],), [3, 0, 1, 4, 2]),
        (([1, [2], [[3], [[4], 5]]],), [1, 2, 3, 4, 5]),
        (([0, [[2, [1], 4]], [[3]]],), [0, 2, 1, 4, 3]),
        (([[[0], 2], 3, 1, 4],), [0, 2, 3, 1, 4]),
        (([[9, 5, 0, 4], [8, 7, 1], 6, 3, 2],), [9, 5, 0, 4, 8, 7, 1, 6, 3, 2]),
        (([6, 9, [2, 8, 7, 4], [[0, [5]], 1, 3]],), [6, 9, 2, 8, 7, 4, 0, 5, 1, 3])
        )

    s2_tests = (
        (([[0], [[[2, 4, 3]], [1]]],), [0, 2, 4, 3, 1]),
        (([[4, [[1]]], 0, 2, 3],), [4, 1, 0, 2, 3]),
        (([[[1, 3, 4, [[[[2]]]]]], 0],), [1, 3, 4, 2, 0]),
        (([[4], 1, [[3, [0], [[2]]]]],), [4, 1, 3, 0, 2]),
        (([[[0]], 4, [[[3]]], [1, 2]],), [0, 4, 3, 1, 2]),
        (([7, [[5], [2], 4], 6, [[[0, [8], 1]], 9], [[3]]],), [7, 5, 2, 4, 6, 0, 8, 1, 9, 3]),
        (([[2, 6, [[[5]]], [7], 4, 9, 1, 0, 8], [[3]]],), [2, 6, 5, 7, 4, 9, 1, 0, 8, 3]),
        (([8, 6, 2, 1, 5, 7, 3, 9, [[[[[[[4]]]]]]], [0]],), [8, 6, 2, 1, 5, 7, 3, 9, 4, 0]),
        (([[4, [[[1]], 5, 2, 8, [[[3]], 0, 6]], 7, 9]],), [4, 1, 5, 2, 8, 3, 0, 6, 7, 9]),
        (([[[[1, 9], [3]], [2, [7, 5, 8], 6, 0]], 4],), [1, 9, 3, 2, 7, 5, 8, 6, 0, 4])
        )

    s3_tests = (
        (([1, [], [2], [[3], [], [[4], [], 5]]],), [1, 2, 3, 4, 5]),
        (([1, [[3], []], [], [[], 2, 4], 0],), [1, 3, 2, 4, 0]),
        (([0, [[], [2, [1], 4]], [[], [3]]],), [0, 2, 1, 4, 3]),
        (([[], [[], [[], 3, 0], 1], [], 4, 2],), [3, 0, 1, 4, 2]),
        (([[[0], [], 2], [], [], 3, 1, [], 4],), [0, 2, 3, 1, 4]),
        (([2, [[]], 1, [3], [[0, 4]]],), [2, 1, 3, 0, 4]),
        (([[[]]],), [])
        )


    def run_function_tests(self, _suppress_output = False):
        ok, fun, msg = self.find_function(self.fun_name)
        if not ok:
            return False, msg
        if fun is None:
            return False, msg
        ft1 = FunctionTestOnMutableArgs(fun, self.s1_tests,
                                        verbose = self.verbose - 1,
                                        raise_exceptions = self.raise_exceptions,
                                        suppress_output = _suppress_output)
        ft2 = FunctionTestOnMutableArgs(fun, self.s2_tests,
                                        verbose = self.verbose - 1,
                                        raise_exceptions = self.raise_exceptions,
                                        suppress_output = _suppress_output)
        ft3 = FunctionTestOnMutableArgs(fun, self.s3_tests,
                                        verbose = self.verbose - 1,
                                        raise_exceptions = self.raise_exceptions,
                                        suppress_output = _suppress_output)
        st = StagedTest((ft1, ft2, ft3), self.verbose, self.raise_exceptions)
        ok, msg = st.run()
        return ok, msg

    def run(self):
        print("checking function " + self.fun_name +
              " in file " + self.filepath)
        print()
        ok, msg = self.run_function_tests(False)
        print(msg)

    ## end Problem4Test


## To produce less verbose output, change verbose from 3 to 2 or 1:

Problem4Test("problem4.py", verbose = 3).run()
