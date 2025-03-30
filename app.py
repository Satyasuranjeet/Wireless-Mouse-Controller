import pywhatkit
import qrcode
import socket

# Get the local IPv4 address
hostname = socket.gethostname()
ipv4 = socket.gethostbyname(hostname)

# Generate the URL
url = f"http://{ipv4}:8000"

# Generate and display the QR code in the terminal
qr = qrcode.QRCode()
qr.add_data(url)
qr.make()
qr.print_ascii()

# Print the URL for reference
print(f"Server URL: {url}")

pywhatkit.start_server()