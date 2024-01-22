# Nome: Vitor F. Regis , Felipe D. Martins
# RA: 123612 , 123959

# Funções 

def organiza(hora_string):
    horas, minutos, segundos = map(int, hora_string.split(':'))
    return horas, minutos, segundos

def volta_para_string(horas,minutos,segundos):
    horario = str(horas).zfill(2) + ":" + str(minutos).zfill(2) + ":" + str(segundos).zfill(2)
    return horario

def soma_horario(horario1,horario2):
    horas1, minutos1, segundos1 = organiza(horario1)
    horas2, minutos2, segundos2 = organiza(horario2)

    nova_h = horas1 + horas2
    novo_m = minutos1 + minutos2
    novo_s = segundos1 + segundos2
    
    if novo_s >= 60:
        novo_m += 1
        novo_s = novo_s % 60

    if novo_m >= 60:
        nova_h += 1
        novo_m = novo_m % 24

    if nova_h >= 24:
         nova_h = nova_h % 24

    novo_horario = volta_para_string(nova_h,novo_m,novo_s)

    return novo_horario

def subtrai_horario(horario1,horario2):
    horas1, minutos1, segundos1 = organiza(horario1)
    horas2, minutos2, segundos2 = organiza(horario2)

    horas1, minutos1, segundos1 = organiza(horario1)
    horas2, minutos2, segundos2 = organiza(horario2)

    nova_h = horas1 - horas2
    novo_m = minutos1 - minutos2
    novo_s = segundos1 - segundos2
    
    if novo_s < 0:
        novo_m = 1
        novo_s = novo_s % 60

    if novo_m < 0:
        nova_h += 1
        novo_m = novo_m % 24

    if nova_h < 0:
         nova_h = nova_h % 24

    novo_horario = volta_para_string(nova_h,novo_m,novo_s)

    return novo_horario

def compara_horario(horario1,horario2):
    horas1, minutos1, segundos1 = organiza(horario1)
    horas2, minutos2, segundos2 = organiza(horario2)

    if horas1 > horas2: 
        horario_maior = horario1
    elif horas2 > horas1:
        horario_maior = horario2
    else:
        if minutos1 > minutos2:
            horario_maior = horario1
        elif minutos2 > minutos1:
            horario_maior = horario2
        else:
            if segundos1 > segundos2:
                horario_maior = horario1
            elif segundos2 > segundos1:
                horario_maior = horario2
                
    return horario_maior

def tique(hora_atual):
    horas, minutos, segundos = organiza(hora_atual)

    segundos += 1 

    if segundos == 60:
        minutos += 1
        segundos = 00

    if minutos == 60:
        horas += 1
        minutos = 00

    if horas == 24:
        horas = 00

    novo_horario = volta_para_string(horas,minutos,segundos)

    return novo_horario

# Casos de Teste 	
def test_01():
	assert subtrai_horario("22:43:45","02:03:25") == "20:40:20"
     
def test_02():
	assert soma_horario("22:43:45","02:03:25") == "00:47:10"
     
def test_03():
	assert compara_horario("12:22:13","08:12:00") == "12:22:13"
      
def test_04():
	assert tique("22:43:45") == "22:43:46"
     
def test_05():
	assert subtrai_horario("22:43:45","23:46:51") == "23:01:54"
     
def test_06():
	assert soma_horario("22:43:45","10:28:00") == "09:23:45"
     
def test_07():
	assert compara_horario("23:22:13","23:58:12") == "23:58:12"
      
def test_08():
	assert tique("23:59:59") == "00:00:00"