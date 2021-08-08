import json
import os

from task_interfaces import TaskInterface, SubscriptionLevels, TaskTypes
from code_check import CodeCheck
from task_interfaces import MetaTaskInterface
from task_interfaces import SubscriptionLevels


class Task(TaskInterface):
    """
    Runs pylint on files.
    """

    name = "Pylint"
    slug = "pylint"
    pass_summary = ""
    pass_text = ""
    fail_summary = "All files not formatted correctly."
    fail_text = ""
    actions = None
    subscription_level = SubscriptionLevels.FREE
    type = TaskTypes.CODE_FORMAT
    source_script_path="%s/task.sh" % os.path.dirname(__file__),
    handler = "task"

    def execute(self, github_body, settings) -> bool:
        pass
