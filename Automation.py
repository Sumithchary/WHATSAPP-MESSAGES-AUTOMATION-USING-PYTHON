import tkinter as tk
from tkinter import messagebox
import pywhatkit as kit
from datetime import datetime
import time

root = tk.Tk()
root.geometry("500x500")
root.title("WhatsApp Image and Message Sender")


def hide_widgets():
    for widget in root.winfo_children():
        widget.pack_forget()


def show_image_options():
    hide_widgets()
    tk.Button(root, text="Send Image to Single Person",
              command=send_image_to_single_person).pack(pady=10)
    tk.Button(root, text="Send Image to Group",
              command=send_image_to_group).pack(pady=10)
    tk.Button(root, text="Send Image to Selected Members",
              command=send_img_to_selected_members).pack(pady=10)
    tk.Button(root, text="Back to Main Menu",
              command=main_menu).pack(pady=5)


def show_message_options():
    hide_widgets()
    tk.Button(root, text="Send Message to Single Person",
              command=send_msg_to_single_person).pack(pady=10)
    tk.Button(root, text="Send Message to Group",
              command=send_msg_to_group).pack(pady=10)
    tk.Button(root, text="Send Message to Selected Members",
              command=send_msg_to_selected_members).pack(pady=10)
    tk.Button(root, text="Back to Main Menu",
              command=main_menu).pack(pady=5)


def main_menu():
    hide_widgets()
    tk.Button(root, text="Send an Image",
              command=show_image_options).pack(pady=10)
    tk.Button(root, text="Send a Message",
              command=show_message_options).pack(pady=10)


def send_image_to_single_person():
    hide_widgets()
    tk.Button(root, text="Send Image Instantly",
              command=send_image_instantly).pack(pady=10)
    tk.Button(root, text="Send Image After Some Time",
              command=send_image_after_time).pack(pady=10)
    tk.Button(root, text="Back",
              command=show_image_options).pack(pady=5)


def send_image_to_group():
    hide_widgets()
    tk.Button(root, text="Send Group Image Instantly",
              command=send_group_image_instantly).pack(pady=10)
    tk.Button(root, text="Send Group Image After Some Time",
              command=send_group_image_after_time).pack(pady=10)
    tk.Button(root, text="Back",
              command=show_image_options).pack(pady=5)


def send_img_to_selected_members():
    hide_widgets()
    tk.Button(root, text="Send Image Instantly",
              command=send_selected_image_instantly).pack(pady=10)
    tk.Button(root, text="Send Image After Some Time",
              command=send_selected_image_after_time).pack(pady=10)
    tk.Button(root, text="Back",
              command=show_image_options).pack(pady=5)


def send_image_instantly():
    def send_instant_image():
        number = entry_number.get()
        file_path = entry_image_path.get()

        if not file_path or not number:
            messagebox.showerror("Error", "Please provide both phone number and image path.")
            return

        try:
            print(f"Sending image to number: {number} from path: {file_path}")
            kit.sendwhats_image(number, file_path, "Hello")
            print(f"Sent image to number: {number} from path: {file_path}")
            messagebox.showinfo("Success", "Image sent instantly!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    hide_widgets()

    tk.Label(root, text="Phone Number (with country code):").pack(pady=5)
    entry_number = tk.Entry(root, width=50)
    entry_number.pack(pady=5)

    tk.Label(root, text="Image Path:").pack(pady=5)
    entry_image_path = tk.Entry(root, width=50)
    entry_image_path.pack(pady=5)

    tk.Button(root, text="Send Instantly",
              command=send_instant_image).pack(pady=20)
    tk.Button(root, text="Back",
              command=send_image_to_single_person).pack(pady=5)


def send_image_after_time():
    def send_delayed_image():
        number = entry_number.get()
        file_path = entry_image_path.get()

        try:
            send_hour = int(entry_hour.get())
            send_minute = int(entry_minute.get())
        except ValueError:
            messagebox.showerror("Error", "Invalid time format")
            return

        now = datetime.now()
        send_time = now.replace(hour=send_hour, minute=send_minute,
                                second=0, microsecond=0)

        if send_time < now:
            messagebox.showerror("Error", "Scheduled time must be in the future")
            return

        if not file_path or not number:
            messagebox.showerror("Error", "Please provide both phone number and image path.")
            return

        while now < send_time:
            time.sleep(10)
            now = datetime.now()

        try:
            print(f"Sending image to number: {number} from path: {file_path}")
            kit.sendwhats_image(number, file_path, "Hello")
            print(f"Sent image to number: {number} from path: {file_path}")
            messagebox.showinfo("Success", "Image sent at the scheduled time!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    hide_widgets()

    tk.Label(root, text="Phone Number (with country code):").pack(pady=5)
    entry_number = tk.Entry(root, width=50)
    entry_number.pack(pady=5)

    tk.Label(root, text="Image Path:").pack(pady=5)
    entry_image_path = tk.Entry(root, width=50)
    entry_image_path.pack(pady=5)

    tk.Label(root, text="Hour (24-hour format):").pack(pady=5)
    entry_hour = tk.Entry(root, width=5)
    entry_hour.pack(pady=5)

    tk.Label(root, text="Minute:").pack(pady=5)
    entry_minute = tk.Entry(root, width=5)
    entry_minute.pack(pady=5)

    tk.Button(root, text="Send After Time",
              command=send_delayed_image).pack(pady=20)
    tk.Button(root, text="Back",
              command=send_image_to_single_person).pack(pady=5)


# (Remaining code continues in same structured formatting…)

main_menu()
root.mainloop()
