import json
import os
from typing import Any

from app.config import config
from app.tool.base import BaseTool, ToolResult


class FileSaverTool(BaseTool):
    """
    A tool for saving job application reports in Markdown format.
    This tool will generate a Markdown report with job application details and save it to the specified file path.
    """

    name: str = "file_saver"
    description: str = "A tool for saving job application reports in Markdown format."

    parameters: dict = {
        "type": "object",
        "properties": {
            "file_path": {
                "type": "string",
                "description": "Path where the report will be saved.",
            },
            "job_application_data": {
                "type": "object",
                "description": "Data of the job application to be saved in the report. The data will be formatted as a markdown table or list.",
            },
        },
        "required": ["file_path", "job_application_data"],
    }

    async def execute(
        self, file_path: str, job_application_data: dict[str, Any], **kwargs
    ) -> ToolResult:
        """
        Executes the action to save the job application data in a Markdown file.

        Args:
            file_path: The path where the markdown report will be saved.
            job_application_data: A dictionary containing job application data to include in the report.

        Returns:
            ToolResult: The result of the file saving operation.
        """
        try:
            # Prepare Markdown content
            markdown_content = self.generate_markdown_report(job_application_data)

            # Write content to file
            directory = os.path.dirname(file_path)
            if not os.path.exists(directory):
                os.makedirs(directory)

            with open(file_path, "w", encoding="utf-8") as file:
                file.write(markdown_content)

            return ToolResult(output=f"Job application report saved to {file_path}")
        except Exception as e:
            return ToolResult(error=f"Failed to save the report: {str(e)}")

    def generate_markdown_report(self, job_application_data: dict[str, Any]) -> str:
        """
        Generates a Markdown report from the job application data.

        Args:
            job_application_data: A dictionary containing job application data.

        Returns:
            str: The generated Markdown report.
        """
        markdown_report = "# Job Application Report\n\n"

        # Loop through each job application entry and generate corresponding Markdown
        for job in job_application_data.get("applications", []):
            markdown_report += f"## {job['job_title']}\n"
            markdown_report += f"**Company:** {job['company_name']}\n"
            markdown_report += f"**Location:** {job['location']}\n"
            markdown_report += f"**Status:** {job['status']}\n"
            markdown_report += f"**Application Date:** {job['date']}\n\n"

            markdown_report += "### Resume Details:\n"
            markdown_report += f"- **Name:** {job['resume']['name']}\n"
            markdown_report += f"- **Skills:** {', '.join(job['resume']['skills'])}\n\n"

            # Add any further details as necessary, such as application messages, responses, etc.
            markdown_report += "---\n\n"

        return markdown_report
