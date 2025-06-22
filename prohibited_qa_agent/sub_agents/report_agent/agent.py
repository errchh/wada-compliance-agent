import os

from dotenv import load_dotenv
load_dotenv()

from .prompt import report_prompt
from pydantic import BaseModel, Field

from google.adk.agents import LlmAgent
# from google.adk.models.lite_llm import LiteLlm


# Define output schema
class RestrictionReport(BaseModel):
    is_sufficient: bool = Field(
        description="TRUE if the product ingredient is determined to be sufficient; otherwise, FALSE."
    )
    is_restricted: bool = Field(
        description="TRUE if the product is determined to be prohibited; otherwise, FALSE."
    )
    reason: str = Field(
        description="A brief reason for violation or insufficient product information."
    )


model = "gemini-2.5-flash"
# model = LiteLlm(
#     model="openrouter/microsoft/mai-ds-r1:free",
#     api_base=os.getenv("OPENROUTER_API_BASE"),
#     api_key=os.getenv("OPENROUTER_API_KEY"),
# )


report_agent = LlmAgent(
    name="report_agent",
    model=model,
    instruction=report_prompt,
    description="Generate a report with structured output: is_prohibited and reason.",
    output_schema=RestrictionReport,
    output_key="report",
    disallow_transfer_to_parent=True,
    disallow_transfer_to_peers=True,
)
