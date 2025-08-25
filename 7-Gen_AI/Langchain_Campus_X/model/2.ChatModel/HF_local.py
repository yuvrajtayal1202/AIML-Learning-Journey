from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

# from dotenv import load_dotenv
# import os

# load_dotenv()
# api_key = os.getenv("HF_TOKEN")

llm = HuggingFacePipeline.from_model_id(
    model_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation",
    # huggingfacehub_api_token=api_key
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_tokens=100
    )
)

model = ChatHuggingFace(llm=llm)

response = model.invoke("What is the capital of India?")
print(response.content)
