import csv, json, os, yaml
from typing import List

import datetime
import modelFactory
# from Model import baselineModel_lg, baselineModel_sm
from modelBase import CliNlpModel, Suggestion
from testset import TestCase, TestSet, testset_queries

from testrunner import TestRunner, TestReportDiff

def ensureTestRunerCanRun():
  runner = TestRunner(testset_queries, modelFactory.getBaselineModel_sm())
  report1 = runner.run()
  report1.saveToYamlFile()

def compareSmLgModels():
  runner = TestRunner(testset_queries, modelFactory.getBaselineModel_sm())
  report1 = runner.run()

  runner = TestRunner(testset_queries, modelFactory.getBaselineModel())
  report2 = runner.run()

  diff = TestReportDiff.diffReports(report1, report2)
  diff.saveToYamlFile()

# ensureTestRunerCanRun()
compareSmLgModels()

# TODO: add more runner to measure different combinations
