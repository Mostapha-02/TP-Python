seconde=float(input("donner un nombre un seconde"))
heurs=int(seconde/3600)
reste=int(seconde%3600)
minute=int(reste/60)
sec=reste%60
print(f"la valeur de {seconde} en convertion est {heurs}h:{minute}min:{sec} sec")