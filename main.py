import mysql.connector
import tkinter as tk
from tkinter import messagebox


def connect_to_database():
    username = entry_username.get()
    password = entry_password.get()

    try:
        cnx = mysql.connector.connect(
            host='server.carrotgrx.top',
            port=13306,
            user=username,
            password=password,
            database='text_one'
        )
        messagebox.showinfo('Success', 'Connected to the database')
        open_main_window(cnx)
    except mysql.connector.Error as err:
        messagebox.showerror('Error', f'Failed to connect to the database: {err}')


def open_main_window(cnx):
    login_window.withdraw()

    main_window = tk.Toplevel()
    main_window.title('Main Window')

    def add_data():
        order_id = entry_order_id.get()
        airline = entry_airline.get()
        aircraft_type = entry_aircraft_type.get()
        departure = entry_departure.get()
        arrival = entry_arrival.get()
        departure_airport = entry_departure_airport.get()
        arrival_airport = entry_arrival_airport.get()
        one_way_price = entry_one_way_price.get()
        discount_price = entry_discount_price.get()
        departure_time = entry_departure_time.get()
        arrival_time = entry_arrival_time.get()
        cabin_type = entry_cabin_type.get()

        if (
            order_id and airline and aircraft_type and departure and arrival and departure_airport and arrival_airport and
            one_way_price and discount_price and departure_time and arrival_time and cabin_type
        ):
            try:
                cursor = cnx.cursor()
                query = "INSERT INTO Orders (OrderID, Airline, AircraftType, Departure, Arrival, DepartureAirport, ArrivalAirport, OneWayPrice, DiscountPrice, DepartureTime, ArrivalTime, CabinType) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                values = (
                    order_id, airline, aircraft_type, departure, arrival, departure_airport, arrival_airport,
                    one_way_price, discount_price, departure_time, arrival_time, cabin_type
                )
                cursor.execute(query, values)
                cnx.commit()
                messagebox.showinfo('Success', 'Data added successfully')
                clear_entries()
            except mysql.connector.Error as err:
                messagebox.showerror('Error', f'Failed to add data: {err}')
        else:
            messagebox.showerror('Error', 'Please fill in all fields')

    def delete_data():
        order_id = entry_order_id.get()

        if order_id:
            try:
                cursor = cnx.cursor()
                query = "DELETE FROM Orders WHERE OrderID = %s"
                value = (order_id,)
                cursor.execute(query, value)
                cnx.commit()
                messagebox.showinfo('Success', 'Data deleted successfully')
                clear_entries()
            except mysql.connector.Error as err:
                messagebox.showerror('Error', f'Failed to delete data: {err}')
        else:
            messagebox.showerror('Error', 'Please enter Order ID')

    def update_data():
        order_id = entry_order_id.get()
        airline = entry_airline.get()
        aircraft_type = entry_aircraft_type.get()
        departure = entry_departure.get()
        arrival = entry_arrival.get()
        departure_airport = entry_departure_airport.get()
        arrival_airport = entry_arrival_airport.get()
        one_way_price = entry_one_way_price.get()
        discount_price = entry_discount_price.get()
        departure_time = entry_departure_time.get()
        arrival_time = entry_arrival_time.get()
        cabin_type = entry_cabin_type.get()

        if order_id:
            try:
                cursor = cnx.cursor()
                query = "UPDATE Orders SET Airline = %s, AircraftType = %s, Departure = %s, Arrival = %s, DepartureAirport = %s, ArrivalAirport = %s, OneWayPrice = %s, DiscountPrice = %s, DepartureTime = %s, ArrivalTime = %s, CabinType = %s WHERE OrderID = %s"
                values = (
                    airline, aircraft_type, departure, arrival, departure_airport, arrival_airport, one_way_price,
                    discount_price, departure_time, arrival_time, cabin_type, order_id
                )
                cursor.execute(query, values)
                cnx.commit()
                messagebox.showinfo('Success', 'Data updated successfully')
                clear_entries()
            except mysql.connector.Error as err:
                messagebox.showerror('Error', f'Failed to update data: {err}')
        else:
            messagebox.showerror('Error', 'Please enter Order ID')

    def query_data():
        order_id = entry_order_id.get()

        if order_id:
            try:
                cursor = cnx.cursor()
                query = "SELECT * FROM Orders WHERE OrderID = %s"
                value = (order_id,)
                cursor.execute(query, value)
                result = cursor.fetchone()

                if result:
                    messagebox.showinfo('Query Result',
                                        f'Order ID: {result[0]}\nAirline: {result[1]}\nAircraft Type: {result[2]}\nDeparture: {result[3]}\nArrival: {result[4]}\nDeparture Airport: {result[5]}\nArrival Airport: {result[6]}\nOne-Way Price: {result[7]}\nDiscount Price: {result[8]}\nDeparture Time: {result[9]}\nArrival Time: {result[10]}\nCabin Type: {result[11]}')
                    clear_entries()
                else:
                    messagebox.showinfo('Query Result', 'No data found')
            except mysql.connector.Error as err:
                messagebox.showerror('Error', f'Failed to query data: {err}')
        else:
            messagebox.showerror('Error', 'Please enter Order ID')

    def return_to_login():
        main_window.destroy()
        login_window.deiconify()

    def clear_entries():
        entry_order_id.delete(0, tk.END)
        entry_airline.delete(0, tk.END)
        entry_aircraft_type.delete(0, tk.END)
        entry_departure.delete(0, tk.END)
        entry_arrival.delete(0, tk.END)
        entry_departure_airport.delete(0, tk.END)
        entry_arrival_airport.delete(0, tk.END)
        entry_one_way_price.delete(0, tk.END)
        entry_discount_price.delete(0, tk.END)
        entry_departure_time.delete(0, tk.END)
        entry_arrival_time.delete(0, tk.END)
        entry_cabin_type.delete(0, tk.END)

    label_order_id = tk.Label(main_window, text='Order ID')
    label_order_id.grid(row=0, column=0, padx=10, pady=5)
    entry_order_id = tk.Entry(main_window)
    entry_order_id.grid(row=0, column=1, padx=10, pady=5)

    label_airline = tk.Label(main_window, text='Airline')
    label_airline.grid(row=1, column=0, padx=10, pady=5)
    entry_airline = tk.Entry(main_window)
    entry_airline.grid(row=1, column=1, padx=10, pady=5)

    label_aircraft_type = tk.Label(main_window, text='Aircraft Type')
    label_aircraft_type.grid(row=2, column=0, padx=10, pady=5)
    entry_aircraft_type = tk.Entry(main_window)
    entry_aircraft_type.grid(row=2, column=1, padx=10, pady=5)

    label_departure = tk.Label(main_window, text='Departure')
    label_departure.grid(row=3, column=0, padx=10, pady=5)
    entry_departure = tk.Entry(main_window)
    entry_departure.grid(row=3, column=1, padx=10, pady=5)

    label_arrival = tk.Label(main_window, text='Arrival')
    label_arrival.grid(row=4, column=0, padx=10, pady=5)
    entry_arrival = tk.Entry(main_window)
    entry_arrival.grid(row=4, column=1, padx=10, pady=5)

    label_departure_airport = tk.Label(main_window, text='Departure Airport')
    label_departure_airport.grid(row=5, column=0, padx=10, pady=5)
    entry_departure_airport = tk.Entry(main_window)
    entry_departure_airport.grid(row=5, column=1, padx=10, pady=5)

    label_arrival_airport = tk.Label(main_window, text='Arrival Airport')
    label_arrival_airport.grid(row=6, column=0, padx=10, pady=5)
    entry_arrival_airport = tk.Entry(main_window)
    entry_arrival_airport.grid(row=6, column=1, padx=10, pady=5)

    label_one_way_price = tk.Label(main_window, text='One-Way Price')
    label_one_way_price.grid(row=7, column=0, padx=10, pady=5)
    entry_one_way_price = tk.Entry(main_window)
    entry_one_way_price.grid(row=7, column=1, padx=10, pady=5)

    label_discount_price = tk.Label(main_window, text='Discount Price')
    label_discount_price.grid(row=8, column=0, padx=10, pady=5)
    entry_discount_price = tk.Entry(main_window)
    entry_discount_price.grid(row=8, column=1, padx=10, pady=5)

    label_departure_time = tk.Label(main_window, text='Departure Time')
    label_departure_time.grid(row=9, column=0, padx=10, pady=5)
    entry_departure_time = tk.Entry(main_window)
    entry_departure_time.grid(row=9, column=1, padx=10, pady=5)

    label_arrival_time = tk.Label(main_window, text='Arrival Time')
    label_arrival_time.grid(row=10, column=0, padx=10, pady=5)
    entry_arrival_time = tk.Entry(main_window)
    entry_arrival_time.grid(row=10, column=1, padx=10, pady=5)

    label_cabin_type = tk.Label(main_window, text='Cabin Type')
    label_cabin_type.grid(row=11, column=0, padx=10, pady=5)
    entry_cabin_type = tk.Entry(main_window)
    entry_cabin_type.grid(row=11, column=1, padx=10, pady=5)

    button_add = tk.Button(main_window, text='Add', command=add_data)
    button_add.grid(row=12, column=0, padx=10, pady=5)

    button_delete = tk.Button(main_window, text='Delete', command=delete_data)
    button_delete.grid(row=12, column=1, padx=10, pady=5)

    button_update = tk.Button(main_window, text='Update', command=update_data)
    button_update.grid(row=13, column=0, padx=10, pady=5)

    button_query = tk.Button(main_window, text='Query', command=query_data)
    button_query.grid(row=13, column=1, padx=10, pady=5)

    button_return = tk.Button(main_window, text='Return', command=return_to_login)
    button_return.grid(row=14, column=0, columnspan=2, padx=10, pady=5)

    main_window.protocol("WM_DELETE_WINDOW", return_to_login)


if __name__ == '__main__':
    login_window = tk.Tk()
    login_window.title('Login')

    label_username = tk.Label(login_window, text='Username')
    label_username.grid(row=0, column=0, padx=10, pady=5)
    entry_username = tk.Entry(login_window)
    entry_username.grid(row=0, column=1, padx=10, pady=5)

    label_password = tk.Label(login_window, text='Password')
    label_password.grid(row=1, column=0, padx=10, pady=5)
    entry_password = tk.Entry(login_window, show='*')
    entry_password.grid(row=1, column=1, padx=10, pady=5)

    button_login = tk.Button(login_window, text='Login', command=connect_to_database)
    button_login.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

    login_window.mainloop()
