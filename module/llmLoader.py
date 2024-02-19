from llama_index.llms import OpenAI
import json
from typing import *
from treelib import Tree
from pdfLoader import pdfReader

client = OpenAI(
    model="",
    api_key="sk-M2zfKQU0xM5fkCj8E71562WDkTY43ZlnGhh5lvpjkIBAmz7Q",
    system_prompt=""
)

class nerPrompt():
    task_prompt = f"""You are a Named Entity Recognition Model.
    Now I will give you a sentence and you will have to recognize the named entities in the sentence and output them in the list format.
    The list format is as follows: ["entity1":"entity_type1"], ["entity2":"entity_type2"]... in which entity_type is the entity type.
    IF there is no entity in the sentence, you will have to output: []."""

    instance_message = """"""

    def __init__(self, entity_types:list ) -> None:
        self.entity_types = str(entity_types)

    def set_context(self, context:str):
        self.context = context

    def set_entity_types(self, entity_types:list):
        self.entity_types = str(entity_types)
    
    def set_instance_message(self, instance_message:str):
        self.instance_message = instance_message

    @property
    def system_prompt(self) -> str:
        return self.task_prompt + self.instance_message
    
    @property
    def input_message(self) -> str:
        input_message =  f"""Now, recognize the named entities in the given sentence and output them in the list format. 
        Stress once again DO NOT output other text than the list format.
        sentence: {self.context}
        entity types: {self.entity_types}
        Named Entity Recognition output: """
        return input_message

    @property
    def messages(self) -> List[Dict[str, str]]:
        return [{"role": "system", "content": self.system_prompt},
                {"role": "user", "content": self.input_message}]

if __name__ == "__main__":
    pdf = pdfReader(
        "document/Digital Image Processing (Rafael C. Gonzalez, Richard E. Woods) (Z-Library).pdf"
    )
    tree = pdf.tree_spliter()
    leaf = tree.leaves()
    data = [leaf.data for leaf in tree.leaves()]

