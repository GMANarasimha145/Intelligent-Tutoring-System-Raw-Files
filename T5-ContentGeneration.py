from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

def text_generator(my_text):
    print(1111)
    # Load or download the model and tokenizer
    model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-large")
    tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-large")
    print(1)

    # Tokenize the input text and generate output
    inputs = tokenizer(my_text, return_tensors="pt")
    outputs = model.generate(**inputs, \
                            min_length=256, \
                            max_new_tokens=1024, \
                            length_penalty=0.9, \
                            num_beams=8, \
                            no_repeat_ngram_size=2, \
                            early_stopping=True)
    
    # Decode the generated output and return
    output_text_Flan_t5 = tokenizer.batch_decode(outputs,\
                                                skip_special_tokens=True)
    return output_text_Flan_t5

# Example usage
input_text = "Explain about Cyber Security"
output_text = text_generator(input_text)
print(output_text)
