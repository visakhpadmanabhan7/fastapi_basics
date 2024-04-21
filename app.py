from fastapi import FastAPI, HTTPException
from transformers import pipeline
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define a request body model for question answering
class QuestionRequest(BaseModel):
    context: str
    question: str

# Load the model once to save resources
qa_pipeline = pipeline("question-answering", model="bert-large-uncased-whole-word-masking-finetuned-squad")

@app.post("/ask/")
def answer_question(request: QuestionRequest):
    try:
        result = qa_pipeline({
            "context": request.context,
            "question": request.question
        })
        return {"answer": result['answer']}
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        raise HTTPException(status_code=500, detail="An error occurred while processing the request.")
