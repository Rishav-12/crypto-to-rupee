import requests
from rich import print as rprint
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt

with open("api_key.txt","r") as file:
    KEY = file.read().strip()

BASE_URL = "http://api.coinlayer.com/api/live"

def get_exchange_rate(ticker):
    """
    returns the exchange rate for the given ticker to INR
    """
    request_url = f"{BASE_URL}?access_key={KEY}&target=INR&symbols={ticker}"
    data = requests.get(request_url).json()

    return data["rates"][ticker]

def run():
    """
    renders a pretty ui and runs the program
    """
    panel = Panel(Text("Crypto to Rupee Converter", justify="center"))
    rprint(panel)

    rprint("[yellow]Please provide a crypto ticker symbol[/yellow]")
    ticker = Prompt.ask("[red]>[/red][green]>[/green][blue]>[/blue]", default="BTC")

    rprint(f"\n\n[bold][magenta]Fetching exchange rate of [/magenta][purple]{ticker} to Rupee[/purple][/bold] :rocket:")
    rate = get_exchange_rate(ticker)
    rprint(f"[italic green]The rate is {rate}[/italic green]")

if __name__ == "__main__":
    run()
