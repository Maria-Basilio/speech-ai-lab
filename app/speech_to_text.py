from pathlib import Path

from openai import OpenAI


def transcribe_audio(
    client: OpenAI,
    audio_path: Path,
) -> str:
    """
    Envia um arquivo de áudio para transcrição
    e retorna o texto reconhecido.
    """

    if not audio_path.exists():
        raise FileNotFoundError(
            f"Arquivo de áudio não encontrado: {audio_path}"
        )

    if not audio_path.is_file():
        raise ValueError(
            f"O caminho informado não é um arquivo: {audio_path}"
        )

    with audio_path.open("rb") as audio_file:
        transcription = client.audio.transcriptions.create(
            model="gpt-4o-transcribe",
            file=audio_file,
            language="pt",
        )

    return transcription.text
