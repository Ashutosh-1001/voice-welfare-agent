##System Overview

This project is a voice-first AI assistant designed to help users identify suitable government welfare schemes. Users interact with the system entirely through voice in a native Indian language, making it accessible to people who may not be comfortable with text-based or English-only systems. The assistant listens to the user’s request, reasons about what information is required, uses internal tools to make decisions, and responds back using spoken audio.

##High-Level Architecture

The overall flow of the system is simple and intuitive:

User Voice → Speech-to-Text → Agent (Planner–Executor–Evaluator) → Tools → Text-to-Speech → User Voice
This ensures that the interaction remains voice-first from start to finish.

##Agent Lifecycle

The agent follows a clear step-by-step lifecycle during every interaction:
The user speaks a request through voice.
The speech-to-text module converts the spoken input into text.
The planner analyzes the input and identifies missing or required information.
The executor invokes relevant tools, such as the eligibility checking engine.
The evaluator determines the final response based on tool outputs.
The response is converted into speech and played back to the user.

##Planner–Executor–Evaluator Flow

Planner: Determines what information is missing, such as age or income, and decides the next question to ask.

Executor: Uses the eligibility engine to check whether the user qualifies for a specific welfare scheme.

Evaluator: Generates the final response based on the results returned by the tools.
This workflow allows the system to reason and act autonomously rather than relying on fixed responses.

##Tools Used

Eligibility Engine: Applies rule-based logic to determine scheme eligibility.

Memory Module: Stores user details such as age and income across multiple conversation turns.

Speech-to-Text: Converts spoken input into text for processing.

Text-to-Speech: Converts the agent’s responses back into spoken output.

##Memory Design

The system maintains conversation memory by storing key user information like age and income. This allows the agent to remember details across turns, avoid asking repeated questions, and detect contradictions if the user changes previously provided information.

##Failure Handling

The system is designed to handle real-world issues such as unclear speech or incomplete input. If the agent cannot understand the user or if required information is missing, it politely asks the user to repeat or clarify the input, ensuring a smooth and robust interaction experience.