import os

from dotenv import load_dotenv
load_dotenv()

from .prompt import triage_prompt

from google.adk.agents import LlmAgent
# from google.adk.models.lite_llm import LiteLlm


model = "gemini-2.5-flash"
# model = LiteLlm(
#     model="openrouter/microsoft/mai-ds-r1:free",
#     api_base=os.getenv("OPENROUTER_API_BASE"),
#     api_key=os.getenv("OPENROUTER_API_KEY"),
# )


triage_agent = LlmAgent(
    name="triage_agent",
    model=model,
    instruction=triage_prompt,
    description="Determine if the provided product information is complete and detailed enough for a full compliance review.",
    output_key="triage_status",
)
