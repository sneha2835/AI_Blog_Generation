# backend/api/utils/model_loader.py

import os
from langchain_community.llms import CTransformers
from django.conf import settings

_model_instance = None  # Singleton instance

def load_llama_model():
    global _model_instance
    if _model_instance is not None:
        return _model_instance

    model_path = os.path.abspath(os.path.join(settings.BASE_DIR, "..", "models", "llama-2-7b-chat.Q4_K_M.gguf"))

    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found at {model_path}")

    _model_instance = CTransformers(
        model=model_path,
        model_type="llama",
        config={
            "max_new_tokens": 512,
            "temperature": 0.7,
            "context_length": 1024,
            "threads": 6  # Adjust based on your CPU (you can go 4–8)
        }
    )
    return _model_instance
