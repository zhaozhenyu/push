# -*- coding: utf-8 -*-

from testing import ModuleTestBase, FunctionTestReturningFloat, StagedTest

class Problem1Test (ModuleTestBase):

    fun_name = "approximate_integral"

    s1_tests = (
        ((0, 1, 1), 0.5, 'sum of 0.5'),
        ((1, 2, 1), 4.5, 'sum of 4.5'),
        ((0, 2, 1), 8.0, 'sum of 8.0'),
        ((0, 1, 2), 0.3125, 'sum of 0.03125, 0.28125'),
        ((1, 2, 2), 3.9375, 'sum of 1.09375, 2.84375'),
        ((0, 2, 2), 5.0, 'sum of 0.5, 4.5'),
        ((0, 1, 5), 0.26, 'sum of 0.0008000000000000003, 0.007200000000000002, 0.028000000000000014, 0.07280000000000002, 0.1512'),
        ((1, 2, 5), 3.7799999999999994, 'sum of 0.2728, 0.4472, 0.6839999999999998, 0.9927999999999998, 1.3831999999999995'),
        ((0, 2, 5), 4.16, 'sum of 0.012800000000000004, 0.11520000000000004, 0.44800000000000023, 1.1648000000000003, 2.4192')
    )

    s2_tests = (
        ((-1, 0, 1), -0.5, 'sum of -0.5'),
        ((-2, -1, 1), -4.5, 'sum of -4.5'),
        ((-2, 0, 1), -8.0, 'sum of -8.0'),
        ((-1, 0, 2), -0.3125, 'sum of -0.28125, -0.03125'),
        ((-2, -1, 2), -3.9375, 'sum of -2.84375, -1.09375'),
        ((-2, 0, 2), -5.0, 'sum of -4.5, -0.5'),
        ((-1, 0, 5), -0.260, 'sum of -0.1512, -0.07280, -0.0280, -0.00720, -0.00080'),
        ((-2, -1, 5), -3.780, 'sum of -1.38320, -0.99280, -0.6840, -0.44720, -0.27280'),
        ((-2, 0, 5), -4.160, 'sum of -2.4192, -1.16480, -0.4480, -0.11520, -0.01280')
    )

    s3_tests = (
        ((-1, 1, 1), 0.0, 'sum of 0.0'),
        ((-1, 1, 2), 0.0, 'sum of -0.5, 0.5'),
        ((-1, 1, 4), 0.0, 'sum of -0.28125, -0.03125, 0.03125, 0.28125'),
        ((-2, 2, 1), 0.0, 'sum of 0.0'),
        ((-2, 2, 2), 0.0, 'sum of -8.0, 8.0'),
        ((-2, 2, 4), 0.0, 'sum of -4.5, -0.5, 0.5, 4.5')
    )

    def run_function_tests(self, _suppress_output = False):
        ok, fun, msg = self.find_function(self.fun_name)
        if not ok:
            return False, msg
        if fun is None:
            return False, msg
        ft1 = FunctionTestReturningFloat(fun, self.s1_tests,
                                         precision = 0.0001,
                                         verbose = self.verbose - 1,
                                         raise_exceptions = self.raise_exceptions,
                                         suppress_output = _suppress_output)
        ft2 = FunctionTestReturningFloat(fun, self.s2_tests,
                                         precision = 0.0001,
                                         verbose = self.verbose - 1,
                                         raise_exceptions = self.raise_exceptions,
                                         suppress_output = _suppress_output)
        ft3 = FunctionTestReturningFloat(fun, self.s3_tests,
                                         precision = 0.0001,
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

    ## end Problem1Test


## To produce less verbose output, change verbose from 3 to 2 or 1:

Problem1Test("problem1.py", verbose = 3).run()
