from google.adk.agents import SequentialAgent

from .sub_agents.triage_agent import triage_agent
from .sub_agents.compliance_agent import compliance_agent
from .sub_agents.report_agent import report_agent

from utils import read_file


prohibited_list = read_file("docs/prohibited_list.md")


root_agent = SequentialAgent(
    name="prohibited_qa_agent",
    sub_agents=[triage_agent, compliance_agent, report_agent],
    description="A pipeline agent that triages product information, checks compliance, and generates a structured report on product prohibition.",
)
