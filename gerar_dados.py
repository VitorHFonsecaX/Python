import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def gerar_dados_frota(num_registros=250):
    tipos_veiculo = ['Caminhão Baú', 'Van', 'Carreta', 'Caminhão Refrigerado']
    status = ['Em Uso', 'Em Manutenção', 'Disponível']
    anos = np.random.randint(2014, 2023, num_registros)
    quilometragens = [np.random.randint(50000, 450000) for _ in range(num_registros)]
    capacidades = [np.random.randint(2000, 25000) for _ in range(num_registros)]
    
    # Linha corrigida
    letras = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    placas = [f'{np.random.choice(letras)}{np.random.choice(letras)}{np.random.choice(letras)}-{np.random.randint(1000, 9999)}' for _ in range(num_registros)]

    dados = {
        'id_veiculo': range(1, num_registros + 1),
        'placa': placas,
        'tipo_veiculo': np.random.choice(tipos_veiculo, num_registros),
        'capacidade_kg': capacidades,
        'status': np.random.choice(status, num_registros),
        'quilometragem_km': quilometragens,
        'ano_fabricacao': anos
    }
    df = pd.DataFrame(dados)
    return df

def gerar_dados_motoristas(num_registros=250):
    nomes = [
        'João Silva', 'Maria Oliveira', 'Pedro Santos', 'Ana Souza', 'Carlos Pereira',
        'Sofia Costa', 'Lucas Martins', 'Beatriz Rocha', 'Rafael Gomes', 'Juliana Alves'
    ] * 25
    status = ['Ativo', 'Férias', 'Afastado']
    tempos_servico = np.random.randint(1, 15, num_registros)
    
    dados = {
        'id_motorista': range(101, 101 + num_registros),
        'nome': nomes[:num_registros],
        'cnh': [f'{np.random.randint(100000000, 999999999)}' for _ in range(num_registros)],
        'status': np.random.choice(status, num_registros),
        'tempo_servico_anos': tempos_servico,
        'id_veiculo_preferido': np.random.randint(1, 251, num_registros)
    }
    df = pd.DataFrame(dados)
    return df

def gerar_dados_entregas(num_registros=250):
    cidades = ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba', 'Salvador', 'Porto Alegre', 'Brasília', 'Recife', 'Fortaleza']
    status_entrega = ['Entregue', 'Em Trânsito', 'Atrasada', 'Cancelada']
    
    id_veiculos = np.random.randint(1, 251, num_registros)
    id_motoristas = np.random.randint(101, 351, num_registros)
    
    data_partida = [datetime(2025, 5, 1) + timedelta(days=np.random.randint(0, 30), hours=np.random.randint(6, 18)) for _ in range(num_registros)]
    data_chegada_prevista = [d + timedelta(hours=np.random.randint(8, 72)) for d in data_partida]
    
    origem_cidade = np.random.choice(cidades, num_registros)
    destino_cidade = [c for c in np.random.choice(cidades, num_registros) if c != origem_cidade[0]]
    
    distancias = np.random.randint(100, 2000, num_registros)
    pesos = np.random.randint(500, 25000, num_registros)
    valores_frete = [int(d * 2.5 + p * 0.1) for d, p in zip(distancias, pesos)]

    dados = {
        'id_entrega': range(2001, 2001 + num_registros),
        'id_veiculo': id_veiculos,
        'id_motorista': id_motoristas,
        'data_partida': data_partida,
        'data_chegada_prevista': data_chegada_prevista,
        'status_entrega': np.random.choice(status_entrega, num_registros),
        'origem_cidade': origem_cidade,
        'destino_cidade': np.random.choice(cidades, num_registros),
        'distancia_km': distancias,
        'peso_carga_kg': pesos,
        'valor_frete': valores_frete
    }
    df = pd.DataFrame(dados)
    return df

if __name__ == "__main__":
    df_frota = gerar_dados_frota()
    df_motoristas = gerar_dados_motoristas()
    df_entregas = gerar_dados_entregas()

    df_frota.to_csv('frota.csv', index=False)
    df_motoristas.to_csv('motoristas.csv', index=False)
    df_entregas.to_csv('entregas.csv', index=False)

    print("Arquivos CSV gerados com sucesso: frota.csv, motoristas.csv, entregas.csv")
