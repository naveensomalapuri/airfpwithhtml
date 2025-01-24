from pydantic import BaseModel, Field

# Define the data structure for the RICEF form output.
class AIFS(BaseModel):
    project_name: str = Field(description="Extracted project name")
    RICEF_id: str = Field(description="Generated or extracted RICEF ID")
    client_name: str = Field(description="Extracted client name")
    
    # Voice of Customer Section
    Voice_Of_Customer_WHAT_Functional_Description: str = Field(
        description="Generate a client-centered question about the essential functions and capabilities required of the AI solution, addressing what the AI should specifically accomplish to solve their business problem. For example, 'What are the essential functions and capabilities this AI solution should have to effectively address our business problem?'"
    )
    Voice_Of_Customer_WHY_Business_Benefit_Need: str = Field(
        description="Generate a question asking why this AI solution is necessary and what specific business benefits it provides. The question should clarify the value and the risk of not implementing it. For example, 'What business benefits will this solution provide, and what risks or inefficiencies might arise if this solution is not in place?'"
    )
    Voice_Of_Customer_WHO_WHERE: str = Field(
        description="Generate a question identifying the primary users of the AI solution within the organization, including departments, teams, or roles. For example, 'Who will be the primary users of this solution, and which departments or organizational units will benefit the most?'"
    )
    Voice_Of_Customer_WHEN: str = Field(
        description="Generate a question to define how frequently and at what times the solution will be used. For example, 'How often will this solution need to be used, and are there specific times or intervals at which it must operate?'"
    )
    Voice_Of_Customer_HOW_Input: str = Field(
        description="Generate a question that specifies the necessary input data for the AI solution to work effectively. Describe fields, data types, and sources needed. For example, 'What specific data inputs are necessary for this solution, and which fields or data sources are critical for achieving accurate results?'"
    )
    Voice_Of_Customer_HOW_Process: str = Field(
        description="Generate a question to clarify how the AI solution should process the input data, covering operations, analyses, or functional steps. For example, 'What specific processes, analyses, or computations should the AI solution perform on the input data to produce meaningful results?'"
    )
    Voice_Of_Customer_HOW_Output: str = Field(
        description="Generate a question about the expected format and presentation of the AI solution’s output, ensuring it’s useful to stakeholders. For example, 'What should the final output look like, and how should it be formatted or presented to best support our decision-making needs?'"
    )

    
    # Response of Consultant Section
    # Consultant_Response_Agreed_Upon_Approach: str = Field(description="Generated or extracted agreed-upon approach selected by consultant")
    # Consultant_Response_Functional_Description: str = Field(description="Generated or extracted functional description provided by consultant")
    # Consultant_Response_Business_Benefit_Need: str = Field(description="Generated or extracted description of business need or benefit according to the consultant")
    # Consultant_Response_Important_Assumptions: str = Field(description="Generated or extracted important assumptions considered by the consultant")
    # Consultant_Response_Additional_Comments: str = Field(description="Additional comments provided by the consultant during the decision-making process")
    
    # Functional Design Section
    Functional_Design_Process: str = Field(description="Generated or extracted process flow for the functional design")
    Functional_Design_Interface_Direction: str = Field(description="Direction of data flow (to/from or bi-directional with SAP)")
    Functional_Design_Error_Handling: str = Field(description="Generated or extracted error-handling owner definition and business needs")
    Functional_Design_Frequency: str = Field(description="Frequency at which the report will be run")
    Functional_Design_Data_Volume: str = Field(description="Estimated data volume for the report")
    Functional_Design_Security_Requirements: str = Field(description="Security requirements requiring explicit authorization checks or special processing")
    Functional_Design_Data_Sensitivity: str = Field(description="Sensitivity of data, including level of restrictions")
    Functional_Design_Unit_Testing: str = Field(description="Information for unit testing scenarios, instructions, test data, and expected results")
    Functional_Design_Additional_Comments: str = Field(description="Additional information for functional design")
    Functional_Design_Rework_Log: str = Field(description="Rework log containing previous version(s) of the section")
    
    # Technical Design Section
    Technical_Design_Design_Points: str = Field(description="Design points for clear definition, including calculations, formulas, and performance recommendations")
    Technical_Design_Special_Configuration_Settings: str = Field(description="Special configuration settings or temporary prerequisites")
    Technical_Design_Outbound_Definition: str = Field(description="Outbound file(s) structure and format details")
    Technical_Design_Target_Environment: str = Field(description="Target environment where data will be sent and any specific requirements")
    Technical_Design_Starting_Transaction: str = Field(description="Starting transaction or application name")
    Technical_Design_Triggering_Events: str = Field(description="SAP business process event that triggers the report")
    Technical_Design_Data_Transformation_Process: str = Field(description="Data transformation process within SAP or middleware")
    Technical_Design_Data_Transfer_Process: str = Field(description="Description of data transfer process to SAP")
    Technical_Design_Data_Format: str = Field(description="Format of data (XML, EDI, Flat File, etc.)")
    Technical_Design_Error_Handling: str = Field(description="Technical error handling components and owner definition")
    Technical_Design_Additional_Process_Requirements: str = Field(description="Additional process requirements")
    Technical_Design_Inbound_Definition: str = Field(description="Inbound file structure and format")
    Technical_Design_Source_Environment: str = Field(description="Origin of data from an external system")
    Technical_Design_Receiving_Transaction: str = Field(description="Receiving transaction/application, whether it is new or existing")
    Technical_Design_Rework_Log: str = Field(description="Rework log containing previous versions for technical design")
