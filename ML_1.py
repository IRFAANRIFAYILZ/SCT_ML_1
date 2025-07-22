import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import pandas as pd

# Sample dataset
data = {
    'SquareFootage': [1000, 1500, 2000, 2500, 3000],
    'Bedrooms': [2, 3, 3, 4, 4],
    'Bathrooms': [1, 2, 2, 3, 3],
    'Price': [200000, 300000, 400000, 500000, 600000]
}
df = pd.DataFrame(data)

# Train model
X = df[['SquareFootage', 'Bedrooms', 'Bathrooms']]
y = df['Price']
model = LinearRegression()
model.fit(X, y)

# GUI
root = tk.Tk()
root.title("House Price Predictor")
root.geometry("900x900")
root.configure(bg="#f0f8ff")

big_font = ("Helvetica", 20)

# Title Label
title_label = tk.Label(root, text="House Price Predictor", font=("Helvetica", 20, "bold"), bg="#f0f8ff", fg="#2f4f4f")
title_label.pack(pady=10)

# Entry Fields Frame
frame = tk.Frame(root, bg="#f0f8ff")
frame.pack()

tk.Label(frame, text="Square Footage:", bg="#f0f8ff", font=big_font).grid(row=0, column=0, padx=10, pady=5, sticky="w")
sqft_entry = tk.Entry(frame, font=big_font, width=28)
sqft_entry.grid(row=0, column=1)

tk.Label(frame, text="Bedrooms:", bg="#f0f8ff", font=big_font).grid(row=1, column=0, padx=10, pady=5, sticky="w")
bed_entry = tk.Entry(frame, font=big_font, width=28)
bed_entry.grid(row=1, column=1)

tk.Label(frame, text="Bathrooms:", bg="#f0f8ff", font=big_font).grid(row=2, column=0, padx=10, pady=5, sticky="w")
bath_entry = tk.Entry(frame, font=big_font, width=28)
bath_entry.grid(row=2, column=1)

# Result Label
result_label = tk.Label(root, text="", font=("Helvetica", 20), bg="#f0f8ff", fg="green")
result_label.pack(pady=10)

# Plot area
fig, ax = plt.subplots(figsize=(5, 3))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(pady=10)

# Prediction Function
def predict_price():
    try:
        sqft = int(sqft_entry.get())
        bed = int(bed_entry.get())
        bath = int(bath_entry.get())
        new_data = [[sqft, bed, bath]]
        prediction = model.predict(new_data)[0]
        result_label.config(text=f"Predicted Price: ₹{int(prediction):,}", fg="green")

        # Plotting
        ax.clear()
        ax.scatter(df['SquareFootage'], df['Price'], color='blue', label="Original Data")
        ax.scatter(sqft, prediction, color='red', label="Prediction")
        ax.set_title("SquareFootage vs Price")
        ax.set_xlabel("Square Footage")
        ax.set_ylabel("Price")
        ax.legend()
        canvas.draw()
    except ValueError:
        result_label.config(text="Please enter valid numbers!", fg="red")

# Clear Function
def clear_all():
    sqft_entry.delete(0, tk.END)
    bed_entry.delete(0, tk.END)
    bath_entry.delete(0, tk.END)
    result_label.config(text="")
    ax.clear()
    canvas.draw()

# Buttons
btn_frame = tk.Frame(root, bg="#f0f8ff")
btn_frame.pack(pady=10)

predict_btn = tk.Button(btn_frame, text="Predict", command=predict_price, bg="#4682b4", fg="white", padx=10, pady=5, font=big_font)
predict_btn.grid(row=0, column=0, padx=10)

clear_btn = tk.Button(btn_frame, text="Clear", command=clear_all, bg="#cd5c5c", fg="white", padx=10, pady=5, font=big_font)
clear_btn.grid(row=0, column=1, padx=10)

root.mainloop()
