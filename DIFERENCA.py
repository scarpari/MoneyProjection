import numpy as np
import matplotlib.pyplot as plt

f = open("analise.txt", "a")

class diferenca:
    def __init__(self, nome, nome_1, nome_2, array_1, array_2, tempo):
        self.nome = nome
        self.nome_1 = nome_1
        self.nome_2 = nome_2
        self.array_1 = array_1
        self.array_2 = array_2
        self.tempo = tempo

    def mes(self):
        tempo = self.tempo
        mes = list(range(1, 1 + tempo + 1))
        return mes

    def montante_delta(self):
        return self.array_1 - self.array_2

    def plot(self):
        nome = self.nome
        nome_1 = self.nome_1
        nome_2 = self.nome_2
        Mes = np.array(self.mes())
        array_1 = self.array_1
        array_2 = self.array_2
        m_delta = self.montante_delta()
        plt.plot(Mes, array_1, 'b-', label= nome_1)
        plt.plot(Mes, array_2, 'r-', label= nome_2)
        plt.plot(Mes, m_delta, 'g-', label='Diferença Total')
        plt.legend(loc="upper left")
        plt.title(nome + '\n')
        plt.xlabel('Mês')
        plt.ylabel('Montante (R$)')
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
        self.write()
        plt.show()

    def write(self):
        nome = self.nome
        nome_1 = self.nome_1
        nome_2 = self.nome_2
        array_1 = self.array_1
        array_2 = self.array_2
        mes = self.mes()
        f.write("-> " + nome + ":")
        for i in mes:
            f.write("\n\n     Mes {:2d} - {}:  R${:11.2f}\n"
                    "              {}:  R${:11.2f}\n"
                    "              Diferenca    :  R${:11.2f}".format(i, nome_1.ljust(13), array_1[i - 1], nome_2.ljust(13), array_2[i - 1],
                                                                                   array_1[i - 1] - array_2[i - 1]))
        f.write("\n\n-------------------------------------------------------------------------------------------------\n\n")