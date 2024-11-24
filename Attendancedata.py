import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
import sqlite3
import csv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import tkinter as tk
from tkinter import font as tkFont

def showAttendance():
    conn = sqlite3.connect('attendance.db')
    cursor = conn.cursor()
    
    def save_as_csv(data,selected_date):
        global filename
        filename=f"data_{selected_date}.csv"
        with open(filename, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(['Name', 'Time', 'Date'])
            csvwriter.writerows(data)

    def retrieve_data(selected_date):
        cursor.execute("SELECT * FROM attendance WHERE date = ?", (selected_date,))
        data = cursor.fetchall()
        return data

    def update_table(selected_date):
        data = retrieve_data(selected_date)
        tree.delete(*tree.get_children())  
        for record in data:
            tree.insert('', 'end', values=record)
    
    def mail():
        def send_email():
            receiver_email = entry_receiver.get() 
            subject = 'CSV File Attachment'
            attachment_path =filename
            # Create a multipart message
            message = MIMEMultipart()
            message['From'] = 'jojerline2212@gmail.com' 
            message['To'] = receiver_email
            message['Subject'] = subject



            # Attach CSV file
            with open(attachment_path, 'rb') as file:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(file.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename= {attachment_path}')
            message.attach(part)

            # Connect to SMTP server and send email
            smtp_server = 'smtp.gmail.com'  # Update with your SMTP server address
            smtp_port = 587  # Update with your SMTP server port
            try:
                server = smtplib.SMTP(smtp_server, smtp_port)
                server.starttls()
                server.login('jojerline2212@gmail.com', 'dowl qhjp uuzb peym')
                server.sendmail('jojerline2212@gmail.com', receiver_email, message.as_string())
                print("success")
                root.destroy()
            except Exception as e:
                print(f"Error: {e}")
            finally:
                server.quit()


        root = tk.Tk()
        root.title("Email Sender")
        root.geometry('400x200')
        font_title = tkFont.Font(family='Helvetica', size=10, weight='bold')
        tk.Label(root,text="Enter Reciever Mail",
                        font=font_title).pack()
        entry_receiver = tk.Entry(root, )
        entry_receiver.pack()
        tk.Button(root, text="Send Email", command=send_email).pack()

        root.mainloop()
        
    def calendar_date_selected():
        selected_date = cal.selection_get().strftime('%d-%m-%y')
        update_table(selected_date)
        return selected_date
    
    
    def save_csv_button_clicked():
        
        selected_date = cal.selection_get().strftime('%d-%m-%y')
        data = retrieve_data(selected_date)
        save_as_csv(data,selected_date)
        print("Data saved as CSV")
        
        
        
    root = tk.Tk()
    root.title("Attendance Register")

    cal = Calendar(root, selectmode='day', year=2024, month=3, day=1)
    cal.pack()

    cal.bind("<<CalendarSelected>>", lambda event: calendar_date_selected())

    tree = ttk.Treeview(root, columns=('Name', 'Time', 'Date'), show='headings')
    tree.heading('Name', text='Name')
    tree.heading('Time', text='Time')
    tree.heading('Date', text='Date')
    tree.pack()

    btn_save_csv = tk.Button(root, text="Save as CSV", command=save_csv_button_clicked,)
    btn_save_csv.pack()
    btn_send_mail= tk.Button(root,text="Send as mail",command=mail)
    btn_send_mail.pack()

    root.mainloop()

    conn.close()
# showAttendance()