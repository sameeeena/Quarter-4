from agents import Agent, Runner
from connection import config
import asyncio

# Define your resume builder agent
resume_builder_agent = Agent(
    name="Resume Builder Agent",
    instructions="""
    You are an expert resume generator agent.
    Your task is to collect information from the user about:
    1. Personal information (name, location, LinkedIn)
    2. Academic information (school, degree, achievements)
    3. Work Experience (company, title, duration)
    4. Career objectives (objectives)
    5. Skills (skills)
    6. Certificates or Awards (certs)
    
    When the user provides all the information, create a clean and professional resume.
    """
)

async def main():
    print("👋 Welcome to the Resume Builder!")
    print("I'll help you create a professional resume. Let's begin.\n")

    # Step 1: Personal Information
    print("🧍 PERSONAL INFORMATION")
    name = input("What's your full name? ").strip()
    location = input("Where are you located? ").strip()
    linkedin = input("Do you have a LinkedIn or portfolio link? (optional) ").strip()

    # Step 2: Academic Information
    print("\n🎓 ACADEMIC INFORMATION")
    school = input("What's the name of your school/university? ").strip()
    degree = input("What degree did you earn (or are pursuing)? ").strip()
    achievements = input("Any academic achievements you'd like to mention? ").strip()

    # Step 3: Work Experience
    print("\n💼 WORK EXPERIENCE")
    company = input("What's your most recent company name? ").strip()
    title = input("What was your job title/responsibilities? ").strip()
    duration = input("How long did you work there? ").strip()

    # Step 4: Career Objectives
    print("\n🎯 CAREER OBJECTIVE")
    objectives = input("Can you briefly describe your career goals? ").strip()

    # Step 5: Skills
    print("\n⚙️ SKILLS")
    skills = input("List your technical and professional skills (comma-separated): ").strip()

    # Step 6: Certificates and Awards
    print("\n🏆 CERTIFICATES / AWARDS")
    certs = input("Do you have any certificates or awards? If yes, list them with issuer and date: ").strip()

    # Combine all inputs into a single prompt for the AI agent
    user_prompt = f"""
Use the following details to create a clean, professional resume.

Personal Information:
Name: {name}
Location: {location}
LinkedIn/Portfolio: {linkedin}

Education:
School/University: {school}
Degree: {degree}
Achievements: {achievements}

Work Experience:
Company: {company}
Job Title/Responsibilities: {title}
Duration: {duration}

Career Objective:
{objectives}

Skills:
{skills}

Certificates/Awards:
{certs}

Please format this as a professional resume with clear sections, spacing, and layout.
"""

    print("\n🧠 Generating your resume...\n")

    # Run the AI agent
    result = await Runner.run(
        starting_agent=resume_builder_agent,
        input=user_prompt,
        run_config=config
    )

    print("✅ Resume Generated Successfully!\n")
    print(result.final_output)


# Run the async function correctly
if __name__ == "__main__":
    asyncio.run(main())












