### Reflection Log

Implementing the two-agent itinerary planner taught me how role separation and clear handoff logic can greatly improve generation quality. The Planner Agent worked as a structured content generator that transformed vague user prompts into consistent five-section itineraries. This required balancing creativity with feasibility—learning to embed defaults and pacing constraints directly in the prompt. The Reviewer Agent then acted as a quality gate, applying targeted fact-checks and budget sanity checks using the `internet_search` tool.

The main challenge was controlling Reviewer verbosity and ensuring it didn’t overwrite the whole text. I solved this by enforcing a fixed A/B/C output format where only revised sections are returned. Another issue was timing: excessive tool calls slowed execution. Limiting fact-checking to high-impact uncertainties (e.g., closures, ticket prices) made it faster and cleaner.

For design choices, I gave the Planner a consistent textual layout instead of JSON, improving readability and stability under Streamlit. The Reviewer was designed to act like an editor—surgical, evidence-based, and brief—rather than a re-writer. This separation mirrored real-world review workflows and made the app feel more collaborative than hierarchical.

**External tools used:** OpenAI API via Streamlit template; ChatGPT was used to draft and refine the system prompts and reflection wording.

