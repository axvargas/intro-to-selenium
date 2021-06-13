from unittest import TestLoader, TestSuite
from HtmlTestRunner import HTMLTestRunner
from assertions import Assertions
from searcher import Searcher

# ? loading the test cases
assertions_test = TestLoader().loadTestsFromTestCase(Assertions)
searcher_test = TestLoader().loadTestsFromTestCase(Searcher)

# ? Suite of test cases coonstruction
smoke_test = TestSuite([assertions_test, searcher_test])

# ? Parameters for the report
kwargs = {
    "output": "reports/smoke-report",
    "report_name": "smoke-report",
    "combine_reports": True,
    "add_timestamp": True
}

# ? create runner with the parameters ans run
runner = HTMLTestRunner(**kwargs)
runner.run(smoke_test)