from agents import Agent, RunContextWrapper
from pydantic import BaseModel


# class Blogs (BaseModel):
#     topic: str
#     tone : str
#     length : int 
#     format : str

# blogPost = Blogs(
#     topic = "Artificial intelligence , Fashion trends, current affairs",
#     tone = "friendly, Professional",
#     length= "100 _ 1000",
#     format= "markdown, html, text"
#     )

# async def my_dynamic_instructions(ctx: RunContextWrapper[blogPost], agent: Agent):
#     if ctx.context.tone == 'friendly'
#         return """
#             Keep your answers simple and easy to understand in friendly manners.
#         """
#         or ctx.context.tone == 'Professional'
#         return """
#     """
#     elif ctx.context.user_level == "PHD":
#         return """ Keep you vocabulary advanced and very hard like your are talking to a PHD level peron """
def my_dynamic_instructions(
    """
    """
)

blog_agent = Agent (
    name= "Blog website agent",
    instructions = ""
)