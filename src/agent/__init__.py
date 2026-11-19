from pydantic_ai import Agent
import uvicorn
from dotenv import load_dotenv
from pydantic_ai.mcp import load_mcp_toolsets


load_dotenv()
mcp_toolset = load_mcp_toolsets("mcp.json")
agent = Agent(model="openrouter:openrouter/free",toolsets=mcp_toolset)


if __name__ == "__main__":
    web = agent.to_web()
    uvicorn.run(web)

