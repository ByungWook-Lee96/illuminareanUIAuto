import unittest
import HtmlTestRunner
from test_exam import TestApplyService

# Load the test cases
test_suite = unittest.TestLoader().loadTestsFromTestCase(TestApplyService)

# Create a test runner
runner = HtmlTestRunner.HTMLTestRunner(output='test-reports', report_name='my_test_report')

# Run the tests
runner.run(test_suite)
