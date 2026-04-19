import pandas as pd
import plotly.express as px

# Estrutura de Dados (Visão de Gestão de Projetos Ágeis)
data = {
    'Sprint_Ativa': ['Refatoração API', 'Dashboard BI', 'Segurança Bancária', 'App UI/UX', 'Cloud Migration'],
    'KPI_Status': ['On Track', 'Completed', 'At Risk', 'Critical', 'On Track'],
    'Completion_%': [85, 100, 45, 15, 90]
}

df = pd.DataFrame(data)

# Criando o Dashboard Profissional
fig = px.bar(df, x='Sprint_Ativa', y='Completion_%', color='KPI_Status',
             title='📊 Agile Performance & Analytics Hub - Engineering Overview',
             text='Completion_%',
             color_discrete_map={'On Track': '#2ecc71', 'Completed': '#3498db', 'At Risk': '#f1c40f', 'Critical': '#e74c3c'},
             template='plotly_dark')

# Salvando como site
fig.write_html("index.html")
print("✅ Dashboard gerado com sucesso!")
