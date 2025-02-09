from datasets import load_dataset

# Lade den eigenen Datensatz
dataset = load_dataset("text", data_files={"train": "Training ki.txt"})

from transformers import GPT2Tokenizer, GPT2LMHeadModel

# Modell und Tokenizer laden (GPT-2 Basisversion)
model_name = "gpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

def tokenize_function(examples):
    return tokenizer(examples["text"], truncation=True, padding="max_length", max_length=512)

# Tokenisierung des gesamten Datensatzes
tokenized_datasets = dataset.map(tokenize_function, batched=True)

import torch

# Konvertiere die Token in PyTorch-Tensoren
tokenized_datasets.set_format(type="torch", columns=["input_ids", "attention_mask"])
train_dataset = tokenized_datasets["train"]

from transformers import Trainer, TrainingArguments

# Definiere die Trainingsparameter
training_args = TrainingArguments(
    output_dir="./gpt2_finetuned",  # Speicherort der Modelle
    evaluation_strategy="epoch",
    save_strategy="epoch",
    per_device_train_batch_size=4,  # Anzahl der Sätze pro Batch (RAM abhängig)
    num_train_epochs=3,  # Anzahl der Durchläufe über den Datensatz
    save_total_limit=2,  # Speichert nur die letzten zwei Modelle
    learning_rate=5e-5,  # Standard-Lernrate für Feintuning
    weight_decay=0.01,  # Regularisierung gegen Overfitting
)

# Erstelle den Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
)

# Training starten
trainer.train()

model.save_pretrained("./gpt2_finetuned")
tokenizer.save_pretrained("./gpt2_finetuned")