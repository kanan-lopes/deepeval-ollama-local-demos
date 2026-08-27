from chatbot import perguntar
from deepeval.test_case import LLMTestCase

from utils.dataset_loader import (
    carregar_dataset,
    contexto_para_texto,
)


def main():
    # 1. Carrega todos os casos do Golden Dataset
    casos = carregar_dataset()

    # 2. Seleciona somente o DIR-01
    caso = next(
        caso for caso in casos
        if caso["id"] == "DIR-01"
    )

    print("\n=== CASO SELECIONADO ===")
    print(f"ID: {caso['id']}")
    print(f"Input: {caso['input']}")

    # 3. Envia o input real para o Cosmetic Bot
    print("\n=== EXECUTANDO CHATBOT ===")

    resposta = perguntar(caso["input"])

    print("\n=== RESPOSTA DO CHATBOT ===")
    print(resposta)

    # 4. Converte o contexto estruturado do JSON para texto
    contexto = contexto_para_texto(
        caso["contexto_referencia"]
    )

    print("\n=== CONTEXTO DE REFERÊNCIA ===")

    for item in contexto:
        print(item)

    # 5. Cria um LLMTestCase do DeepEval
    test_case = LLMTestCase(
        input=caso["input"],
        actual_output=resposta,
        retrieval_context=contexto,
    )

    print("\n=== LLM TEST CASE ===")
    print(f"Input: {test_case.input}")
    print(f"Actual output: {test_case.actual_output}")
    print(f"Retrieval context: {test_case.retrieval_context}")

    print("\nIntegração concluída com sucesso.")


if __name__ == "__main__":
    main()
