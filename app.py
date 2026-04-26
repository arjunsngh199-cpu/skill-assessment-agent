import gradio as gr

# -----------------------------
# Skill Extraction
# -----------------------------
def extract_skills(text):
    skills_list = [
    "html", "css", "javascript", "react",
    "python", "sql", "excel",
    "communication", "problem-solving",
    "java", "c++", "machine learning", "data analysis"
]

    found = []
    text_lower = text.lower()

    for skill in skills_list:
        if skill in text_lower:
            found.append(skill.capitalize())

    return found


# -----------------------------
# Interview Question Generator
# -----------------------------
def generate_questions(missing_skills):
    questions = []

    for skill in missing_skills:
        q = f"""
Skill: {skill}

Interview Question:
What is a practical use of {skill}?

Good Answer Should Include:
- Basic explanation
- Real-world example

Level:
Beginner
"""
        questions.append(q)

    return "\n".join(questions)


# -----------------------------
# Learning Plan Generator
# -----------------------------
def generate_learning_plan(missing_skills):
    plans = []

    for skill in missing_skills:
        plan = f"""
Skill: {skill}

What to Learn:
Basics of {skill} and how it is used in real projects

Time Estimate:
1-2 weeks

Resources:
- YouTube tutorials on {skill}
- FreeCodeCamp
- Practice projects

Weekly Plan:
Week 1: Learn basics
Week 2: Build small project
"""
        plans.append(plan)

    return "\n".join(plans)


# -----------------------------
# Main Agent Logic
# -----------------------------
def respond(jd, resume):
    jd_skills = extract_skills(jd)
    resume_skills = extract_skills(resume)

    matching = [s for s in jd_skills if s in resume_skills]
    missing = [s for s in jd_skills if s not in resume_skills]

    questions = generate_questions(missing)
    learning_plan = generate_learning_plan(missing)

    # Simple scoring logic
    strength = "Strong Match" if len(missing) <= 2 else "Needs Improvement"

    output = f"""
===== AI SKILL ASSESSMENT REPORT =====

🧠 Overall Fit: {strength}

📌 Required Skills:
{", ".join(jd_skills)}

👤 Candidate Skills:
{", ".join(resume_skills)}

✅ Matching Skills:
{", ".join(matching)}

❌ Missing Skills:
{", ".join(missing)}

-------------------------------------

🎤 INTERVIEW ASSESSMENT:

{questions}

-------------------------------------

📚 PERSONALISED LEARNING PLAN:

{learning_plan}

=====================================
"""

    return output


# -----------------------------
# Gradio UI
# -----------------------------
iface = gr.Interface(
    fn=respond,
    inputs=[
        gr.Textbox(label="📄 Job Description", lines=8, placeholder="Paste job description here..."),
        gr.Textbox(label="👤 Candidate Resume", lines=8, placeholder="Paste resume here...")
    ],
    outputs=gr.Textbox(label="📊 AI Assessment Report", lines=25),
    title="🚀 AI Skill Assessment & Learning Agent",
    description="Analyze skills, identify gaps, simulate interview questions, and generate a personalized learning plan."
)

iface.launch()