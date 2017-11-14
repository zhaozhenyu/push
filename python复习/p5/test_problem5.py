# -*- coding: utf-8 -*-

from testing import ModuleTestBase, FunctionTestBase, StagedTest

class Problem5ATest (ModuleTestBase):

    fun_name = "digit_sum"

    tests = (
        ((1,), 1),
        ((101,), 2),
        ((21,), 3),
        ((220,), 4),
        ((32,), 5),
        ((123,), 6),
        ((2121,), 6),
        ((1001,), 2),
        ((1234,), 10),
        ((7250,), 14),
        ((5027,), 14),
        ((100001,), 2),
        ((908010,), 18),
        ((901019910,), 30),
        ((312213123,), 18),
        ((901019910019,), 40),
        ((312213213231,), 24),
        ((190901019910019,), 50),
        ((312132213213231,), 30)
    )

    def run_function_tests(self, _suppress_output = False):
        ok, fun, msg = self.find_function(self.fun_name)
        if not ok:
            return False, msg
        if fun is None:
            return False, msg
        ft = FunctionTestBase(fun, self.tests,
                              verbose = self.verbose - 1,
                              raise_exceptions = self.raise_exceptions,
                              suppress_output = _suppress_output)
        ok, msg = ft.run()
        return ok, msg


    def run(self):
        print("checking function " + self.fun_name +
              " in file " + self.filepath)
        print()
        ok, msg = self.run_function_tests(False)
        print(msg)

    ## end Problem5ATest


## To produce less verbose output, change verbose from 3 to 2 or 1:

Problem5ATest("problem5.py", verbose = 3).run()
