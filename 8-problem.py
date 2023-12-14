def juft_toq_uzunlikdagi_sozlarni_ayirish(fayl_nomi):
    with open('txt1.txt', 'r') as f:
        sozlar = f.read().split()

    uzunlik = {}
    for soz in sozlar:
        if len(soz) % 2 == 0:
            if 'juft' not in uzunlik:
                uzunlik['juft'] = []
            uzunlik['juft'].append(soz)
        else:
            if 'toq' not in uzunlik:
                uzunlik['toq'] = []
            uzunlik['toq'].append(soz)

    with open('juft_sozlar.txt', 'w') as juft_fayl:
        for soz in uzunlik['juft']:
            juft_fayl.write(soz + '\n')

    with open('toq_sozlar.txt', 'w') as toq_fayl:
        for soz in uzunlik['toq']:
            toq_fayl.write(soz + '\n')

fayl_nomi = 'matn.txt'  # Matn faylning nomi
juft_toq_uzunlikdagi_sozlarni_ayirish(fayl_nomi)
