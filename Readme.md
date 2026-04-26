#  AI Skill Assessment & Personalized Learning Agent

##  Overview

This project evaluates a candidate’s skills by comparing their resume with a job description. It identifies gaps, generates interview questions, and provides a personalized learning plan.

---

## Features

* Skill extraction from JD and Resume
* Matching and missing skills detection
* Interview-style questions
* Personalized learning roadmap
* Simple UI using Gradio

---

## Run Locally

1. Install dependencies:
   pip install gradio

2. Run the app:
   python app.py

3. Open browser:
   http://127.0.0.1:7860

---

## How It Works

User Input → Skill Extraction → Comparison → Gap Detection → Questions → Learning Plan

---

## Architecture

User Input (JD + Resume)  
↓  
Skill Extraction  
↓  
Skill Comparison  
↓  
Gap Detection  
↓  
Interview Question Generation  
↓  
Learning Plan Generation  
↓  
Final Output  

---

## Scoring Logic

The system evaluates candidate fit based on missing skills:

- Missing skills ≤ 2 → Strong Match  
- Missing skills > 2 → Needs Improvement  

The approach focuses on clarity, usability, and reliability using rule-based extraction and structured outputs.

## Sample Input & Output

### Input:
Job Description: Frontend Developer (HTML, CSS, JavaScript, React)  
Resume: HTML, CSS, basic JavaScript  

### Output:
- Matching Skills: HTML, CSS, JavaScript  
- Missing Skills: React  
- Interview Questions generated  
- Learning Plan generated  

## Author

Arjun Singh
