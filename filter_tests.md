# Network Traffic Filtering Tests

## Firewall Rules Configuration (iptables)
```bash
# Reset rules
sudo iptables -F INPUT

# a. Block Guest network (10.0.20.0/24) access to HTTPS (port 443) on Records Server (10.0.1.50)
sudo iptables -A INPUT -p tcp -s 10.0.20.0/24 -d 10.0.1.50 --dport 443 -j DROP

# b. Permit Staff network (10.0.10.0/24) access to HTTPS (port 443) on Records Server (10.0.1.50)
sudo iptables -A INPUT -p tcp -s 10.0.10.0/24 -d 10.0.1.50 --dport 443 -j ACCEPT

# c. Block all other inbound access to HTTPS (port 443)
sudo iptables -A INPUT -p tcp --dport 443 -j DROP