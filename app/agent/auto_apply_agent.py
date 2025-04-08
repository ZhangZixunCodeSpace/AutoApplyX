from pydantic import Field

from app.agent.toolcall import ToolCallAgent
from app.config import config
from app.prompt.auto_apply import NEXT_STEP_PROMPT, SYSTEM_PROMPT
from app.tool import Terminate, ToolCollection
from app.tool.autoapply.browser_automation import BrowserAutomationTool
from app.tool.autoapply.markdown_generate import FileSaverTool
from app.tool.autoapply.resume_parser_tool import ResumeParserTool


class AutoApplyAgent(ToolCallAgent):
    """
    An agent that automates job applications.

    This agent extends ToolCallAgent with a set of custom tools to:
    - Parse and optimize resumes.
    - Search and automatically apply for job positions.
    - Generate 1 Markdown summary report of these.
    """

    name: str = "AutoApplyAgent"
    description: str = (
        "An agent designed to automate the job application process by leveraging multiple tools."
    )

    # 使用自定义的系统提示，注入工作目录信息
    system_prompt: str = SYSTEM_PROMPT.format(directory=config.workspace_root)
    next_step_prompt: str = NEXT_STEP_PROMPT

    max_observe: int = 15000
    max_steps: int = 30

    # 注册工具集合，根据需求添加或替换工具
    available_tools: ToolCollection = Field(
        default_factory=lambda: ToolCollection(
            ResumeParserTool(),
            # BrowserAutomationTool(),
            # FileSaverTool(),
            Terminate(),
        )
    )
