import cores

def menu():
    print(cores.fundo_verde,'-=' * 15, cores.parar_cor)
    print('\n          \033[3;30;47mFarmVille\033[m\n')
    print(cores.fundo_verde, '-='* 15, cores.parar_cor, '\n')


def limpar_tela():
    import os
    os.system('cls')