class Televisao:
    # Constructor
    def __init__(self):
        self.__status: bool = False
        self.__volume: int  = 0
        self.__canal:  int  = 0
    
    # Getters and Setters
    @property
    def status(self) -> bool:
        return self.__status

    @status.setter
    def status(self, status: bool) -> None: 
        self.__status = status

    @property
    def volume (self) -> int:
        return self.__volume

    @volume.setter
    def volume(self, volume: int) -> None:
        self.__volume = volume

    @property
    def canal(self) -> int:
        return self.__canal

    @canal.setter
    def canal(self, canal: int) -> None:
        self.__canal = canal

    # Methods
    def ligar_desligar(self) -> None:
        self.status = not self.status

        if self.status:
            print("Status da TV: Ligada!")
        else:
            print("Status da TV: Desligada!")

    def aumentar_volume(self) -> None:
        self.volume += 1
        print(f"Volume da TV +: {self.volume}")

    def diminuir_volume(self) -> None:
            self.volume -= 1
            print(f"Volume da TV -: {self.volume}")

    def aumentar_canal(self) -> None:
        self.canal += 1
        print(f"Canal da TV +: {self.canal}")
    
    def diminuir_canal(self) -> None:
        self.canal -= 1
        print(f"Canal da TV -: {self.canal}")

    def mudar_canal(self, canal: int) -> None:
        self.canal = canal
        print(f"Canal da TV ?: {self.canal}")

class ControleRemoto:
    
    # Constructor
    def __init__(self, televisao: Televisao) -> None:
        self.__televisao: Televisao = televisao

    # Getters and Setters
    @property
    def televisao(self) -> Televisao:
        return self.__televisao

    @televisao.setter
    def televisao(self, televisao: Televisao) -> None:
        self.__televisao = televisao

    # Methods
    def ligar_desligar(self) -> None:
        self.televisao.ligar_desligar()

    def aumentar_volume(self) -> None:
        self.televisao.aumentar_volume()

    def diminuir_volume(self) -> None:
        self.televisao.diminuir_canal()
    
    def aumentar_canal(self) -> None:
        self.televisao.aumentar_canal()
        
    def diminuir_canal(self) -> None:
        self.televisao.diminuir_canal()        

    def mudar_canal(self, canal: int) -> None:
        self.televisao.mudar_canal(canal)


if __name__ == "__main__":
    tv: Televisao = Televisao()

    tv.ligar_desligar()

    tv.aumentar_canal()
    tv.aumentar_canal()
    tv.aumentar_canal()

    tv.mudar_canal(42)

    tv.aumentar_volume()
    tv.aumentar_volume()
    tv.aumentar_volume()

    tv.diminuir_canal()
    tv.diminuir_volume()

    tv.ligar_desligar()

    cr: ControleRemoto = ControleRemoto(tv)

    cr.ligar_desligar()

    cr.aumentar_canal()
    cr.aumentar_canal()
    cr.aumentar_canal()

    cr.mudar_canal(42)

    cr.aumentar_volume()
    cr.aumentar_volume()
    cr.aumentar_volume()

    cr.diminuir_canal()
    cr.diminuir_volume()

    cr.ligar_desligar()