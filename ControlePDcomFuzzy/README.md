# Controle-PD-com-Fuzzy

# Simulação de Controle Fuzzy de Elevador

Este projeto implementa um sistema de controle fuzzy para um elevador utilizando Python e bibliotecas como scikit-fuzzy, numpy, matplotlib e tkinter para simulação e interface gráfica.

## Descrição

O objetivo do projeto é simular o movimento de um elevador entre diferentes andares utilizando um controlador fuzzy. O sistema ajusta a potência do motor do elevador com base no erro (diferença entre o andar desejado e o atual) e na variação do erro.

## Funcionalidades

- **Interface Gráfica (Tkinter)**: Permite selecionar andares e iniciar a simulação.
- **Controlador Fuzzy**: Utiliza regras fuzzy para calcular a potência do motor.
- **Simulação**: Mostra a posição do elevador ao longo do tempo até alcançar o andar desejado.
- **Gráficos (Matplotlib)**: Plota a posição do elevador e o set point (andar desejado) ao longo do tempo.

## Estrutura do Projeto

- `andares`: Dicionário que mapeia os andares para suas alturas correspondentes.
- `iniciar_simulacao`: Função que inicia a simulação com base no andar selecionado.
- `simulacao`: Função principal que executa a simulação do movimento do elevador.
- `ControleVelocidade`: Controlador fuzzy definido usando scikit-fuzzy.
- `tkinter`: Interface gráfica para interação com o usuário.

## Requisitos

- Python 3.9 ou superior
- Bibliotecas Python: numpy, matplotlib, scikit-fuzzy, tkinter, control

## Instalação
```bash    
    https://github.com/Jonathan-Stefan/Trabalhos-Inatel/tree/main/ControlePDcomFuzzy
```
```bash    
    - pip install scipy
    - pip install matplotlib
    - pip install control
    - pip install tk 
    - pip install pandas
```

2. Use a interface gráfica para selecionar o andar desejado e iniciar a simulação.

## Exemplo de Código

```python
andares = {
    "Térreo": 4,
    "1º Andar": 8,
    "2º Andar": 11,
    "3º Andar": 14,
    "4º Andar": 17,
    "5º Andar": 20,
    "6º Andar": 23,
    "7º Andar": 26,
    "8º Andar": 29
}

def iniciar_simulacao(andar_deslocado, nome_andar):
    global andarAtual, posicaoAtual
    andarAtual = posicaoAtual
    label_atual.config(text=f"Andar Atual: {nome_andar}")
    simulacao(andar_deslocado, andarAtual)

def simulacao(andarDeslocado, andarAtual):
    # Código de simulação aqui
    pass

# Interface gráfica com Tkinter
root = tk.Tk()
root.title("Simulação de Controle Fuzzy de Elevador")
label_atual = tk.Label(root, text="Andar Atual: Térreo", font=("Helvetica", 16))
label_atual.pack()
# Configuração dos botões
root.mainloop()
```
## Interface grafica
- Cria uma janela principal usando Tkinter.
- Adiciona campos de entrada (Entry) para os andares requeridos.

## Autor
[Jonathan Stefan Covelo de Carvalho]

## Contato

Jonathan Carvalho - [jonathan.stefan@gec.inatel.br]

Sinta-se à vontade para entrar em contato caso tenha dúvidas ou sugestões!