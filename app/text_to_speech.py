from pathlib import Path

from openai import OpenAI


def generate_speech(
    client: OpenAI,
    text: str,
    output_path: Path,
    voice: str = "coral",
) -> Path:
    """
    Converte texto em áudio e salva o resultado em output_path.
    """

    if not text.strip():
        raise ValueError("O texto não pode estar vazio.")

    output_path.parent.mkdir(parents=True, exist_ok=True)

    response = client.audio.speech.create(
        model="gpt-4o-mini-tts",
        voice=voice,
        input=text,
        response_format="mp3",
    )

    response.write_to_file(output_path)

    return output_path
