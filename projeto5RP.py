"""
Para descobrir qual interruptor controla cada lâmpada com apenas duas idas até a sala das lâmpadas, a estratégia é a seguinte: Ligue um interruptor e deixe-o ligado por alguns minutos. Em seguida, desligue-o e ligue um segundo interruptor. Vá até a sala das lâmpadas. A lâmpada que estiver acesa será controlada pelo segundo interruptor, a lâmpada que estiver apagada mas quente será controlada pelo primeiro interruptor, e a lâmpada que estiver apagada e fria será controlada pelo terceiro interruptor.

Estratégia para identificar os interruptores:
a) Preparação inicial  

Ligue o primeiro interruptor e espere alguns minutos. Esse tempo é suficiente para que a lâmpada controlada por esse interruptor aqueça. Após esse tempo, desligue o primeiro interruptor e ligue o segundo interruptor.
b) Primeira ida à sala das lâmpadas  

Ao chegar à sala das lâmpadas, você observará três possíveis situações:

A lâmpada acesa estará conectada ao segundo interruptor, que foi o último a ser ligado.
A lâmpada apagada e quente será a que estava conectada ao primeiro interruptor, que foi ligado inicialmente e depois desligado.
A lâmpada apagada e fria será a que está conectada ao terceiro interruptor, que não foi ligado em nenhum momento.
Desse modo, com essa sequência de ações, é possível identificar com clareza qual interruptor controla cada lâmpada utilizando apenas duas idas à sala.
"""