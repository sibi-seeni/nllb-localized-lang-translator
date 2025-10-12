from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from sacremoses import MosesPunctNormalizer
from flores import code_mapping
import gradio as gr
import torch

# Use MPS (Metal GPU on Apple Silicon) if available
device = "mps" if torch.backends.mps.is_available() else "cpu"
print("Using device:", device)

MODEL_DIR = "RohanAi/nllb_quantized"

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained(MODEL_DIR)

# Load model and move to selected device (MPS or CPU)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_DIR).to(device)

punct_normalizer = MosesPunctNormalizer(lang="en")

# Language mapping
langs = {
    "Tamil": "tam_Taml",
    "Hindi": "hin_Deva",
    "French": "fra_Latn",
    "Spanish": "spa_Latn",
    "German": "deu_Latn",
    "Arabic": "arb_Arab"
}

def translate(text: str, src_lang: str, tgt_lang: str):
    src_code = code_mapping[src_lang]
    tgt_code = code_mapping[tgt_lang]
    print("Source lang code:", src_code, "| Target lang code:", tgt_code)

    tokenizer.src_lang = src_code
    tokenizer.tgt_lang = tgt_code

    # Normalize punctuation
    text = punct_normalizer.normalize(text)

    # Encode input and move to device
    inputs = tokenizer(text, return_tensors="pt").to(device)

    # Generate translation
    outputs = model.generate(
        **inputs,
        forced_bos_token_id=tokenizer.convert_tokens_to_ids(tgt_code),
        num_beams=3,
        no_repeat_ngram_size=2,
    )

    # Decode output
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

langs = list(code_mapping.keys())

iface = gr.Interface(
    fn=translate,
    inputs=[
        gr.Textbox(lines=10, label="Input Text"),
        gr.Dropdown(langs, label="Source Language"),
        gr.Dropdown(langs, label="Target Language")
    ],
    outputs=gr.Textbox(lines=30, label="Translated Text"),
    title="🌍 Language Translation (Apple MPS Optimized)"
)

iface.launch(share=True)
