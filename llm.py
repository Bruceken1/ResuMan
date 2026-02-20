
import ollama

def rewrite_resume(resume_text, job_text):
    
    prompt = f"""
    You are a professional ATS optimization system.
    
    STRICT RULES:
    - Do NOT invent experience
    - Do NOT add companies not present
    - Do NOT fabricate skills
    - Rewrite existing experience to better align with job description
    - Improve clarity and measurable achievements
    - Optimize for ATS keyword alignment
    
    JOB DESCRIPTION:
    {job_text}
    
    ORIGINAL_RESUME:
    {resume_text}
    
    Return a fully rewritten professional resume.
    """
    
    response = ollama.chat(
        model = "llama3",
        messages = [
            {"role": "user", "conten": prompt}
        ]
    )
    
    return response["message"]["content"]

