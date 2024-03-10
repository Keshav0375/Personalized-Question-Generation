
# Personalized Interview Question Generation API

## Description

This API harnesses the power of Google's Gemini model to generate tailored interview questions based on a candidate's resume and the corresponding job description. It aims to create a comprehensive set of questions that effectively assess the candidate's suitability for the role.

## Endpoints

* **POST /question_generation**
    Generates personalized interview questions.

## Request Data

**Parameters:**

- **resume** (str, required): The text content of the candidate's resume.
- **job_description** (str, required): The text content of the job description.

**Format:**

```json
{
    "resume": "(resume content here)",
    "job_description": "(job description content here)"
}
```

## Response Data

**Data Structure:**

```json
{
    "questions": [
        {
            "question_id": 1,
            "response": "(question text here)"
        },
        {
            "question_id": 2,
            "response": "(question text here)"
        },
        ...
    ]
}
```

**Example:**

```json
{
    "questions": [
        {
            "question_id": 1,
            "response": "Welcome, (candidate name)! It's a pleasure to meet you. To start, can you briefly share a bit about your professional journey and what led you to this opportunity?"
        },
        {
            "question_id": 2,
            "response": "I noticed you're currently based in (candidate's location). Are you comfortable with the job location in (job location)?"
        },
        {
            "question_id": 3, 
            "response": "(Tailored question based on resume and job description)"
        },
        ...
    ]
}
```

## Required Packages

* `fastapi`
* `python-dotenv`
* `google-generativeai`

## Additional Notes

* Ensure you have a valid Google API key configured in your environment variable `GOOGLE_API_KEY`.
* The API typically generates 15-18 questions, but the exact number may vary based on the prompt and model response.



