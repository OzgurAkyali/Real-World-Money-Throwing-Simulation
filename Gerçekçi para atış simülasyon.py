import random

def para_ihtimaller(dik_ihtimal: float, taraf_bias: float):
    kalan = 1.0 - dik_ihtimal
    p_yazi = (0.5 - taraf_bias / 2.0) * kalan
    p_tura = (0.5 + taraf_bias / 2.0) * kalan
    return {"yazı": p_yazi, "tura": p_tura, "dik": dik_ihtimal}

def bir_kere_at(dik_ihtimal: float, taraf_bias: float):
    ihtimaller = para_ihtimaller(dik_ihtimal, taraf_bias)
    r = random.random()
    if r < ihtimaller["dik"]:
        return "D"
    r -= ihtimaller["dik"]
    if r < ihtimaller["yazı"]:
        return "Y"
    return "T"

if __name__ == "__main__":
    dik_ihtimal = 1 / 6000
    taraf_bias = random.uniform(0.0005, 0.003)

    sonuc = bir_kere_at(dik_ihtimal, taraf_bias)

    if sonuc == "Y":
        print("Yazı geldi")
    elif sonuc == "T":
        print("Tura geldi")
    else:
        print("Para dik geldi!")

