from pydantic_ai import Agent
import uvicorn
from dotenv import load_dotenv


load_dotenv()
agent = Agent(model="openrouter:openrouter/free")


if __name__ == "__main__":
    web = agent.to_web()
    uvicorn.run(web)

