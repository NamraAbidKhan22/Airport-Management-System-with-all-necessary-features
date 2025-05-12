import tkinter as tk
from tkinter import messagebox, simpledialog

# Flight information
flights = {
    "MH370": {"time": "10:10", "destination": "Karachi", "status": "Delayed"},
    "KI784": {"time": "1:20", "destination": "Lahore", "status": "Delayed"},
    "AI169": {"time": "11:30", "destination": "Islamabad", "status": "Cancelled"},
    "BA256": {"time": "14:45", "destination": "Rohri", "status": "On Time"},
    "QR912": {"time": "16:00", "destination": "Dukkur", "status": "Delayed"},
    "EK205": {"time": "19:30", "destination": "UK UMER KOT", "status": "On Time"},
    "AF124": {"time": "08:50", "destination": "Paris", "status": "Cancelled"},
    "SQ318": {"time": "12:15", "destination": "Singapore", "status": "On Time"},
    "DL178": {"time": "23:10", "destination": "New York", "status": "Delayed"},
    "QF407": {"time": "05:30", "destination": "Sydney", "status": "On Time"}
}

# Search for flight details
def search_flight():
    name = name_entry.get()
    flight_number = flight_entry.get()
    seat_number = seat_entry.get()

    if flight_number in flights:
        flight = flights[flight_number]
        messagebox.showinfo(
            "Flight Details",
            f"Passenger Name: {name}\n"
            f"Flight Number: {flight_number}\n"
            f"Seat Number: {seat_number}\n"
            f"Time: {flight['time']}\n"
            f"Destination: {flight['destination']}\n"
            f"Status: {flight['status']}"
        )
    else:
        messagebox.showerror("Error", "Flight not found!")

# View all available flights
def view_all_flights():
    all_flights = "\n".join(
        f"{key}: {value['destination']} at {value['time']} - {value['status']}"
        for key, value in flights.items()
    )
    messagebox.showinfo("All Flights", all_flights)

# Reset the form
def reset_fields():
    name_entry.delete(0, tk.END)
    flight_entry.delete(0, tk.END)
    seat_entry.delete(0, tk.END)

# Update flight status
def update_flight_status():
    flight_number = simpledialog.askstring("Update Status", "Enter flight number:")
    if flight_number in flights:
        new_status = simpledialog.askstring("New Status", "Enter new flight status (On Time, Delayed, Cancelled):")
        flights[flight_number]['status'] = new_status
        messagebox.showinfo("Status Updated", f"Flight {flight_number} status updated to {new_status}.")
    else:
        messagebox.showerror("Error", "Flight not found!")

# Add a new flight
def add_flight():
    flight_number = simpledialog.askstring("Add Flight", "Enter new flight number:")
    if flight_number in flights:
        messagebox.showerror("Error", "Flight already exists!")
        return
    time = simpledialog.askstring("Add Flight", "Enter flight time (HH:MM):")
    destination = simpledialog.askstring("Add Flight", "Enter destination:")
    status = simpledialog.askstring("Add Flight", "Enter flight status (On Time, Delayed, Cancelled):")

    flights[flight_number] = {
        "time": time,
        "destination": destination,
        "status": status
    }
    messagebox.showinfo("Flight Added", f"Flight {flight_number} to {destination} at {time} added.")

# Main window
def view_flights():
    window = tk.Tk()
    window.title("Flight Management System")

    tk.Label(window, text="Flight Management System", font=("Arial", 16, "bold")).grid(row=0, column=0, columnspan=3, pady=10)

    tk.Label(window, text="Name:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
    global name_entry
    name_entry = tk.Entry(window)
    name_entry.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(window, text="Flight Number:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
    global flight_entry
    flight_entry = tk.Entry(window)
    flight_entry.grid(row=2, column=1, padx=5, pady=5)

    tk.Label(window, text="Seat Number:").grid(row=3, column=0, sticky="e", padx=5, pady=5)
    global seat_entry
    seat_entry = tk.Entry(window)
    seat_entry.grid(row=3, column=1, padx=5, pady=5)

    # Buttons
    tk.Button(window, text="Search", command=search_flight).grid(row=4, column=0, pady=10)
    tk.Button(window, text="Reset", command=reset_fields).grid(row=4, column=1, pady=10)
    tk.Button(window, text="View All Flights", command=view_all_flights).grid(row=5, column=0, pady=10)
    tk.Button(window, text="Update Status", command=update_flight_status).grid(row=5, column=1, pady=10)
    tk.Button(window, text="Add New Flight", command=add_flight).grid(row=6, column=0, pady=10)
    tk.Button(window, text="Close", command=window.destroy).grid(row=6, column=1, pady=10)

    window.mainloop()

view_flights()