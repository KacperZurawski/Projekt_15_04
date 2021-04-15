# -*- coding: utf-8 -*-
import numpy as np

"""
%% 1(a) inicjalizacja parametrow sterujacych programem CZESC 1
[ parametry_sterujace ] = inicjalizacja_parametrow_sterujacych ( ... ) ;
%% 1(b) definicja parametrow fizycznych i geometrycznych obszaru , warunkow brzegowych CZESC 1
% - definicja przedzialu ,
% - liczba wezlow / elementow modelu w przypadku dyskretyzacji jednorodnej
% - zadanie funkcji wymuszajacej , parametrow rownania rozniczkowego
% - ...
[ parametry_geom_i_fiz ] = definicja_parametrow_geom_i_fiz ( ... ) ;
"""

def inicjalizacja_parametrow_sterujacych():
    
#1a
[parametry_sterujace] = 


#1b


wezly = np.array([[1, 0],
                  [2, 1],
                  [3, 0.5],
                  [4, 0.75]])

elementy = np.array([[1, 1, 3],
                     [2, 4, 2],
                     [4, 3, 4]])

twb_L = 'D'
twb_R = 'D'

wwb_L = 0
wwb_R = 1