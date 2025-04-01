# 🏠 Simulador de Lucros Airbnb

Resolvi formular um app interativo de lucros para aluguel por temporada no **Airbnb**, voltado para **proprietários de imóveis** e **co-anfitriões** que desejam entender melhor o retorno financeiro de uma locação. Ainda penso em aprimorar o app aplicando estratégias de precificação dinâmica para otimizar a ocupação e maximização de receita.

## Objetivo

Este app permite simular, de forma visual e simples:

- A **receita estimada** com base na taxa de ocupação e valor da diária
- O impacto das **taxas do Airbnb**
- O valor recebido pelo **coanfitrião** (gestor)
- O **lucro final do proprietário**

Tudo com base em dados configuráveis, como:

- Diária média 
- Ocupação mensal 
- Taxa de limpeza 
- Comissão do coanfitrião

## Acesse o simulador online:

👉 [Clique aqui para abrir o app no navegador](https://airbnb-simulador-lucros-e84y6qwzzzxsbphj55u2bw.streamlit.app)

> Você pode alterar os valores no menu lateral e visualizar os lucros em tempo real.

---

## Exemplo de uso

1. Defina uma diária de R$250
2. Estime uma ocupação de 80% para o mês
3. Ajuste a taxa do Airbnb e comissão do coanfitrião
4. Veja em segundos:
   - Receita total
   - Taxas pagas
   - Comissão do gestor
   - Lucro final do dono do imóvel

---

## Arquivos do projeto

| Arquivo         | Função                                          |
|-----------------|--------------------------------------------------|
| `app.py`        | Código principal do app em Python com Streamlit |
| `requirements.txt` | Lista de dependências                         |
| `README.md`     | Documentação do projeto                         |

---

## Como rodar localmente

Se quiser testar o projeto no seu computador:

```bash
git clone https://github.com/raissaalvimt/airbnb-simulador-lucros.git
cd airbnb-simulador-lucros
pip install -r requirements.txt
streamlit run app.py
