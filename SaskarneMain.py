import pygame

# === Poga =========================================

class Poga:

    # Konstruktors -  izveido jaunu pogu ar norādīto pozīciju, izmēru un tekstu
    def __init__(self, x, y, platums, augstums, teksts):
        self.X = x
        self.Y = y
        self.Platums = platums
        self.Augstums = augstums
        self.Teksts = teksts
        self.Taisnsturis = pygame.Rect(x, y, platums, augstums)

    # Parāda pogu uz ekrāna
    def Paradit(self, Logs, Fonts):
        PeleX, PeleY = pygame.mouse.get_pos() # iegūst peles pašreizējo pozīciju

        if self.Taisnsturis.collidepoint(PeleX, PeleY):
            Krasa = pygame.Color("#D4FF5E") # pogas krāsa, kad pele atrodas virs tās
        else:
            Krasa = pygame.Color("#C6FFA3") # pogas parastā krāsa
            
        pygame.draw.rect(Logs, Krasa, self.Taisnsturis, border_radius=15)
        pygame.draw.rect(Logs, pygame.Color("#74C214"), self.Taisnsturis, width=3, border_radius=15)

        Teksts = Fonts.render(self.Teksts, True, (0, 0, 0))
        TekstaVieta = Teksts.get_rect(center=self.Taisnsturis.center)
        Logs.blit(Teksts, TekstaVieta)

    # Pārbauda, vai poga ir nospiesta
    def VaiNospiesta(self, Pozicija):
        return self.Taisnsturis.collidepoint(Pozicija)


# === Saskarne =====================================

pygame.init()

Platums = 1000
Augstums = 650

#izveido programmas logu
Logs = pygame.display.set_mode((Platums, Augstums)) 
pygame.display.set_caption("Dārgumu Medības Džungļos")

Fonts = pygame.font.SysFont("comicsansms", 30, bold=True)

Fons = pygame.image.load("assets/fons.png")
Fons = pygame.transform.scale(Fons, (Platums, Augstums))

Pogas = [
    Poga(350, 250, 300, 60, "Spēlēt"),
    Poga(350, 320, 300, 60, "Spēles noteikumi"),
    Poga(350, 390, 300, 60, "Rezultāti"),
    Poga(350, 460, 300, 60, "Iziet")
]

Darbojas = True # mainīgais, kas kontrolē programmas darbību

while (Darbojas == True):

    for Event in pygame.event.get():

        if Event.type == pygame.QUIT:
            Darbojas = False

        # Lietotājs nospiež peles pogu
        if Event.type == pygame.MOUSEBUTTONDOWN:
            Pozicija = Event.pos  # Saglabā peles pozīciju

            for poga in Pogas:
                if poga.VaiNospiesta(Pozicija):
                    print("Nospiesta poga:", poga.Teksts)

                    if poga.Teksts == "Iziet":
                        Darbojas = False

    Logs.blit(Fons, (0, 0))

    for poga in Pogas:
        poga.Paradit(Logs, Fonts)
    
    # Atjauno ekrāna attēlu
    pygame.display.update()

pygame.quit()