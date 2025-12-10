learning_rate = 0.01
batch_size = 64
epochs = 100
dropout = 0.5

if 0 < learning_rate <= 1:
    print("learning_rate: OK")

if batch_size > 0 and (batch_size & (batch_size - 1)) == 0:
    print("batch_size: OK")

if 0 < epochs < 1000:
    print("epochs: OK")

if 0 <= dropout <= 1:
    print("dropout: OK")
