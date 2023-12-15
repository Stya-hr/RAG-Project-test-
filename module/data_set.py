import os
from llama_index import SimpleDirectoryReader
from llama_index.node_parser import SimpleNodeParser
from llama_index.llms import HuggingFaceInferenceAPI
from llama_index.finetuning import (
    generate_qa_embedding_pairs,
    EmbeddingQAFinetuneDataset,
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

HF_TOKEN = "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"
remote_llm = HuggingFaceInferenceAPI(
    model_name="intfloat/multilingual-e5-large",
    token=HF_TOKEN
)

train_dataset = generate_qa_embedding_pairs(train_nodes, llm=remote_llm)
val_dataset = generate_qa_embedding_pairs(val_nodes, llm=remote_llm)

train_dataset.save_json("train_dataset.json")
val_dataset.save_json("val_dataset.json")

train_dataset = EmbeddingQAFinetuneDataset.from_json("train_dataset.json")
val_dataset = EmbeddingQAFinetuneDataset.from_json("val_dataset.json")
