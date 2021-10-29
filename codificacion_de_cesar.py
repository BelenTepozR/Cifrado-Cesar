class CodigoCesar:
    texto = " "

    def __init__(self):
        pass

    def setText(self,texto):
        self.texto = texto

    def codificar(self,num_desp, texoLLano):
        textoCodif = "";
        for ch in texoLLano:
            textoCodif+= chr(self.codAscci(ord(ch)+num_desp))
        return textoCodif

    def decodificar(self,num_desp,textoCodificado):
        textoDeCodif = "";
        for ch in textoCodificado:
          textoDeCodif+= chr(self.codAscci(ord(ch)-num_desp))
        return textoDeCodif

    def codAscci(self, character):
        if character > 256:
            return character%256
        if character < 0:
            return character%256
        return character
        

    def getText(self):
        return self.texto
