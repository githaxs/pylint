import json
import os

from task_interfaces import StaticAnalysisTask, SubscriptionLevels

class Task(StaticAnalysisTask):
    """
    Runs pylint on files.
    """

    name = "Pylint"
    subscription_level = SubscriptionLevels.FREE
    source_script_path = "%s/task.sh" % os.path.dirname(__file__)