from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import FileResponse
import shutil
import os
from utils import extract_text_from_pdf, generate_pdf
from llm import rewrite_resume

app = FastAPI()

UPLOAD_DIR = "uploads"
OUTPUT_DIR = "output"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)


@app.post("/optimize/")
async def optimize_resume_endpoint(
    resume: UploadFile = File(...),
    job_description: UploadFile = File(None),
    job_text: str = Form(None)
):

    resume_path = os.path.join(UPLOAD_DIR, resume.filename)

    with open(resume_path, "wb") as buffer:
        shutil.copyfileobj(resume.file, buffer)

    resume_text = extract_text_from_pdf(resume_path)

    if job_description:
        job_path = os.path.join(UPLOAD_DIR, job_description.filename)
        with open(job_path, "wb") as buffer:
            shutil.copyfileobj(job_description.file, buffer)
        job_text_content = extract_text_from_pdf(job_path)
    else:
        job_text_content = job_text

    optimized_resume = rewrite_resume(resume_text, job_text_content)

    output_file = os.path.join(OUTPUT_DIR, "optimized_resume.pdf")
    generate_pdf(optimized_resume, output_file)

    return FileResponse(output_file, filename="optimized_resume.pdf")
