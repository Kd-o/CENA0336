#!/usr/bin/env python3
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))
import sys
nome = sys.argv[1]
cor = sys.argv[2]
atividade =  sys.argv[3]
animal = sys.argv[4]
print(nome,',',cor,',',atividade,',',animal)
print(nome,'+',cor,'+',atividade,'+',animal)
#'jose renato' 'roxo' 'fazer bolos' 'gatos'
