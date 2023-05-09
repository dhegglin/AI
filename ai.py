from llama_index import SimpleDirectoryReader, GPTListIndex, GPTVectorStoreIndex, LLMPredictor, PromptHelper, StorageContext, load_index_from_storage, ServiceContext
from langchain.chat_models import ChatOpenAI
import gradio as gr
import sys
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--train', action='store_true')
parser.add_argument('ip')
args = parser.parse_args()

os.environ["OPENAI_API_KEY"] = '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'

def construct_index(directory_path):
    max_input_size = 4096
    num_outputs = 512
    max_chunk_overlap = 20
    chunk_size_limit = 600

    prompt_helper = PromptHelper(max_input_size, num_outputs, max_chunk_overlap, chunk_size_limit=chunk_size_limit)

    llm_predictor = LLMPredictor(llm=ChatOpenAI(temperature=0.7, model_name="gpt-3.5-turbo", max_tokens=num_outputs))

    service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor, prompt_helper=prompt_helper)
    documents = SimpleDirectoryReader(directory_path).load_data()
    index = GPTVectorStoreIndex.from_documents(documents, service_context=service_context)
    #index = GPTVectorStoreIndex(documents, llm_predictor=llm_predictor, prompt_helper=prompt_helper)

    index.storage_context.persist()
    #index.save_to_disk('index.json')

    return index

def chatbot(input_text):
    storage_context = StorageContext.from_defaults(persist_dir='./storage')
    index = load_index_from_storage(storage_context)
    #index = GPTVectorStoreIndex.load_from_disk('index.json')
    query_engine = index.as_query_engine()
    response = query_engine.query(input_text)
    #response = index.query(input_text, response_mode="compact")
    return response.response

iface = gr.Interface(fn=chatbot,
                     inputs=gr.components.Textbox(label="Ask me a question on any security control"),
                     outputs=gr.components.Textbox(label="Here's what I know:"),
                     title="Security Controls Chatbot")

if (args.train):
    index = construct_index("docs")
#iface.launch(share=True, server_name="10.0.0.181", server_port=7860)
iface.launch(share=True, server_name=args.ip, server_port=7860)
