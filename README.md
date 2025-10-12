---
title: Quantized_lang._Translator
app_file: app.py
sdk: gradio
sdk_version: 5.48.0
---

# NLLB-FB Language Translator (Apple Silicon Optimized)

This project is a fork of [Rohan Bagulwar’s Quantized Language Translator](https://huggingface.co/spaces/RohanAi/Quantized_lang._Translator), originally designed for quantized CPU usage.

This modified version has been updated to run efficiently on **Apple Silicon Macs (M1/M2/M4)** using **MPS (Metal Performance Shaders)** for GPU acceleration, and no longer relies on CUDA or quantization.

---

## 🔧 Key Changes

- ✅ Removed `bitsandbytes` and 8-bit quantization (not compatible with macOS).
- ✅ Switched to Apple's MPS backend for GPU acceleration on Mac.
- ✅ Compatible with MacBook Air/Pro (M1/M2/M3/M4).
- ✅ Updated `app.py` and `requirements.txt` to reflect Apple Silicon optimizations.

---

## 🚀 Features

- **Apple Silicon Optimized:** Runs on Mac GPU using PyTorch MPS backend.
- **Multi-language Support:** Translate between many language pairs using NLLB.
- **Fast Inference on Mac:** Leveraging the GPU gives significant speedup over CPU.
- **Gradio Interface:** Easy-to-use web UI for testing and demo.

---

## ✅ Setup Instructions

### 1. Clone the repository

    git clone https://github.com/your-username/nllb_quantized_lang_translator.git
    cd nllb_quantized_lang_translator

### 2. Create and activate a virtual environment
    python3 -m venv myenv
    source myenv/bin/activate
    
### 3. Install dependencies
    pip install -r requirements.txt
    
Make sure you're using Python ≥3.8 and a recent version of pip.
    
### 4. Run the Gradio app:
    python app.py

## 🌍 Supported Languages
Languages include (but are not limited to):
- Tamil 🇮🇳
- Hindi 🇮🇳
- French 🇫🇷
- Spanish 🇪🇸
- German 🇩🇪
- Arabic 🇸🇦

More languages can be added using the FLORES-200 codes.

## References
 - [Original Hugging Face Space by RohanAi](https://github.com/Rohanbagulwar/nllb_quantized_lang_translator/)
- [NLLB: No Language Left Behind (Meta AI)](https://ai.facebook.com/research/no-language-left-behind/)
- [Hugging Face Transformers Documentation](https://huggingface.co/docs/transformers/model_doc/nllb)
- [PyTorch MPS Documentation](https://docs.pytorch.org/docs/stable/notes/mps.html)

 ## Acknowledgements
 Thanks to Rohan Bagulwar for the original implementation and to the Hugging Face and Meta AI teams for their amazing models and tooling.
