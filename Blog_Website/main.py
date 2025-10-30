from agents import Agent, Runner
from connection import config
import asyncio

# Define the blog writer agent

blog_agent = Agent(
    name="Blog Website Agent",
    instructions="""
    You are a professional blog writer.
    Generate a well-structured SEO blog with:
    - Catchy title and meta description
    - H2 headings
    - Keywords used naturally
    - Return in requested format only (HTML, text, or markdown).

    Your task is to write a blog based on the user's selections:
    1. Topic (artificial intelligence, fashion trends, global current affairs)S
    2. Tone / style (friendly, professional)
    3. Keywords / SEO optimization
    4. Content length and output format (HTML, text, markdown)
    """
)

async def main():
    print("👋 Welcome to the Blog Generator!")
    print("Let's set up your blog step-by-step.\n")

    # Step 1: Topic selection
    topic = input("1️⃣ Choose a topic (artificial intelligence, fashion trends, global current affairs): ").strip()

    # Step 2: Tone / style
    tone = input("2️⃣ Choose a tone (friendly, professional): ").strip()

    # Step 3: Keywords
    keywords = input("3️⃣ Enter target keywords (comma separated): ").strip()

    # Step 4: Content format and length
    
    format_type = input("4️⃣ Choose format (html, text, markdown): ").strip().lower()
    length = input("📏 Desired length (e.g., 200 words, 500 words, 1000 words): ").strip()

    # Combine into a single instruction
    
    user_prompt = f"""
    Write a blog about {topic}, using a {tone} tone.
    Optimize it for the keywords: {keywords}.
    The blog should be about {length} long and formatted in {format_type}.
    """

    print("\n🧠 Generating your blog...\n")

    # Run the AI agent with user's selections
    
    result = await Runner.run(
        starting_agent=blog_agent,
        input=user_prompt,
        run_config=config
    )

    # Print the generated result
    
    print("✅ Blog Generated Successfully!\n")
    print(result.final_output)


# Run the script asynchronously

if __name__ == "__main__":
    asyncio.run(main())

