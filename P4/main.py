import click
from src.rag import retrieve_relevant_context
from src.utils import load_knowledge_base
from src.inference_engine import chain_of_thought_prompt
import ollama
import logging

# Basic logger configuration
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

OLLAMA_MODEL = "llama3.2:1b"


@click.command()
@click.argument("knowledge_base_file", type=click.Path(exists=True))
@click.option(
    "--mode",
    type=click.Choice(["rag", "cot"], case_sensitive=False),
    default="rag",
    help="Select the mode of operation: rag, or cot (chain of thought).",
)
@click.option(
    "--model", default=OLLAMA_MODEL, help="Select the virtual assistant model."
)
@click.option(
    "--verbose", is_flag=True, help="Display detailed execution process information."
)
def start_assistant(knowledge_base_file, mode, model, verbose):
    """
    Start the interactive virtual assistant.
    """
    if verbose:
        click.echo("🔍 Verbose mode activated. Displaying execution details.")

    print("📚 Welcome to the Academic Virtual Assistant. Type 'exit' to quit.")
    print(f"🔧 Selected model: {model} / 🔧 Selected mode: {mode}")
    print("🔎 Example queries:")
    print("    - Which courses does Juan Perez take?")
    print("    - Tell me about Modern Physics.")
    print("    - Who teaches Data Structures and Algorithms?")

    if verbose:
        click.echo(f"📁 Loading knowledge base from file: {knowledge_base_file}")

    knowledge_base = load_knowledge_base(knowledge_base_file)

    if verbose:
        click.echo(
            f"📚 Knowledge base loaded successfully. Found {len(knowledge_base)} items."
        )

    while True:

        user_query = input("\n🔎 Your Query: ").strip()

        if not user_query:
            print("❌ Please enter a valid query.")
            continue

        if user_query.lower() in ["exit", "quit"]:
            print("👋 Goodbye!")
            break

        # Initialize prompt with a default error message
        prompt = "❌ Invalid mode. Please select 'rag' or 'cot'."

        # RAG Mode
        if mode == "rag":
            if verbose:
                click.echo(
                    "🔍 RAG mode selected. Searching for relevant context for the query..."
                )

            context = retrieve_relevant_context(user_query, knowledge_base)
            prompt = f"Context: {context}\n\nUser Query: {user_query}\nAnswer:"

            if verbose:
                click.echo(f"🔎 Relevant context found: {context[:200]}...")

        # Chain of Thought (CoT) Mode
        elif mode == "cot":
            if verbose:
                click.echo(
                    "🔍 Chain of Thought mode selected. Searching for relevant context for the query..."
                )

            # Obtener contexto relevante
            context = retrieve_relevant_context(user_query, knowledge_base)

            # Generar el prompt con la reflexión inicial
            prompt = chain_of_thought_prompt(user_query, context)

            if verbose:
                click.echo(f"🔎 Relevant context found: {context[:200]}...")

        # Call the model with the corresponding prompt
        if verbose:
            click.echo("💬 Sending prompt to the model...")

        response = call_language_model(prompt, verbose)
        print(f"\n🤖 Assistant: {response}")

        if verbose:
            click.echo("✅ Response received and displayed to the user.")


def call_language_model(prompt, verbose):
    """
    Calls the language model to get a response.
    """
    try:
        if verbose:
            click.echo("🔧 Initiating call to Ollama model...")

        response = ollama.chat(
            model=OLLAMA_MODEL, messages=[{"role": "user", "content": prompt}]
        )

        if verbose:
            click.echo("🔧 Response received from the model.")

        return response.get("message", {}).get(
            "content", "❌ No valid response received from the model."
        )

    except Exception as e:
        logging.error(f"Error communicating with the Ollama model: {e}")

        if verbose:
            click.echo(
                f"❌ An error occurred while communicating with the Ollama model: {e}"
            )

        return "❌ An error occurred while obtaining the response. Please try again."


if __name__ == "__main__":
    start_assistant()
