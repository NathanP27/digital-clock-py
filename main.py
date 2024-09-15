import tkinter as tk
from tkinter import ttk
from time import strftime
import pytz
from datetime import datetime

# Initializing the tkinter window
window = tk.Tk()
window.title("Digital Clock")
window.geometry("600x250")  # Set the window size
window.configure(bg='white')  # Set background to black
window.resizable(False, False)  # Non-resizable window size

# Set the timezone to GMT+8 (Philippine Standard Time)
timezone = pytz.timezone('Asia/Manila')

# Function to fetch and update the current time and date
def update_time():
    current_time = datetime.now(timezone).strftime('%I:%M %p')  # 12-hour format with AM/PM
    current_date = datetime.now(timezone).strftime('%A, %B %d, %Y')  # Date format: Day, Month DD, YYYY
    clock_label.config(text=current_time)  # Update time on label
    date_label.config(text=current_date)   # Update date on label
    clock_label.after(1000, update_time)   # Refresh every 1 second

date_label = ttk.Label(window, font=('Helvetica', 20, 'bold'), 
                       background='white', foreground='black')

clock_label = ttk.Label(window, font=('Helvetica', 70, 'bold'), 
                        background='white', foreground='black')

# Positioning the date at the top and time in the center of the window
date_label.pack(anchor='n', pady=(50, 0))
clock_label.pack(anchor='center')

update_time()
window.mainloop()