import json
import os

from code_check import CodeCheck
from task_interfaces import MetaTaskInterface
from task_interfaces import SubscriptionLevels


class Task(MetaTaskInterface):
    """
    Verifies files are formatted with prettier.
    """

    name = "Pylint"
    slug = "pylint"
    pass_summary = ""
    pass_text = ""
    fail_summary = "All files not formatted correctly."
    fail_text = ""
    actions = None
    subscription_level = SubscriptionLevels.FREE

    def execute(self, github_body, settings) -> bool:
        head_branch = github_body["pull_request"]["head"]["ref"]
        base_branch = github_body["repository"]["default_branch"]

        code_check = CodeCheck(
            token=github_body.get("githaxs").get("token"),
            branch=head_branch,
            default_branch=base_branch,
            full_repo_name=github_body.get("repository", {}).get("full_name"),
            source_script_path="%s/task.sh" % os.path.dirname(__file__),
        )

        code_check.execute()

        self.fail_text = code_check.fail_text

        return code_check.result