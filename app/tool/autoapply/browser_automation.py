from typing import Any, Dict

from app.config import config
from app.tool.browser_use_tool import BrowserUseTool


class BrowserAutomationTool(BrowserUseTool):
    """A tool for automating browser tasks essential for job application processes."""

    name: str = "browser_automation"
    description: str = (
        "Automates job search and data collection from job platforms based on extracted resume keywords.\n"
        "Key functionalities include:\n"
        "1. 'search_jobs': Search for jobs using keywords.txt in workspace directory by querying external platforms.\n"
        "2. 'collect_job_info': Extract detailed job information such as job description, requirements, and salary. "
        "Use print() for all outputs so the results can be collected and save in the same markdown file in workspace directory: {directory}".format(
            directory=config.workspace_root
        )
    )

    parameters: Dict[str, Any] = {
        "type": "object",
        "properties": {
            "action": {
                "type": "string",
                "description": "The action to perform: 'search_jobs' or 'collect_job_info'.",
                "enum": ["search_jobs", "collect_job_info"],
            },
            "query": {
                "type": "string",
                "description": "The search query for 'search_jobs' action.",
            },
            "job_url": {
                "type": "string",
                "description": "The URL of a job listing for 'collect_job_info' action.",
            },
        },
        "required": ["action"],
    }

    async def execute(self, action: str, **kwargs) -> Dict[str, Any]:
        """
        Executes the specified browser automation action.
        """
        return await super().execute(action=action, **kwargs)
