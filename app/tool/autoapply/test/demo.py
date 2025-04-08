import asyncio
import time

from app.agent.auto_apply_agent import AutoApplyAgent
from app.agent.manus import Manus
from app.flow.flow_factory import FlowFactory, FlowType
from app.logger import logger


async def run_flow():
    # Create an agent instance for auto-application
    agents = {"auto_apply": AutoApplyAgent(), "Manus": Manus()}

    try:
        prompt = (
            """I have uploaded my resume at 'workspace/resume.pdf'.
            Please search for related positions on available work website api,
            generate a markdown summary of latest and relevant jobs i can apply""",
        )

        # Create a flow using our AUTO_APPLY type and pass the agent
        flow = FlowFactory.create_flow(
            flow_type=FlowType.PLANNING,
            agents=agents,
        )
        logger.warning("Processing your job application request...")

        try:
            start_time = time.time()
            result = await asyncio.wait_for(
                flow.execute(prompt),
                timeout=3600,  # 60 minute timeout
            )
            elapsed_time = time.time() - start_time
            logger.info(f"Request processed in {elapsed_time:.2f} seconds")
            logger.info(result)
        except asyncio.TimeoutError:
            logger.error("Request processing timed out after 1 hour")
            logger.info(
                "Operation terminated due to timeout. Please try a simpler request."
            )
    except KeyboardInterrupt:
        logger.info("Operation cancelled by user.")
    except Exception as e:
        logger.error(f"Error: {str(e)}")


if __name__ == "__main__":
    asyncio.run(run_flow())
