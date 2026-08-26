# 01 — Setup e Validação Inicial

## Ambiente

- Sistema operacional: Windows
- Ambiente virtual: `.venv`
- DeepEval: `4.1.9`
- Provider da aplicação: Ollama
- Modelo da aplicação: `qwen3:8b`
- Modelo juiz: `qwen2.5:7b-instruct`

Validação das dependências:

`python -m pip check`

Resultado esperado:

`No broken requirements found.`

---

## Smoke Tests

### 1. Listagem de produtos

**Input:**  
> Quais protetores solares vocês têm?

**Resultado técnico:** PASS

O bot retornou corretamente os produtos do catálogo, mas adicionou alguns benefícios não presentes explicitamente na fonte.

---

### 2. Consulta direta

**Input:**  
> Quanto custa o Sérum de Vitamina C 10%?

**Resultado técnico:** PASS

Preço, marca e ingredientes foram retornados corretamente. A resposta também incluiu claims não presentes no catálogo, como combate a manchas, ressecamento e brilho por 24 horas.

---

### 3. Recomendação por perfil

**Input:**  
> Qual protetor solar vocês têm para pele sensível?

**Resultado técnico:** PASS

O produto recomendado estava de acordo com o catálogo, porém a resposta acrescentou alegações como “não irrita a pele” e outros benefícios não explicitados na fonte.

---

## Validação do Judge

Foi executada a demo de Answer Relevancy com `qwen2.5:7b-instruct`.

| Caso | Score | Resultado |
| --- | ---: | --- |
| Resposta relevante | 1.00 | PASS |
| Resposta irrelevante | 0.00 | FAIL |

A execução foi repetida três vezes e os scores permaneceram idênticos.

O `reason` do caso negativo, porém, apresentou uma justificativa contraditória com o score em todas as execuções. Por isso, os `reason` serão usados como apoio, mas sempre analisados criticamente.

---

## Conclusão

A infraestrutura foi validada com sucesso:

- chatbot funcionando com Ollama;
- `qwen3:8b` como modelo da aplicação;
- `qwen2.5:7b-instruct` funcionando como judge;
- DeepEval executando corretamente.

Os smoke tests também levantaram hipóes iniciais de problemas de fidelidade ao catálogo e de claims não sustentados, que serão investigadas na sessão exploratória.
