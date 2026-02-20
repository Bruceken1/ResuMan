import os
from huggingface_hub import InferenceClient

client = InferenceClient(
    model="mistralai/Mistral-7B-Instruct-v0.2",
    token=os.getenv("HF_TOKEN")
)

def rewrite_resume(resume_text, job_text):

    prompt = f"""
You are a professional ATS resume optimization system.

STRICT RULES:
- Do NOT invent experience.
- Do NOT add new companies.
- Do NOT fabricate skills.
- Rewrite existing content to align strongly with job description.
- Improve clarity and measurable impact.
- Optimize for ATS keyword matching.

JOB DESCRIPTION:
{job_text}

ORIGINAL RESUME:
{resume_text}

Return a clean, fully rewritten professional resume.
"""

    response = client.text_generation(
        prompt,
        max_new_tokens=1200,
        temperature=0.3
    )

    return response
