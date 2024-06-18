subyek = {'saya', 'kamu', 'dia', 'mereka', 'kita'}
predikat = {'makan', 'minum', 'membaca', 'menulis', 'pergi'}
obyek = {'apel', 'buku', 'air', 'surat', 'rumah'}
keterangan = {'di rumah', 'di kampus', 'sendiri', 'kemarin', 'besok'}

kombinasiValid = {
    "makan": {"apel"},
    "minum": {"air"},
    "membaca": {"buku", "surat"},
    "menulis": {"buku", "surat"},
    # pergi tidak memiliki kombinasi valid dengan objek
}

struktur_valid = [
    ["S", "P", "O", "K"],
    ["S", "P", "K"],
    ["S", "P", "O"],
    ["S", "P"]
]

def cek_jenis(kata):
    if kata in subyek:
        return "S"
    elif kata in predikat:
        return "P"
    elif kata in obyek:
        return "O"
    elif kata in keterangan:
        return "K"
    else:
        return "U"
        # U == bukan s,p,o,k

def split_kalimat(kalimat):
    kata = kalimat.split()
    hasil = []
    i = 0
    while i < len(kata):
        frasa = kata[i]
        while i + 1 < len(kata) and frasa + " " + kata[i + 1] in keterangan:
            frasa += " " + kata[i + 1]
            i += 1
        hasil.append(frasa)
        i += 1
    return hasil

def cek_struktur_valid(jenis):
    return jenis in struktur_valid

def cek_logika(words):
    for i in range(len(words) - 1):
        if cek_jenis(words[i]) == "P" and cek_jenis(words[i + 1]) == "O":
            predicate = words[i]
            obj = words[i + 1]
            if obj not in kombinasiValid.get(predicate, set()):
                return False
    return True

# nomor 2
def parser(jenis):
    stack = ["S"]
    index = 0

    while stack:
        top = stack.pop()
        if top == "S" and index < len(jenis) and jenis[index] == "S":
            stack.append("P")
            index += 1
        elif top == "P" and index < len(jenis) and jenis[index] == "P":
            if index + 1 < len(jenis) and jenis[index + 1] == "O":
                stack.append("O")
            elif index + 1 < len(jenis) and jenis[index + 1] == "K":
                stack.append("K")
            index += 1
        elif top == "O" and index < len(jenis) and jenis[index] == "O":
            if index + 1 < len(jenis) and jenis[index + 1] == "K":
                stack.append("K")
            index += 1
        elif top == "K" and index < len(jenis) and jenis[index] == "K":
            index += 1
        else:
            return False

    return index == len(jenis)
# nomor 2

def main():
    kalimat = input("Masukkan kalimat: ")
    
    kata = split_kalimat(kalimat)
    print("Kata terdeteksi :", kata) 

    jenis = [cek_jenis(word) for word in kata]
    print("Jenis terdeteksi :", jenis)

    if "U" in jenis:
        print("Terdapat kata yang invalid.")
    elif cek_struktur_valid(jenis):
        print("Struktur yang cocok:", jenis)

        if cek_logika(kata) and parser(jenis):
            print("Kalimat valid.")
        else:
            print("Kalimat invalid karena tidak logis.")
    else:
        print("Struktur tidak valid.")

if __name__ == "__main__":
    main()