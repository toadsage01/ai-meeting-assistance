import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

from dotenv import load_dotenv
load_dotenv()

# Sample Meeting Transcript
MEETING_TRANSCRIPT = """
Alex: Okay everyone, let's kick off the Project Phoenix sync. Sarah, can you give us the latest on the UI mockups?
Sarah: Yep. The design team has finalized the V2 mockups for the dashboard. I've uploaded them to Figma. John, I need you to review them by end of day tomorrow.
Alex: Great. John, is that feasible?
John: Yes, I'll get the feedback to you, Sarah, by tomorrow EOD. My main focus today is deploying the new authentication service. I'm aiming to get it live by 4 PM.
Alex: Perfect. That's a critical piece. One last thing, we need to decide on the new database. Maria, please schedule a meeting with the infra team for sometime next week to finalize the choice.
Sarah: Sounds good. I'll need the final decision before I can start on the V3 designs.
Alex: Understood. Okay, that's all for today. Let's keep the momentum going.
"""

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "AI Meeting Assistant API is running!"}

# Pydantic Schema
class ActionItem(BaseModel):
    task: str = Field(..., description="The specific task that needs to be done.")
    owner: str = Field(..., description="The person assigned to the task.")
    deadline: str = Field(None, description="The deadline for the task, if mentioned.")

class MeetingInfo(BaseModel):
    summary: str = Field(..., description="A concise, 3-4 sentence summary of the meeting's key points.")
    action_items: List[ActionItem]


# 1. Define LLM and bind it to output structure
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest", temperature=0)
structured_llm = llm.with_structured_output(MeetingInfo)

# 2. Prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert meeting assistant. Your goal is to extract key information from the user's input."),
    ("human", "{transcript}")
])

# 3. extraction chain
extraction_chain = prompt | structured_llm

# Testing chian
if __name__ == "__main__":
    # Run chain on sample transcript
    print("Running extraction chain with Gemini 1.5 Flash...")
    extracted_data = extraction_chain.invoke({"transcript": MEETING_TRANSCRIPT})
    
    # The output from this chain is now a clean Pydantic object, not a dictionary
    print("\n--- Extracted Summary ---")
    print(extracted_data.summary)
    print("\n--- Extracted Action Items ---")
    for item in extracted_data.action_items:
        print(f"- Task: {item.task}, Owner: {item.owner}, Deadline: {item.deadline}")