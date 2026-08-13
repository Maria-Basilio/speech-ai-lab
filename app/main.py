import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

from speech_to_text import transcribe_audio
from text_to_speech import generate_speech


# Localização do projeto
BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_DIR = BASE_DIR / "input"
OUTPUT_DIR = BASE_DIR / "output"


def create_client() -> OpenAI:
    """
    Cria o cliente da OpenAI usando a chave
    armazenada no arquivo .env.
    """

    load_dotenv()

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise RuntimeError(
            "A variável OPENAI_API_KEY não foi configurada."
        )

    return OpenAI(api_key=api_key)


def text_to_speech_flow(client: OpenAI) -> None:
    """
    Executa o fluxo Texto -> Fala.
    """

    text = input("\nDigite o texto:\n").strip()

    if not text:
        print("\nErro: o texto não pode estar vazio.")
        return

    voice = input(
        "\nDigite a voz [coral]: "
    ).strip()

    if not voice:
        voice = "coral"

    output_path = OUTPUT_DIR / "speech.mp3"

    print("\nGerando áudio...")

    try:
        generate_speech(
            client=client,
            text=text,
            output_path=output_path,
            voice=voice,
        )

        print("\nÁudio salvo em:")
        print(output_path)

    except Exception as error:
        print(f"\nErro durante a geração do áudio: {error}")


def speech_to_text_flow(client: OpenAI) -> None:
    """
    Executa o fluxo Fala -> Texto.
    """

    audio_input = input(
        "\nArquivo: "
    ).strip()

    if not audio_input:
        print("\nErro: informe o caminho do arquivo.")
        return

    audio_path = Path(audio_input)

    if not audio_path.is_absolute():
        audio_path = BASE_DIR / audio_path

    try:
        transcription = transcribe_audio(
            client=client,
            audio_path=audio_path,
        )

        print("\nTranscrição:")
        print()
        print(f'"{transcription}"')

    except FileNotFoundError as error:
        print(f"\nErro: {error}")

    except Exception as error:
        print(f"\nErro durante a transcrição: {error}")


def speech_text_speech_flow(client: OpenAI) -> None:
    """
    Executa o fluxo Fala -> Texto -> Fala.
    """

    audio_input = input(
        "\nArquivo de áudio: "
    ).strip()

    if not audio_input:
        print("\nErro: informe o caminho do arquivo.")
        return

    audio_path = Path(audio_input)

    if not audio_path.is_absolute():
        audio_path = BASE_DIR / audio_path

    output_path = OUTPUT_DIR / "repeated.mp3"

    try:
        print("\n1/2 - Transcrevendo áudio...")

        transcription = transcribe_audio(
            client=client,
            audio_path=audio_path,
        )

        print("\nTexto transcrito:")
        print(f'"{transcription}"')

        if not transcription.strip():
            print("\nErro: a transcrição retornou vazia.")
            return

        print("\n2/2 - Gerando novo áudio...")

        generate_speech(
            client=client,
            text=transcription,
            output_path=output_path,
            voice="coral",
        )

        print("\nNovo áudio salvo em:")
        print(output_path)

    except FileNotFoundError as error:
        print(f"\nErro: {error}")

    except Exception as error:
        print(
            f"\nErro no fluxo Speech -> Text -> Speech: {error}"
        )


def show_menu() -> None:
    """
    Exibe o menu principal.
    """

    print("\n==============================")
    print("       SPEECH AI LAB")
    print("==============================")
    print()
    print("1 - Texto para fala")
    print("2 - Fala para texto")
    print("3 - Speech -> Text -> Speech")
    print("0 - Sair")


def main() -> None:
    """
    Ponto de entrada da aplicação.
    """

    try:
        client = create_client()

    except RuntimeError as error:
        print(f"\nErro de configuração: {error}")
        return

    while True:
        show_menu()

        option = input("\nEscolha uma opção: ").strip()

        if option == "1":
            text_to_speech_flow(client)

        elif option == "2":
            speech_to_text_flow(client)

        elif option == "3":
            speech_text_speech_flow(client)

        elif option == "0":
            print("\nEncerrando o SPEECH AI LAB...")
            break

        else:
            print(
                "\nOpção inválida. "
                "Escolha 0, 1, 2 ou 3."
            )


if __name__ == "__main__":
    main()
