import os
from smolagents import CodeAgent, DuckDuckGoSearchTool, OpenAIServerModel
from dotenv import load_dotenv, find_dotenv
load_dotenv()

model = OpenAIServerModel(
    model_id="gpt-4.1-mini",
    api_key=os.getenv("OPENAI_API_KEY"),
)


tools = [
    DuckDuckGoSearchTool(max_results=6),
]

agent = CodeAgent(
    model=model,
    tools=tools,
    add_base_tools=True,   # терминал
    # max_iterations=6,      # лимит шагов на задачу GAIA
    # verbose=True           # печать размышлений для UI
)
agent.max_steps = 6
