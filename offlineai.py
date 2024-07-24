import tkinter as tk
from tkinter import messagebox, scrolledtext
from llama_cpp import Llama
import threading
import sys
import ctypes
import os
import ctypes.util
import tempfile
import shutil
import getpass
from pathlib import Path
import io

username = getpass.getuser()

script_dir = os.path.dirname(os.path.abspath(__file__))

# List of models
models = ["Phi-3-mini-4k-instruct.Q4_0.gguf", "Phi-3-mini-4k-instruct.Q4_0.gguf"]

global model
model = Llama(
  model_path=os.path.join(script_dir, "Phi-3-mini-4k-instruct.Q4_0.gguf"),  # path to GGUF file
  n_ctx=4096,  # The max sequence length to use - note that longer sequence lengths require much more resources
  n_threads=8, # The number of CPU threads to use, tailor to your system and the resulting performance
  n_gpu_layers=35, # The number of layers to offload to GPU, if you have GPU acceleration available. Set to 0 if no GPU acceleration is available on your system.
  verbose=False  # Suppress timing information
)

print("-------------------------------------")
print("Loading the model. please wait...")
print("============================================================")
print("Welcome to the Offline AI assistant!")
print("============================================================")
print("Created by: Corvus Codex")
print("Github: https://github.com/CorvusCodex/")
print("Licence : MIT License")
print("Support my work:")
print("BTC: bc1q7wth254atug2p4v9j3krk9kauc0ehys2u8tgg3")
print("ETH & BNB: 0x68B6D33Ad1A3e0aFaDA60d6ADf8594601BE492F0")
print("Buy me a coffee: https://www.buymeacoffee.com/CorvusCodex")
print("============================================================")


def change_model(*args):
    global model
    print("OfflineAi: Loading model...\n")
    # Load the model in a separate thread to avoid freezing the GUI
    threading.Thread(target=load_model, args=(var.get(),), daemon=True).start()

model_path = Path(script_dir)


def load_model(model_name):
    global model
    model = Llama(
      model_path=os.path.join(script_dir, model_name),  
      n_ctx=int(n_ctx_entry.get()),  
      n_threads=int(n_threads_entry.get()),
      n_gpu_layers=int(n_gpu_layers_entry.get()), 
      verbose=False  # Suppress timing information
    )
    print("OfflineAi: Model loaded.\n")

def generate_response(question):
    timing_output = io.StringIO()
    sys.stderr = timing_output

    # Generate the response
    output = model(
      f"<|user|>\n{question}<|end|>\n<|assistant|>",  # Add the user and assistant tags
      max_tokens=256,  # Generate up to 256 tokens
      stop=["<|end|>"], 
      echo=False,  # Don't echo the prompt
    )

    sys.stderr = sys.__stderr__

    print("-" * 40 + "\n")

    print("OfflineAi: " + output['choices'][0]['text'] + "\n")

    print("-" * 40 + "\n")

def clear_chat():
    print("Chat cleared.\n")


while True:
    user_input = input("User: ")
    if user_input.lower() == "exit":
        break
    generate_response(user_input)
