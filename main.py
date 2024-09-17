import argparse
import json
from utils import process_pdf
import openai
from config import OPENAI_API_KEY
from datetime import datetime
from langchain_openai import ChatOpenAI
from langchain.chains.question_answering import load_qa_chain
import warnings
warnings.filterwarnings("ignore")

openai.api_key = OPENAI_API_KEY





class Main:
    def __init__(self):
        """An instance of the Main class is created"""
        parser = argparse.ArgumentParser(description="RAG CLI Application")
        parser.add_argument("pdf_path", type=str, help="Path to the PDF file")
        parser.add_argument("questions", type=str, nargs='+', help="Questions to answer")
        args = parser.parse_args()
        self.vectordb = process_pdf(args.pdf_path)
        self.questions = args.questions
        self.rag()
        
    
    def rag(self):
        """The rag method is called"""
        results = {}
        chain = self.create_agent_chain()
        for question in self.questions:
            matching_docs = self.vectordb.similarity_search(question, k=3)
            answer = chain.run(input_documents=matching_docs, question=question)
            results[question] = answer
        # Print results
        print(json.dumps(results, indent=4))
        # Save results to a JSON file
        with open("results.json", "w") as f:
            json.dump(results, f, indent=4)
            
        
    def create_agent_chain(self):
        model_name = "gpt-3.5-turbo"
        llm = ChatOpenAI(model_name=model_name)
        chain = load_qa_chain(llm, chain_type="stuff")
        return chain


if __name__ == "__main__":
    main = Main()
    