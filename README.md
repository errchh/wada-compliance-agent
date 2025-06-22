![cover](demo/cover_art.png)

# WADA Prohibited List Compliance Agent

## Summary

An AI agent that ensures pro athletes' sport supplements are World Anti-Doping Agency (WADA) compliant, preventing accidental doping from off-the-shelf sport supplement products.

This is my entry for the **Google Agent Development Kit Hackathon** with Google Cloud 2025 under **Automation of Complex Process** catagory.

## About

Professional athletes are solely responsible for prohibited substances inside their systems. While the World Anti-Doping Agency (WADA) provides a comprehensive list, its complex chemical nomenclature makes manual supplement compliance checks unwieldy and error-prone.

This AI agent automates the verification process for off-the-shelf sport supplement products, ensuring accurate and efficient adherence to anti-doping regulations.

## AI Agent

This AI agent was developed using the Google Agent Development Kit (ADK), employing a multi-agent architecture. The system uses a sequential agent workflow to control the flow of states, comprising specialised components:

![flowchart](demo/flowchart.png)

* **Triage Agent**: Responsible for initial processing and validation of user input, ensuring data quality before further analysis.
* **Compliance Agent**: The system's core, this agent meticulously validates supplement substances against the WADA Prohibited List to identify potential violations.
* **Report Agent**: Generates a structured output in JSON format for integration with downstream systems or analytical tools. **Pydantic** was used to enforce strict data schemas, ensuring the accuracy and integrity of all structured outputs.

This modular, agent-based design ensures scalability, maintainability, and precise control over each stage of the compliance-checking process.

## Usage

![devui](demo/devUI_demo.png)


https://github.com/user-attachments/assets/697c06d4-24d2-4e29-b1f5-f7078d1b5b1e



1. Install dependencies

```
uv sync
```

2. Start Dev UI

```
adk web
```

3. Start query

```
User input ingredients in the prompt
```

4. AI agent responses

States example:

```
INSUFFICIENT. The individual concentrations for β-Phenylethylamine, Caffeine, and Theobromine within the "Acuity Blend" are not specified, only the total for the blend is provided. Additionally, the serving size and recommended daily dosage are missing, which are necessary to determine the total daily intake of the ingredients.

VIOLATED. Contains **β-Phenylethylamine (β-PEA)**, a prohibited non-Specified Stimulant (S6.a).
```

AI agent response with a JSON structured output of result and reason. Example:

```
{
  "is_sufficient": false,
  "is_prohibited": true,
  "reason": "Contains β-Phenylethylamine (β-PEA), a prohibited non-Specified Stimulant (S6.a)."
}
```
