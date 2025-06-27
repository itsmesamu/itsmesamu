import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# GPT-2 Modell und Tokenizer laden
model_name = "gpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

# Modell in den Evaluierungsmodus setzen (kein Training nötig)
model.eval()

def generate_text(prompt, max_length=128, temperature=0.5):

    # Eingabetext in Token umwandeln
    input_ids = tokenizer.encode(prompt, return_tensors="pt")

    # Modell mit Sampling verwenden
    output = model.generate(
        input_ids, 
        max_length=max_length, 
        temperature=temperature,  # Kreativität des Outputs
        top_k=22,  # Reduziert Unsinn durch Begrenzung der Wahrscheinlichkeiten
        top_p=1,  # Kontrolliert Varianz
        do_sample=True  # Sampling anstatt Greedy Decoding
    )

    # Dekodieren und zurückgeben
    return tokenizer.decode(output[0], skip_special_tokens=True)

# Beispielaufruf
prompt = "What do you think about chiaretta?"
generated_text = generate_text(prompt)
print(generated_text)