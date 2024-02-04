import joblib
import numpy as np
import tkinter as tk

# Load the model
model_loaded = joblib.load('./Model/model_updated.joblib')
print("Model loaded")

# Function to make a prediction
def make_prediction():
    # Get input values from the Entry widgets
    cores_val = float(entry1.get())
    threads_val = float(entry2.get())
    lithography_val = float(entry3.get())
    max_turbo_freq_val = float(entry4.get())
    tdpw_val = float(entry5.get())
    cache_val = float(entry6.get())

    # Create test data
    test_data = [[cores_val, threads_val, lithography_val, max_turbo_freq_val, tdpw_val, cache_val]]

    # Predict
    prediction = model_loaded.predict(test_data)

    # Round the prediction
    rounded_number = np.round(prediction, 2)

    # Display the prediction
    result_label.config(text=f"Predicted Base Freq GHz: {rounded_number[0]}")

# Create the main Tkinter window
# order: 'Cores', 'Threads', 'Lithography(nm)', 'Max. Turbo Freq.(GHz)', 'TDP(W)', 'Cache(MB)'
root = tk.Tk()
root.title("Predict base frequency of CPU's")
root.title("Must use . instead of ,")

# Create and place the first Entry widget
cores_label = tk.Label(root, text="Cores")
cores_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.E)

entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=10, pady=5)

# Create and place the second Entry widget
entry2_label = tk.Label(root, text="Threads")
entry2_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)

entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=10, pady=5)

# Repeat the process for the next 4 Entry widgets
entry3_label = tk.Label(root, text="Lithography(nm)")
entry3_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.E)

entry3 = tk.Entry(root)
entry3.grid(row=2, column=1, padx=10, pady=5)

entry4_label = tk.Label(root, text="Max Turbo Freq(GHZ)")
entry4_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.E)

entry4 = tk.Entry(root)
entry4.grid(row=3, column=1, padx=10, pady=5)

entry5_label = tk.Label(root, text="TDP(W)")
entry5_label.grid(row=4, column=0, padx=10, pady=5, sticky=tk.E)

entry5 = tk.Entry(root)
entry5.grid(row=4, column=1, padx=10, pady=5)

entry6_label = tk.Label(root, text="Cache(MB)")
entry6_label.grid(row=5, column=0, padx=10, pady=5, sticky=tk.E)

entry6 = tk.Entry(root)
entry6.grid(row=5, column=1, padx=10, pady=5)

# Create a button to make a prediction
predict_button = tk.Button(root, text="Make Prediction", command=make_prediction)
predict_button.grid(row=6, column=1, pady=10)

# Label to display the prediction result
result_label = tk.Label(root, text="")
result_label.grid(row=7, column=1, pady=10)

# Start the Tkinter event loop
root.mainloop()

#couple of issues the model is very VERY overfitted 
# secondly it uses entries that doesnt actually affect the final result all the much
#thirdly it hasnt been cleaned and optimized
#originally this was a jupyter notebook project with graphs and preparation for optimisation but i just haven't gotten around to it