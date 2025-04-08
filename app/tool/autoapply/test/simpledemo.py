import asyncio

from app.agent.auto_apply_agent import AutoApplyAgent
from app.agent.manus import Manus


async def main():
    # 实例化 AutoApplyAgent
    agent = AutoApplyAgent()
    # agent = Manus()

    # 传入一个任务描述。该描述要求代理处理自动投递任务，
    # 例如：解析保存在 workspace/resume.pdf 的简历，
    # 搜索CTgoodjobs上的相关岗位，
    # 自动进行投递操作，并生成一个 markdown 格式的应用摘要报告。
    prompt = """
       I have uploaded my resume at 'workspace/resume.pdf'.
            Please search for related positions on https://web3.career/,
            generate a markdown summary of 50 jobs i can apply
        """

    # 调用 Agent 的 run 方法启动任务
    result = await agent.run(prompt)
    print("Agent run result:")
    print(result)


if __name__ == "__main__":
    asyncio.run(main())
