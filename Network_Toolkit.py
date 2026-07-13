import tkinter as tk
import subprocess
import os

def run_cmd(cmd):
    subprocess.Popen(
        f'start cmd /k "{cmd}"',
        shell=True
    )

def ip_config():
    run_cmd("ipconfig /all")

def flush_dns():
    run_cmd("ipconfig /flushdns")

def release_ip():
    run_cmd("ipconfig /release")

def renew_ip():
    run_cmd("ipconfig /renew")

def reset_winsock():
    run_cmd("netsh winsock reset")

def reset_tcp():
    run_cmd("netsh int ip reset")

def ping_google():
    run_cmd("ping google.com -t")

def open_network():
    os.system("ncpa.cpl")

root = tk.Tk()
root.title("Network Troubleshoot Toolkit")
root.geometry("420x520")
root.configure(bg="#0d1b2a")

title = tk.Label(
    root,
    text="NETWORK TOOLKIT",
    bg="#0d1b2a",
    fg="#00f5d4",
    font=("Segoe UI", 18, "bold")
)
title.pack(pady=20)

btn_style = {
    "font": ("Segoe UI", 11),
    "bg": "#1b263b",
    "fg": "white",
    "activebackground": "#415a77",
    "width": 30,
    "height": 2
}

buttons = [
    ("Show IP Configuration", ip_config),
    ("Flush DNS Cache", flush_dns),
    ("Release IP Address", release_ip),
    ("Renew IP Address", renew_ip),
    ("Reset Winsock", reset_winsock),
    ("Reset TCP/IP Stack", reset_tcp),
    ("Ping Google", ping_google),
    ("Open Network Connections", open_network),
]

for text, command in buttons:
    tk.Button(root, text=text, command=command, **btn_style).pack(pady=6)
    
tk.Label(
    root,
    text="Prepared by Abdulbaseer Serat – Senior ICT Officer NE ACTED",
    bg="#0d1b2a",
    fg="#9aa3ad",
    font=("Segoe UI", 9, "italic")
).pack(pady=6)

root.mainloop()