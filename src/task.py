import json
import os

from task_interfaces import TaskInterface, SubscriptionLevels, TaskTypes

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

    command = "PYLINTHOME=/tmp pylint"
    file_filters = ".*.py$"

    def execute(self, github_body, settings) -> bool:
        pass
