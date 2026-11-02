f = open("mailbox.txt","r")
out = open("output.txt","w")

for line in f:
    if line.startswith("From"):
        email = line.split()[1]
        domain = email.split("@")[1]
        out.write(domain + "\n")

f.close()
out.close()