from llama_index.finetuning import (
    generate_qa_embedding_pairs,
    EmbeddingQAFinetuneDataset,
)
from llama_index.llms import OpenAI
from llama_index.node_parser import SimpleNodeParser
from llama_index import SimpleDirectoryReader
import os
from llama_index.llms import HuggingFaceLLM
from llama_index import ServiceContext
import torch
from llama_index.prompts import PromptTemplate

system_prompt = """<|SYSTEM|># StableLM Tuned (Alpha version)
- StableLM is a helpful and harmless open-source AI language model developed by StabilityAI.
- StableLM is excited to be able to help the user, but will refuse to do anything that could be considered harmful to the user.
- StableLM is more than just an information source, StableLM is also able to write poetry, short stories, and make jokes.
- StableLM will refuse to participate in anything that could harm a human.
"""

# This will wrap the default prompts that are internal to llama-index
query_wrapper_prompt = PromptTemplate("<|USER|>{query_str}<|ASSISTANT|>")




llm = HuggingFaceLLM(
    context_window=4096,
    max_new_tokens=256,
    generate_kwargs={"temperature": 0.7, "do_sample": False},
    system_prompt=system_prompt,
    query_wrapper_prompt=query_wrapper_prompt,
    tokenizer_name="StabilityAI/stablelm-tuned-alpha-3b",
    model_name="StabilityAI/stablelm-tuned-alpha-3b",
    device_map="auto",
    stopping_ids=[50278, 50279, 50277, 1, 0],
    tokenizer_kwargs={"max_length": 4096},
    # uncomment this if using CUDA to reduce memory usage
    # model_kwargs={"torch_dtype": torch.float16}
)
llm.float()
service_context = ServiceContext.from_defaults(
    chunk_size=1024,
    llm=llm,
)


def load_corpus(docs, for_training=False, verbose=False):
    """
    Load the corpus of documents.

    Args:
        docs (list): List of documents.
        for_training (bool, optional): Whether the corpus is for training or not. Defaults to False.
        verbose (bool, optional): Whether to show progress or not. Defaults to False.

    Returns:
        list: List of nodes parsed from the documents.
    """
    parser = SimpleNodeParser.from_defaults()
    if for_training:
        nodes = parser.get_nodes_from_documents(
            docs[:90], show_progress=verbose)
    else:
        nodes = parser.get_nodes_from_documents(
            docs[91:], show_progress=verbose)

    if verbose:
        print(f'Parsed {len(nodes)} nodes')

    return nodes


SEC_FILE = ['example.txt']

print(f"Loading files {SEC_FILE}")

reader = SimpleDirectoryReader(input_files=SEC_FILE)
docs = reader.load_data()
print(f'Loaded {len(docs)} docs')

train_nodes = load_corpus(docs, for_training=True, verbose=True)
val_nodes = load_corpus(docs, for_training=False, verbose=True)

# os.environ["OPENAI_API_KEY"] = "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"
# OpenAI.api_key = os.environ["OPENAI_API_KEY"]
# llm = OpenAI(temperature=0.1, model="gpt-3.5-turbo")

train_dataset = generate_qa_embedding_pairs(train_nodes, llm=llm)
val_dataset = generate_qa_embedding_pairs(val_nodes, llm=llm)

train_dataset.save_json("train_dataset.json")
val_dataset.save_json("val_dataset.json")

train_dataset = EmbeddingQAFinetuneDataset.from_json("train_dataset.json")
val_dataset = EmbeddingQAFinetuneDataset.from_json("val_dataset.json")
