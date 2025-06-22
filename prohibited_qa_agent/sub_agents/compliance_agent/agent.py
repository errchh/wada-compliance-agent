import os

from dotenv import load_dotenv
load_dotenv()

from utils import read_file
from .prompt import compliance_prompt

from google.adk.agents import LlmAgent
# from google.adk.models.lite_llm import LiteLlm


model = "gemini-2.5-flash"
# model = LiteLlm(
#     model="openrouter/microsoft/mai-ds-r1:free",
#     api_base=os.getenv("OPENROUTER_API_BASE"),
#     api_key=os.getenv("OPENROUTER_API_KEY"),
# )


compliance_agent = LlmAgent(
    name="compliance_agent",
    model=model,
    instruction=compliance_prompt,
    description="Analyze product information against a specific set of provided policies to determine if the product is allowed to use.",
    output_key="compliance_status",
)
