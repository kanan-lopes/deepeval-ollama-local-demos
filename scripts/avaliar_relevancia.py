from chatbot import perguntar

from deepeval.metrics import AnswerRelevancyMetric
from deepeval.test_case import LLMTestCase

from demos.juiz import obter_juiz
from utils.dataset_loader import carregar_dataset


def main():
    # 1. Carrega o Golden Dataset
    casos = carregar_dataset()

    # 2. Seleciona o DIR-01
    caso = next(
        caso for caso in casos
        if caso["id"] == "DIR-01"
    )

    print("\n=== CASO ===")
    print(f"ID: {caso['id']}")
    print(f"Input: {caso['input']}")

    # 3. Obtém uma resposta real do chatbot
    print("\n=== EXECUTANDO CHATBOT ===")

    resposta = perguntar(caso["input"])

    print("\n=== RESPOSTA ===")
    print(resposta)

    # 4. Monta o LLMTestCase
    test_case = LLMTestCase(
        input=caso["input"],
        actual_output=resposta,
    )

    # 5. Configura o juiz
    juiz = obter_juiz()

    # 6. Cria a métrica
    metrica = AnswerRelevancyMetric(
        threshold=0.7,
        model=juiz,
        async_mode=False,
    )

    # 7. Avalia o caso
    print("\n=== ANSWER RELEVANCY ===")

    metrica.measure(test_case)

    status = (
        "PASSOU"
        if metrica.is_successful()
        else "FALHOU"
    )

    print(
        f"{status} — score: {metrica.score:.2f} "
        f"(threshold 0.7)"
    )

    print(f"Motivo do juiz: {metrica.reason}")


if __name__ == "__main__":
    main()