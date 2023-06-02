def convert_notes_to_degrees(notas):
   
    mapeamento = {
        "Dó": "I",
        "Ré": "II",
        "Mi": "III",
        "Fá": "IV",
        "Sol": "V",
        "Lá": "VI",
        "Si": "VII"
    }
    
    
    saida = []
    for note in notas:
        if note in mapeamento:
            saida.append(mapeamento[note])
        else:
            saida.append("Unknown")
    
    return saida


notas = ["Ré","Sol","Dó","Lá","Si","Mi"]
saida = convert_notes_to_degrees(notas)
print("Entrada", notas)
print("Saída", saida)