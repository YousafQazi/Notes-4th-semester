
p = 23         
g_full = 5     


g_sub = 22      

print("Using fake generator with small order:", g_sub)


bob_priv = 7
print("Bob's private key (secret):", bob_priv)

B = pow(g_sub, bob_priv, p)
print("Bob's public value with small-order generator:", B)

candidates = []
for b in range(2):  
    if pow(g_sub, b, p) == B:
        candidates.append(b)

print("Attacker learns Bob's key modulo 2:", candidates)
