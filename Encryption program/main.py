
import base64
import time
# password encryption program
def encrypt_info(data):
    encode_bytes = base64.b64encode(data.encode())
    print(encode_bytes)
    with open("my_data", "a") as new_file:
        new_file.write(str(encode_bytes) + "\n")



while True:
 user_data = input("Enter your info: ")
 if user_data.lower() =="exit":
    break
 time.sleep(2)
 encrypt_info(user_data) 
 print("\n")
#decrypt bytes
def decode_bytes( data):
   decode_bytes = base64.b64decode(data)
   decode_data = decode_bytes.decode()
   print(f"{decode_data}")
print("STRING OF DATA DECRYPTION\n")
encode_string =input("Enter your data string: ")
time.sleep(5)
decode_bytes(encode_string)    
