import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from services.jsondatastructure import AIFS

def openmodle(prompt):
    # Load the environment variables from the .env file
    load_dotenv()

    # Retrieve the API key from the environment
    groq_api_key = os.getenv("GROQ_API_KEY")

    # Initialize the Groq chat model with your API key
    model = ChatGroq(model_name="llama-3.1-70b-versatile", groq_api_key=groq_api_key)

    # And a query intented to prompt a language model to populate the data structure.
    business_requirement_query = prompt

    # Set up a parser + inject instructions into the prompt template.
    parser = JsonOutputParser(pydantic_object=AIFS)


    # Define the prompt template with format instructions.
    prompt = PromptTemplate(
        template=(
            "Using the provided client business requirement, generate a RICEF form that fills out the following details:\n\n"
            "{format_instructions}\n\n"
            "- Project Name\n"
            "- RICEF ID\n"
            "- Client Name\n\n"
            
            "- **Voice of Customer Section**:\n"
            "   - WHAT (Functional Description)\n"
            "   - WHY (Business Benefit/Need)\n"
            "   - WHO/WHERE\n"
            "   - WHEN\n"
            "   - HOW - Input\n"
            "   - HOW - Process\n"
            "   - HOW - Output\n"
            "   - Additional Comments\n\n"
            
            "- **Response of Consultant Section**:\n"
            "   - Agreed Upon Approach\n"
            "   - Functional Description\n"
            "   - Business Benefit/Need\n"
            "   - Important Assumptions\n"
            "   - Additional Comments\n\n"
            
            "- **Functional Design Section**:\n"
            "   - Process\n"
            "   - Interface Direction\n"
            "   - Error Handling\n"
            "   - Frequency\n"
            "   - Data Volume\n"
            "   - Security Requirements\n"
            "   - Data Sensitivity\n"
            "   - Unit Testing\n"
            "   - Additional Comments\n"
            "   - Rework Log\n\n"
            
            "- **Technical Design Section**:\n"
            "   - Design Points\n"
            "   - Special Configuration Settings\n"
            "   - Outbound Definition\n"
            "   - Target Environment\n"
            "   - Starting Transaction/Application\n"
            "   - Triggering Events\n"
            "   - Data Transformation Process\n"
            "   - Data Transfer Process\n"
            "   - Data Format\n"
            "   - Error Handling\n"
            "   - Additional Process Requirements\n"
            "   - Inbound Definition\n"
            "   - Source Environment\n"
            "   - Receiving Transaction/Application\n"
            "   - Rework Log\n\n"
            "Client Business Requirement:\n{client_business_requirement}"
        ),
        input_variables=["client_business_requirement"],
        partial_variables={"format_instructions": parser.get_format_instructions()}
    )


    chain = prompt | model | parser

    response = chain.invoke({"client_business_requirement": business_requirement_query})

    return response