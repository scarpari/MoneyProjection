import numpy as np
import matplotlib.pyplot as plt

f = open("analise.txt", "a")

class investimento:
    def __init__(self, nome, montante0_livre, montante0_investido,
                 montante0_sem_ter_investido, tempo, earnings, gastos):
        self.nome = nome
        self.montante0_livre = montante0_livre
        self.montante0_investido = montante0_investido
        self.montante0_sem_ter_investido = montante0_sem_ter_investido
        self.tempo = tempo
        self.gastos = gastos
        self.earnings = earnings

    def mes(self):
        tempo = self.tempo
        mes = list(range(1, 1 + tempo + 1))
        return mes

    def montante_investido (self):
        earnings = self.earnings
        montante0_investido = self.montante0_investido
        montante_investido = montante0_investido
        m_investido = np.array([])
        mes = self.mes()
        for element in mes:
            montante_investido *= earnings
            m_investido = np.append(m_investido, montante_investido)
        return m_investido

    def montante_livre (self):
        gastos = self.gastos
        montante0_livre = self.montante0_livre
        montante_livre = montante0_livre
        m_livre = np.array([])
        mes = self.mes()
        for element in mes:
            montante_livre -= gastos
            m_livre = np.append(m_livre, montante_livre)
        return m_livre

    def montante_total_investindo (self):
        return self.montante_livre() + self.montante_investido()

    def montante_sem_ter_investido(self):
        gastos = self.gastos
        montante_SemTerInvestido = self.montante0_sem_ter_investido
        m_SemTerInvestido = np.array([])
        mes = self.mes()
        for element in mes:
            montante_SemTerInvestido -= gastos
            m_SemTerInvestido = np.append(m_SemTerInvestido, montante_SemTerInvestido)
        return m_SemTerInvestido

    def montante_delta(self):
        return self.montante_total_investindo() - self.montante_sem_ter_investido()

    def plot(self):
        nome = self.nome
        Mes = np.array(self.mes())
        m_investindo = self.montante_total_investindo()
        m_nao_investindo = self.montante_sem_ter_investido()
        m_delta = self.montante_delta()
        plt.plot(Mes, m_investindo, 'b-', label='Com Investimento')
        plt.plot(Mes, m_nao_investindo, 'r-', label='Sem Investimento')
        plt.plot(Mes, m_delta, 'g-', label='Diferença Total')
        plt.legend(loc="upper left")
        plt.title('Investimento ao Longo do Tempo - ' + nome + '\n')
        plt.xlabel('Mês')
        plt.ylabel('Montante (R$)')
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
        self.write()
        plt.show()

    def write(self):
        nome = self.nome
        gastos= self.gastos
        earnings = self.earnings
        mes = self.mes()
        f.write("-> " + nome + ": \n"
                "     Gastos = R${}"
                "  Rendimento Mensal = {}%".format(gastos, -100 + 100 * earnings))
        for i in mes:
            f.write("\n\n     Mes {:2d} - Montante Sem ter Investido:  R${:11.2f}\n"
                    "              Montante Total Investindo:   R${:11.2f}\n"
                    "              Diferenca:                   R${:11.2f}".format(i, self.montante_sem_ter_investido()[i-1],
                                                                                   self.montante_total_investindo()[i-1],
                                                                                   self.montante_total_investindo()[i-1]
                                                                                   - self.montante_sem_ter_investido()[i-1]))
        f.write("\n\n-------------------------------------------------------------------------------------------------\n\n")