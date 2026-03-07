import random

class Scorboard:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.score1 = 0
        self.score2 = 0
        self.ilk_baslayan = None
        self.oyun_bitti = False
        self.mesaj = ""

    def kim_baslayacak(self):
        if self.ilk_baslayan is not None:
            self.mesaj = f"Maça zaten {self.ilk_baslayan} başladı!"
            return
        
        # Python'ın kendi kütüphanesini (random) doğrudan kullanabiliyoruz
        players = [self.player1, self.player2]
        self.ilk_baslayan = random.choice(players)
        self.mesaj = f"Kura çekildi! Başlayan: {self.ilk_baslayan}"

    def score_player1(self):
        if self.oyun_bitti: return
        self.score1 += 1
        self.kontrol_et(self.score1, self.score2, self.player1)

    def score_player2(self):
        if self.oyun_bitti: return
        self.score2 += 1
        self.kontrol_et(self.score2, self.score1, self.player2)

    def kontrol_et(self, p1_score, p2_score, kazanan_adayi):
        self.mesaj = ""
        if p1_score == 11:
            if p2_score <= 9:
                self.oyun_bitti = True
                self.mesaj = f"🏆 Tebrikler {kazanan_adayi} kazandı! 🏆"
            else:
                self.mesaj = "10-10 oldu! Fark 2 olana kadar oyun uzar."
        elif p1_score > 11:
            if (p1_score - p2_score == 2):
                self.oyun_bitti = True
                self.mesaj = f"🏆 Uzatmalarda {kazanan_adayi} kazandı! 🏆"

    def servis_kimde(self):
        if self.ilk_baslayan is None:
            return "Kura Bekleniyor..."

        toplam = self.score1 + self.score2
        if toplam < 20:
            degisim_sirasi = toplam // 2
        else:
            degisim_sirasi = toplam

        if degisim_sirasi % 2 == 0:
            return self.ilk_baslayan
        else:
            if self.ilk_baslayan == self.player1:
                return self.player2
            else:
                return self.player1
