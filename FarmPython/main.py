import os
from time import sleep
import defs
import cores

#variaveis
animais = 0
racao = 0
sementes_trigo = 0
trigo = 0
exp = 0
dinheiro = 100.00

#Programa principal
defs.limpar_tela()
defs.menu()

while True:
    print('__'*15, '\n')
    print(cores.letra_ciano,f'Animais: {animais}')
    print(f'Sementes: {sementes_trigo}')
    print(f'Trigo: {trigo}')
    print(f'Ração: {racao}')
    print(f'EXP: {exp}')
    print(f'Dinheiro: R${dinheiro}', cores.parar_cor)
    print('__'*15, '\n')

    print(cores.fundo_branco, cores.letra_preta,'O que vc deseja fazer agora?', cores.parar_cor)
    print('[1] - Alimentar animais')
    print('[2] - Plantar Trigo')
    print('[3] - Loja')
    print('[4] - Sair do Jogo')
    res = int(input('\n?'))
    print('\n')
    defs.limpar_tela()

    #if's
    #[1] - Alimentar Animais + EXP
    if res == 1 and racao == 0:
        print('-=' *30)
        print(cores.letra_vermelha, cores.fundo_branco, 'Vc não possui ração. Compre mais na loja!', cores.parar_cor)
        print('-='*30)
    elif res == 1 and racao != 0 and racao >= animais:
        racao -= animais
        exp += 5.50
        animais += 2
        print('Animais alimentados e felizes...')
    elif res == 1 and racao != 0 and racao < animais:
        print('-=' *30)
        print(cores.letra_vermelha, cores.fundo_branco, 'vc não possui ração suficiente para todos animais. Compre mais na loja!', cores.parar_cor)
        print('-='*30)
    

    #[2] - Plantar Trigo + EXP
    elif res == 2 and sementes_trigo == 0:
        print('-=' *30)
        print(cores.letra_vermelha, cores.fundo_branco, 'Você não possui sementes. Compre na loja!', cores.parar_cor)
        print('-='*30)
    elif res == 2 and sementes_trigo != 0:
        print(f'Plantando trigo...')
        sleep(3)
        print(f'Colhendo trigo...')
        sleep(2)
        print('Feito...')
        trigo += sementes_trigo * 2
        sementes_trigo -= sementes_trigo
        exp += 10
    
    #[3] - Loja + EXP
    elif res == 3:
        print(cores.fundo_branco, cores.letra_preta, '[1] - Comprar', cores.parar_cor)
        print(cores.fundo_branco, cores.letra_preta, '[2] - Vender ', cores.parar_cor
        )
        res_loja = int(input('\n?'))
        defs.limpar_tela()

        #[1] - Comprar + EXP
        if res_loja == 1:
            print(cores.fundo_branco, cores.letra_preta, '[1] R$25,00-----------Animal', cores.parar_cor)
            print(cores.fundo_branco, cores.letra_preta, '[2] R$5,00-----------Semente', cores.parar_cor)
            print(cores.fundo_branco, cores.letra_preta, '[3] R$10,00------------Ração', cores.parar_cor)
            res_comprar = int(input('\n?'))
            defs.limpar_tela()

            if res_comprar == 1 and dinheiro >= 25:
                dinheiro -= 25
                animais += 1
                exp += 10
            elif res_comprar == 1 and dinheiro < 25:
                print('-=' *30)
                print(cores.letra_vermelha, cores.fundo_branco, 'Vc não possui dinheiro Suficiente!!!', cores.parar_cor)
                print('-='*30)

            elif res_comprar == 2 and dinheiro >= 5:
                dinheiro -= 5
                sementes_trigo += 1
                exp += 5
            elif res_comprar == 2 and dinheiro < 5:
                print('-=' *30)
                print(cores.letra_vermelha, cores.fundo_branco, 'Vc não possui dinheiro Suficiente!!!', cores.parar_cor)
                print('-='*30)

            elif res_comprar == 3 and dinheiro >= 10:
                dinheiro -= 10
                racao += 1
                exp += 7.5
            elif res_comprar == 3 and dinheiro < 10:
                print('-=' *30)
                print(cores.letra_vermelha, cores.fundo_branco, 'Vc não possui dinheiro Suficiente!!!', cores.parar_cor)
                print('-='*30)

        #[2] - Vender + EXP
        elif res_loja == 2:
            print(cores.fundo_branco, cores.letra_preta, '[1] R$20,00-----------Animal', cores.parar_cor)
            print(cores.fundo_branco, cores.letra_preta, '[2] R$10,00------------Trigo', cores.parar_cor)
            print(cores.fundo_branco, cores.letra_preta, '[3] R$5,00-------------Ração', cores.parar_cor)
            res_vender = int(input('\n?'))
            defs.limpar_tela()

            if res_vender == 1 and animais > 0:
                dinheiro += 20.00
                animais -= 1
                exp += 7.5
            elif res_vender == 1 and animais == 0:
                print('-=' *30)
                print(cores.letra_vermelha, cores.fundo_branco, 'Vc não possui animais!', cores.parar_cor)
                print('-='*30)
            
            elif res_vender == 2 and trigo > 0:
                dinheiro += 10.00
                trigo -= 1
                exp += 5
            elif res_vender == 2 and trigo == 0:
                print('-=' *30)
                print(cores.letra_vermelha, cores.fundo_branco, 'Vc não possui trigo!', cores.parar_cor)
                print('-='*30)

            elif res_vender == 3 and racao > 0:
                dinheiro += 5.00
                racao -= 1
                exp += 3.5
            elif res_vender == 3 and racao == 0:
                print('-=' *30)
                print(cores.letra_vermelha, cores.fundo_branco, 'Vc não possui ração!', cores.parar_cor)
                print('-='*30)
    
    #[4] - Sair
    elif res == 4:
        print('Obrigado por Jogar FarmPython!!!')
        print('Saindo...')
        sleep(2)
        break
    if exp >= 500:
        print(cores.letra_verde, f'Vc Zerou o game!!! Parabens! \n\n\n\n')
        print(cores.letra_verde,
        
        'Copyright © 2021. Todos direitos reservados. Desenvolvido por Davy Pereira.\n\n',
        'Contato: \n',
        'davypereira1802@gmail.com\n\n\n'
        
        , cores.parar_cor)

        break