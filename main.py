""" PROJECTION EARNINGS - RICARDO PATRIZI SCARPARI """
from MILITAR import militar
from ESTAGIO import estagio
from INVESTIMENTO import investimento
from MF import mercado_financeiro
from DIFERENCA import diferenca


f = open("analise.txt", "w")
f.write("================================================"
        " PROJECOES DE GANHOS "
        "================================================"
        "\n\n")

"""
    ------------------------------------------------------------------------------------------------------------
    -------------------------------------------- L E G E N D A -------------------------------------------------
    
    sal0 -> salário inicial
    sal -> salario atualizado
    gastos -> gastos mensais
    invest -> quanto do montante recebido no mês será destinado a investimento (0.85 = 85% do montante recebido)
    earnings -> rendimento mensal dos investimentos (1.04 = 4% de rendimento)
    increase -> porcentagem de aumento anual (1.05 = 5% de aumento)
    nome -> nome da string
    array_1/array_2 -> nome dos arrays em comparacao em funcao do tempo
    montante0_XxXx -> montante inicial de XxXx
    bonus -> bonus do mercado financeiro

    ------------------------------------------------------------------------------------------------------------
    -----------------------------------------------G U I A -----------------------------------------------------
    
    
    estagio -> (nome, montante0_livre, montante0_investido, montante0_sem_ter_investido,
                 sal, tempo, gastos, invest, earnings)
                 
    mercado_financeiro -> (nome, sal0, inicio, tempo, gastos, invest, earnings, increase, bonus,
                 montante0_investido, montante0_livre, montante0_sem_ter_investido)
                 
    militar -> (nome, sal0, inicio, tempo, gastos, invest, earnings, increase,
                 montante0_investido, montante0_livre, montante0_sem_ter_investido)
                 
    investimento -> (nome, montante0_livre, montante0_investido,
                 montante0_sem_ter_investido, tempo, earnings, gastos)
                 
    comparar -> (nome, nome_1, nome_2, array_1, array_2, tempo)
    
    ------------------------------------------------------------------------------------------------------------
"""

if __name__ == "__main__":
    print("Software de prjecoes de montante de verba")
    aspof = militar("aspof", 8000, 2, 35, 900, 0.85, 1.02, 1.05, 0, 0, 0)
    aspof.plot()
    tenente = militar("Tenente", 9500, 2, 35, 900, 0.85, 1.02, 1.05,
    aspof.montante_investido()[aspof.tempo], aspof.montante_livre()[aspof.tempo], aspof.montante_sem_ter_investido()[aspof.tempo])
    tenente.plot()
    estag1 = estagio("estag1",0, 7500, 7500, 2000, 3, 500, 0.50, 1.02) # summer 2° ano
    estag1.plot()
    inv1 = investimento("inv1", estag1.montante_livre()[estag1.tempo], estag1.montante_investido()[estag1.tempo],
                        estag1.montante_sem_ter_investido()[estag1.tempo], 5, 1.04, 500) # investimento durante o periodo de gap entre um estagio e outro
    inv1.plot()
    estag2 = estagio("estag2", inv1.montante_livre()[inv1.tempo], inv1.montante_investido()[inv1.tempo], inv1.montante_sem_ter_investido()[inv1.tempo],
                     2000, 30, 500, 0.50, 1.02) # estagio no 2° semestre do 3° ano ate o final do 5° ano
    estag2.plot()

    mf1 = mercado_financeiro("mf1",2000, 2, 35, 1000, 0.30, 1.02, 1.3, 25000, estag2.montante_livre()[estag2.tempo], estag2.montante_investido()[estag2.tempo],
                        estag2.montante_sem_ter_investido()[estag2.tempo])
    mf1.plot()
    t = min(mf1.tempo, tenente.tempo)
    dif = diferenca('Diferenca MILITAR/MF', 'Militar', 'MF', tenente.montante_total_investindo(),
                    mf1.montante_total_investindo(), t)
    dif.plot()
    f.write("\n\n- Feito por Ricardo Patrizi Scarpari")
    print(("\n\n- Feito por Ricardo Patrizi Scarpari"))
    f.close()