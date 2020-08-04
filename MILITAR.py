import numpy as np
import math
import matplotlib.pyplot as plt

f = open("analise.txt", "a")

class militar:
    def __init__(self, nome, sal0, inicio, tempo, gastos, invest, earnings, increase,
                 montante0_investido, montante0_livre, montante0_sem_ter_investido):
        self.nome = nome
        self.sal0 = sal0
        self.inicio = inicio
        self.tempo = tempo
        self.gastos = gastos
        self.invest = invest
        self.earnings = earnings
        self.increase = increase
        self.montante0_investido = montante0_investido
        self.montante0_livre = montante0_livre
        self.montante0_sem_ter_investido = montante0_sem_ter_investido

    def mes(self):
        inicio = self.inicio
        tempo = self.tempo
        mes = list(range(inicio, inicio + tempo + 1))
        return mes

    def montante_investido (self):
        sal0 = self.sal0
        invest = self.invest
        earnings = self.earnings
        inicio = self.inicio
        increase = self.increase
        montante_investido = self.montante0_investido
        m_investido = np.array([])
        mes = self.mes()
        for i in mes:
            k = i - inicio
            a = (k - k % 12) / 12  # reduz-se 2 pois o aumento so passa a ser valido em fevereiro
            sal = sal0 * math.pow(increase, a)
            recebido = sal
            half_third = 1 / 6 * sal
            half_13 = sal / 2
            if i%6==0:
                recebido += half_13 + half_third
            montante_investido += recebido * invest
            montante_investido *= earnings
            m_investido = np.append(m_investido, montante_investido)
        return m_investido

    def montante_livre (self):
        sal0 = self.sal0
        gastos = self.gastos
        invest = self.invest
        inicio = self.inicio
        increase = self.increase
        montante_livre = self.montante0_livre
        m_livre = np.array([])
        mes = self.mes()
        for i in mes:
            k = i - inicio
            a = (k - k % 12) / 12  # reduz-se 2 pois o aumento so passa a ser valido em fevereiro
            sal = sal0 * math.pow(increase, a)
            recebido = sal
            half_third = 1 / 6 * sal
            half_13 = sal / 2
            if i%6==0:
                recebido += half_13 + half_third
            montante_livre += recebido * (1 - invest) - gastos
            m_livre = np.append(m_livre, montante_livre)
        return m_livre

    def montante_total_investindo(self):
        return self.montante_livre() + self.montante_investido()

    def montante_sem_ter_investido(self):
        sal0 = self.sal0
        gastos = self.gastos
        inicio = self.inicio
        increase = self.increase
        montante_SemTerInvestido = self.montante0_sem_ter_investido
        m_SemTerInvestido = np.array([])
        mes = self.mes()
        for i in mes:
            k = i-inicio
            a = (k - k % 12) / 12  # reduz-se 2 pois o aumento so passa a ser valido em fevereiro
            sal = sal0 * math.pow(increase, a)
            recebido = sal
            half_third = 1 / 6 * sal
            half_13 = sal / 2
            if i%6==0:
                recebido += half_13 + half_third
            montante_SemTerInvestido += recebido - gastos
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
        sal0 = self.sal0
        gastos= self.gastos
        invest = self.invest
        earnings = self.earnings
        mes = self.mes()
        f.write("-> " + nome + ": \n"
                "     Salario = R${}   Gastos = R${}   Investimento Mensal = {}%"
                "  Rendimento Mensal = {}%".format(sal0, gastos, invest * 100, -100 + 100 * earnings))
        for i in mes:
            f.write("\n\n     Mes {:2d} - Montante Sem ter Investido:  R${:11.2f}\n"
                    "              Montante Total Investindo:   R${:11.2f}\n"
                    "              Diferenca:                   R${:11.2f}".format(i, self.montante_sem_ter_investido()[i-self.inicio],
                                                                                   self.montante_total_investindo()[i-self.inicio],
                                                                                   self.montante_total_investindo()[i-self.inicio]
                                                                                   - self.montante_sem_ter_investido()[i-self.inicio]))
        f.write("\n\n-------------------------------------------------------------------------------------------------\n\n")