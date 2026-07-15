"""
Cloud Server Configuration (Class vs Instance Attributes) - SIMPLE

Aik Server class banayein jahan class level par
provider_name = "AWS" ho aur instance level par server ki ip_address
ho. Explain karein ke humne provider name ko class level par kyun
rakha.
"""

class Server:
    provider_name = "AWS"   # CLASS attribute -- shared by every server object

    def __init__(self, ip_address):
        self.ip_address = ip_address   # INSTANCE attribute -- unique per server


server1 = Server("192.168.1.10")
server2 = Server("192.168.1.11")

print(f"Server 1 -> Provider: {server1.provider_name}, IP: {server1.ip_address}")
print(f"Server 2 -> Provider: {server2.provider_name}, IP: {server2.ip_address}")

"""
ANSWER / EXPLANATION:
provider_name is placed at the CLASS level (directly inside the class
body, outside __init__) because EVERY server in this system runs on
the exact same cloud provider ("AWS") -- it's a shared fact that
doesn't change from one server to another.

Putting it at the class level means there's only ONE copy of that
string in memory, shared by ALL Server objects, instead of each
object wastefully storing its own separate, identical copy of "AWS".

In contrast, ip_address is placed at the INSTANCE level (inside
__init__, using self.) because each individual server genuinely has
its OWN, different IP address -- this data can't be shared, since it's
unique to every specific server object.
"""
