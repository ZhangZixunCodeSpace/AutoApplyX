import logging

from app.config import config
from app.tool.python_execute import PythonExecute


class ResumeParserTool(PythonExecute):
    """A tool for parsing resumes using Python code execution."""

    name: str = "resume_parser"
    description: str = (
        f"""A flexible tool for parsing resumes using Python code execution. It attempts to extract keywords from resume files (e.g., PDF, DOCX).
        The Python script should:
        1. Accept the file path of the resume (PDF, DOCX, or other common formats).
        2. Attempt to parse the resume content and extract available information like keywords for job search
        3. Handle various formats and potential missing sections as best as possible.
        4. Use print() for all outputs so the job can search as much as possible
        6. Generate a `keywords.txt` file save in the workspace directory: {config.workspace_root}.
        Note:
        Keyword is word in the resume related to job position name"""
    )

    parameters: dict = {
        "type": "object",
        "properties": {
            "code": {
                "type": "string",
                "description": "The Python code that will parse the resume and extract available details.",
            },
        },
        "required": ["code"],
    }

    async def execute(self, code: str, code_type: str | None = None, timeout=5):
        return await super().execute(code, timeout)
