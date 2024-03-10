from fastapi import FastAPI, Form
import os
import json
from dotenv import load_dotenv
import google.generativeai as genai

app = FastAPI()

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def get_gemini_response(input):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input)
    return response.text


@app.post("/question_generation")
async def evaluate_resume(resume: str = Form(...), job_description: str = Form(...)):
        prompt = f"""
        You are an experienced interviewer, adept at crafting personalized questions tailored to individual resumes and job descriptions.
        Your approach is meticulous, beginning with a warm introduction of the candidate before seamlessly transitioning into relevant inquiries.

        **Resume:**
        {resume}

        **Job Description:**
        {job_description}

        **Personalized Interview Questions:**
        Commence with a brief introduction of the candidate, followed by an inquiry regarding their comfortability with the job location. Subsequently, generate 15 to 18 targeted interview questions based on the candidate's resume and job description.

        I need response in a structure as
        {{
            "questions":
                [
                    {{
                        "question_id": 1,
                        "response": ""
                    }},
                    ...
                ]
        }}
        """

        response = get_gemini_response(prompt)

        # Parse the response string into a dictionary
        response_dict = json.loads(response)

        return response_dict

