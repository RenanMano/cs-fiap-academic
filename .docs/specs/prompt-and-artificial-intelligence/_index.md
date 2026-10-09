<!--META
{
  "header": "Prompt and Artificial Intelligence",
  "typing": ["Do machine learning aos LLMs", "Embeddings + IA generativa = RAG", "Agentes, ferramentas e handoffs", "Guardrails: BLOCK × ALLOW"],
  "badges": [["Tema", "IA generativa", "E60000"], ["SDK", "OpenAI Agents", "FF781F"]],
  "icons": "py",
  "icons_alt": "Python",
  "mapa": "flowchart LR\n    A[\"IA e machine learning<br/>aula 01\"] --> B[\"Aprendizado estatístico<br/>aula 02\"]\n    B --> C[\"LLMs, gradiente e BPE<br/>aula 03\"]\n    C --> D[\"Embeddings e RAG<br/>aula 04\"]\n    D --> E[\"Pipeline RAG e splitting<br/>aula 05\"]\n    E --> F[\"Restaurante agêntico<br/>aula 06\"]\n    F --> G[\"Banco conversacional<br/>e testes de guardrails<br/>aula 07\"]"
}
META-->

**Prompt and Artificial Intelligence** percorre o caminho da IA clássica até as aplicações com LLMs:

- aprendizado de máquina e aprendizado estatístico ($Y = f(X) + \varepsilon$, MSE, paramétrico × não paramétrico);
- regressão logística, gradiente descendente, redes neurais e tokenização (BPE);
- engenharia de *prompt*;
- embeddings e RAG;
- agentes com o OpenAI Agents SDK: ferramentas, *handoffs*, *guardrails*, sessões e canais (Telegram e Gradio).

As duas últimas aulas são *notebooks* práticos: um atendente de restaurante e um assistente bancário com PIX simulado, este acompanhado de seis conjuntos de casos de teste de *guardrails*.

**Docente identificado nos materiais:** José Maia Neto, nome registrado nos metadados dos arquivos de slides.

> [!NOTE]
> Os exemplos em Python das páginas são implementações próprias e executáveis sem chave de API, como o BPE, a regressão logística, os embeddings de brinquedo, o RAG mínimo e a avaliação de *guardrails*. Os *notebooks* das aulas 06 e 07 dependem da API da OpenAI e do Google Colab. Eles foram lidos com as saídas salvas, mas **não foram executados**. Leem as credenciais de Secrets ou de variáveis de ambiente, e nenhuma chave está no repositório.
>
> **Arquivos repetidos:**
>
> - as apresentações das aulas 04 e 05 têm o mesmo texto;
> - `Restaurante_Agentico_Telegram.ipynb` aparece, idêntico, nas aulas 06 e 07.
>
> As páginas tratam essas repetições sem duplicar conteúdo.
