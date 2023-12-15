import os
from typing import List, Optional

from llama_index.llms import OpenLLM, OpenLLMAPI
from llama_index.llms import ChatMessage

os.environ[
    "OPENLLM_ENDPOINT"
] = "na"  # Change this to a remote server that you might run OpenLLM at.
# This uses https://huggingface.co/HuggingFaceH4/zephyr-7b-alpha
# downloaded (if first invocation) to the local Hugging Face model cache,
# and actually runs the model on your local machine's hardware
local_llm = OpenLLM("HuggingFaceH4/zephyr-7b-alpha")

# This will use the model running on the server at localhost:3000
remote_llm = OpenLLMAPI(address="http://localhost:3000", backend="local")

# Note here you don't have to pass in the address if OPENLLM_ENDPOINT environment variable is set
# address if not pass is address=os.getenv("OPENLLM_ENDPOINT")
remote_llm = OpenLLMAPI()
completion_response = remote_llm.complete("To infinity, and")
print(completion_response)
