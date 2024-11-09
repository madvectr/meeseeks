from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
import dotenv

dotenv.load_dotenv()

chat = ChatOpenAI(model="gpt-4o", temperature=1.0)

def cover_letter(job_description: str) -> str:
  """Generate a cover letter for a given job description."""

  with open("prompts/application_one_shot.txt", "r") as file:
    prompt_text = file.read()

  prompt = ChatPromptTemplate.from_template(prompt_text)

  chain = prompt | chat

  return chain.invoke({"job_description": job_description})

def get_job_description() -> str:
  """Get the job description for a given job id."""

  with open("../input/job_description.txt", "r") as file:
    return file.read()

if __name__ == "__main__":
  job_description = get_job_description()
  cover_letter = cover_letter(job_description)
  print("--------------------------------")
  print("Job Description:")
  print(job_description)
  print("--------------------------------")
  print("Cover Letter:")
  print(cover_letter)
  print("--------------------------------")
