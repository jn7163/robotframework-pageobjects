import glob
import unittest

from basetestcase import BaseTestCase


class SmokeTestCase(BaseTestCase):
    """
    Tests for basic options and option handling.

    For tests outside of Robot, individual environment variables
    in the form of "$PO_" (eg. $PO_BROWSER) set options.
    A variable of $PO_VAR_FILE can be set to a path to a Python
    module that can set variables as well. Individual
    environment variables override those set in the variable file.

    For tests within the Robot context the behavior follows
    standard Robot Framework..variables can be set on the
    command-line with --variable (eg. --variable=browser=firefox, which
    override the variables set in a variable file, set with --variablefile=

    The BaseTestCase setUp removes all PO environment variables.
    tearDown restores them. It also removes po_log file in
    setUp and tearDown and screenshots in setUp

    This assures that at the beginning of each test there are no
    PO_ environment variables set and that we are running with
    default options. The tests are then free to set environment variables or
    write variable files as needed.

    This test case tests browser option, but in effect also tests option handling, assuming
    that options are gotten internally using the optionhandler.OptionHandler class.
    """

    def test_unittest_rel_url_set(self):
        self.set_baseurl_env()
        run = self.run_scenario("test_rel_url.py")
        self.assert_run(run, search_output="OK", expected_browser="phantomjs")

    def test_robot_rel_url_set(self):
        run = self.run_scenario("test_rel_url.robot", variable="baseurl:%s" % self.base_file_url)
        self.assert_run(run, search_output="PASS", expected_browser="phantomjs")

    def test_unittest_uri_template(self):
        self.set_baseurl_env()
        run = self.run_scenario("test_template_passed.py")
        print "\n\n***"
        print run.output
        print "\n***"
        self.assert_run(run, expected_returncode=0, search_output="OK")

    def test_robot_uri_template(self):
        run = self.run_scenario("test_template_passed.robot", variable="baseurl:%s" % self.base_file_url)
        self.assert_run(run, expected_returncode=0, search_output="PASS")


class ActionsTestCase(BaseTestCase):
    @unittest.skip("NOT IMPLEMENTED YET")
    def unittest_test_screenshot_on_failure(self):
        run = self.run_scenario("test_fail.py")
        self.assertEquals(len(glob.glob("*.png")), 1, "On Failure page object should take screenshot")

    @unittest.skip("NOT IMPLEMENTED YET")
    def robot_test_screenshot_on_failure(self):
        run = self.run_scenario("test_fail.robot")
        self.assertEquals(len(glob.glob("*.png")), 1, "On Failure page object should generate screenshot")


if __name__ == "__main__":
    unittest.main()








