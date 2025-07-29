from tensorflow.keras.models import load_model

# Load the existing .h5 model
model = load_model("model/wheat_disease_model.h5")

# Save in new .keras format
model.save("model/wheat_disease_model.keras")

print("✅ Model converted and saved as .keras")
