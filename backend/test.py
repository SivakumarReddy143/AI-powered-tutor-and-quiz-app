from ai_engine import get_llm,generate_quiz

llm=get_llm()
print(llm.invoke("hlo"))
subject=input("enter subject::")
level=input("enter level::")
response=generate_quiz(subject,level)
print(response)