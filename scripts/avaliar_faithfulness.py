from chatbot import perguntar

from deepeval.metrics import FaithfulnessMetric
from deepeval.test_case import LLMTestCase

from demos.juiz import obter_juiz
from utils.dataset_loader import (
    carregar_dataset,
    contexto_para_texto,
)


def main():
    # 1. Carrega os casos do Golden Dataset
    casos = carregar_dataset()

    # 2. Seleciona o caso DIR-01
    caso = next(
        caso for caso in casos
        if caso["id"] == "DIR-01"
    )

    print("\n=== CASO ===")
    print(f"ID: {caso['id']}")
    print(f"Input: {caso['input']}")

    # 3. Executa o Cosmetic Bot
    print("\n=== EXECUTANDO CHATBOT ===")

    resposta = perguntar(caso["input"])

    print("\n=== RESPOSTA ===")
    print(resposta)

    # 4. Converte o contexto de referência para texto
    contexto = contexto_para_texto(
        caso["contexto_referencia"]
    )

    print("\n=== CONTEXTO DE REFERÊNCIA ===")

    for item in contexto:
        print(item)

    # 5. Cria o caso de teste do DeepEval
    test_case = LLMTestCase(
        input=caso["input"],
        actual_output=resposta,
        retrieval_context=contexto,
    )

    # 6. Configura o modelo juiz
    juiz = obter_juiz()

    # 7. Configura a métrica de Faithfulness
    metrica = FaithfulnessMetric(
        threshold=0.8,
        model=juiz,
        async_mode=False,
    )

    # 8. Executa a avaliação
    print("\n=== FAITHFULNESS ===")

    metrica.measure(test_case)

    status = (
        "PASSOU"
        if metrica.is_successful()
        else "FALHOU"
    )

    print(
        f"{status} — score: {metrica.score:.2f} "
        f"(threshold 0.8)"
    )

    print(f"Motivo do juiz: {metrica.reason}")


if __name__ == "__main__":
    main()