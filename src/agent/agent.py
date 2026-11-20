from pydantic_ai import Agent
from dotenv import load_dotenv
from pydantic_ai.mcp import load_mcp_toolsets


def build_agent():
    load_dotenv()
    mcp_toolset = load_mcp_toolsets("mcp.json")
    toolsets = [ts.defer_loading() for ts in mcp_toolset]
    agent = Agent(model="openrouter:openrouter/free", toolsets=toolsets)
    return agent
