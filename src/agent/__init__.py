from .agent import build_agent
import uvicorn

if __name__ == "__main__":
    agent = build_agent()
    web = agent.to_web()
    uvicorn.run(web)
