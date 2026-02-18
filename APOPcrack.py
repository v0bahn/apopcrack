# APOP crack pass
import hashlib
import time

# Données de capture(example)

timestamp = "<1755.1.5f403625.BcWGgpKzUPRC8vscWn0wuA==@vps-7e2f5a72>"

target_hash = "4ddd4137b84ff2db7291b568289717f0"

# Wordlist 

wordlist_path = "/usr/share/wordlists/rockyou.txt"

# Initialisation

start_time = time.time()
attempts = 0
found = False

print("[*] APOP MD5 brute-force (CTF)")
print(f"[*] Timestamp      : {timestamp}")
print(f"[*] Hash cible     : {target_hash}")
print(f"[*] Wordlist       : {wordlist_path}")
print("[*] Démarrage...\n")

try:
    with open(wordlist_path, "r", errors="ignore") as f:
        for pwd in f:
            pwd = pwd.strip()
            attempts += 1

            # Calcul MD5(timestamp + password)
            md5 = hashlib.md5((timestamp + pwd).encode()).hexdigest()

            # Check
            if md5 == target_hash:
                elapsed = time.time() - start_time
                print("\n[+] MOT DE PASSE TROUVÉ !")
                print(f"[+] Mot de passe  : {pwd}")
                print(f"[+] Tentatives   : {attempts}")
                print(f"[+] Temps écoulé : {elapsed:.2f} s")
                print(f"[+] Vitesse      : {attempts / elapsed:.0f} hash/s")
                found = True
                break

            # Progression 
            if attempts % 500_000 == 0:
                elapsed = time.time() - start_time
                rate = attempts / elapsed if elapsed > 0 else 0
                print(
                    f"\r[*] {attempts:,} tentatives | {rate:,.0f} hash/s",
                    end="",
                    flush=True
                )

except FileNotFoundError:
    print(f"[!] Wordlist introuvable : {wordlist_path}")


# Récap de fin

if not found:
    elapsed = time.time() - start_time
    print("\n[-] Mot de passe NON trouvé")
    print(f"[-] Tentatives   : {attempts}")
    print(f"[-] Temps écoulé : {elapsed:.2f} s")
    if elapsed > 0:
        print(f"[-] Vitesse      : {attempts / elapsed:.0f} hash/s")
