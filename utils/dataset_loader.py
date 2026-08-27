import json
from pathlib import Path


# Caminho da raiz do projeto
ROOT_DIR = Path(__file__).resolve().parent.parent

# Caminho do Golden Dataset
DATASET_PATH = ROOT_DIR / "dataset" / "golden_dataset.json"


def carregar_dataset():
    """
    Carrega o Golden Dataset e realiza validações estruturais básicas.
    """

    if not DATASET_PATH.exists():
        raise FileNotFoundError(
            f"Golden Dataset não encontrado em: {DATASET_PATH}"
        )

    with open(DATASET_PATH, "r", encoding="utf-8") as arquivo:
        dataset = json.load(arquivo)

    if "casos" not in dataset:
        raise ValueError("O dataset não possui a chave 'casos'.")

    casos = dataset["casos"]

    if not casos:
        raise ValueError("O Golden Dataset não possui casos de teste.")

    ids = [caso["id"] for caso in casos]

    if len(ids) != len(set(ids)):
        raise ValueError("Existem IDs duplicados no Golden Dataset.")

    return casos


def contexto_para_texto(contexto_referencia):
    """
    Converte os produtos estruturados do contexto de referência
    em textos que poderão ser usados posteriormente pelo DeepEval.
    """

    contextos = []

    for produto in contexto_referencia:
        texto = (
            f"Produto: {produto['nome']}; "
            f"Marca: {produto['marca']}; "
            f"Categoria: {produto['categoria']}; "
            f"Tipo de pele: {produto['tipo_pele']}; "
            f"Preço: R$ {produto['preco']:.2f}; "
            f"Ingredientes: {', '.join(produto['ingredientes'])}."
        )

        contextos.append(texto)

    return contextos
