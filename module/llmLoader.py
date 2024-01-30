from openai import OpenAI
import json
from treelib import Tree
from pdfLoader import pdfReader

with open('out.json','r') as f:
    data = json.load(f)
    f.close()
tree = Tree.from_map(child_parent_dict=data)
print(tree)
'''
context = '1'
client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key="sk-M2zfKQU0xM5fkCj8E71562WDkTY43ZlnGhh5lvpjkIBAmz7Q",
    base_url="https://api.chatanywhere.tech/v1"
    # base_url="https://api.chatanywhere.cn/v1"
)

task_prompt = """You are a Named Entity Recognition Model.
Now I will give you a sentence and you will have to recognize the named entities in the sentence and output them in the list format.
The list format is as follows: ["entity1":"entity_type1"], ["entity2":"entity_type2"]... in which entity_type is the entity type.
IF there is no entity in the sentence, you will have to output: []."""

instance_message = """"""
entity_types = ''

input_message = """Now, recognize the named entities in the given sentence and output them in the list format. 
Stress once again DO NOT output other text than the list format.
sentence: {context}
entity types: {entity_types}
Named Entity Recognition output: """

system_prompt = task_prompt + instance_message
messages=[{"role": "system", "content": system_prompt},
            {"role": "user", "content": input_message}]
response = client.completions.create(prompt=messages, temperature=0.1)
'''