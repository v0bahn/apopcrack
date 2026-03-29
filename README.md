# APOP MD5 Cracker

Script Python de crackage de mots de passe via le protocole **APOP**, conçu lors d'un **CTF**. 



## Qu'est-ce que l'APOP ?

APOP est un mécanisme d'authentification du protocole POP3. Lors d'une connexion, le serveur envoie un **timestamp unique**, et le client répond avec :

```
MD5(timestamp + mot_de_passe)
```

Si un attaquant capture ce timestamp et le hash MD5 résultant (via Wireshark ou toute capture réseau), il peut rejouer l'opération localement pour retrouver le mot de passe en clair.



## Fonctionnement du script

Le script effectue une **attaque par dictionnaire** :

1. Il lit la wordlist ligne par ligne
2. Pour chaque mot, il calcule `MD5(timestamp + mot)`
3. Il compare le résultat au hash cible capturé
4. Si les deux correspondent, le mot de passe est affiché

> ⚠️ Ce n'est pas un brute-force pur, mais une attaque par dictionnaire basée sur `rockyou.txt` pour l'example.



## Prérequis

- Python 3.x
- Une wordlist
- Les modules Python utilisés sont tous issus de la bibliothèque standard : `hashlib`, `time`



## Configuration

Les variables à modifier sont en haut du script :

```python
# Le timestamp APOP récupéré dans la capture réseau
timestamp = "<1755.1.5f403625.BcWGgpKzUPRC8vscWn0wuA==@vps-7e2f5a72>"

# Le hash MD5 cible récupéré dans la capture réseau
target_hash = "4ddd4137b84ff2db7291b568289717f0"

# Le chemin vers votre wordlist
wordlist_path = "/usr/share/wordlists/rockyou.txt"
```



## Utilisation

```bash
python3 APOPcrack.py
```

### Exemple de sortie

```
[*] APOP MD5 brute-force (CTF)
[*] Timestamp      : <1755.1.5f403625.BcWGgpKzUPRC8vscWn0wuA==@vps-7e2f5a72>
[*] Hash cible     : 4ddd4137b84ff2db7291b568289717f0
[*] Wordlist       : /usr/share/wordlists/rockyou.txt
[*] Démarrage...

[*] 500,000 tentatives | 1,243,000 hash/s

[+] MOT DE PASSE TROUVÉ !
[+] Mot de passe  : password123
[+] Tentatives    : 743,218
[+] Temps écoulé  : 0.60 s
[+] Vitesse       : 1,238,697 hash/s
```



## Cas d'usage typique (CTF)

1. Capturer un échange POP3 avec **Wireshark** (filtre : `pop`)
2. Récupérer le **timestamp** dans la bannière du serveur (`+OK` initial)
3. Récupérer le **hash MD5** envoyé par le client (commande `APOP`)
4. Renseigner ces deux valeurs dans le script
5. Lancer le script


## Avertissement

Ce script est fourni à des fins **éducatives et CTF uniquement**.  
L'utilisation de cet outil contre des systèmes sans autorisation explicite est **illégale**.
