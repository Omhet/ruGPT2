import youtokentome as yttm

train_data_path = "input.txt"
model_path = "example.model"

# Training model
yttm.BPE.train(data=train_data_path, vocab_size=50000, model=model_path)

# Loading model
# bpe = yttm.BPE(model=model_path)
