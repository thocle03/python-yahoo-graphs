import yfinance as yf
import matplotlib.pyplot as plt

class StockData:
    def __init__(self, ticker):
        """
        Initialise un objet StockData avec un symbole boursier.
        :param ticker: Le symbole boursier (par exemple, "TSLA" pour Tesla).
        """
        self.ticker = ticker
        self.data = None

    def fetch_data(self, start_date, end_date):
        """
        Récupère les données historiques pour le symbole boursier sur une période donnée.
        :param start_date: Date de début (format: "YYYY-MM-DD").
        :param end_date: Date de fin (format: "YYYY-MM-DD").
        """
        try:
            self.data = yf.download(self.ticker, start=start_date, end=end_date)
            print(f"Données récupérées pour {self.ticker}.")
        except Exception as e:
            print(f"Erreur lors de la récupération des données : {e}")

class StockGraph:
    @staticmethod
    def plot_stock(data, title="Graphique des actions", output_file="stock_graph.png"):
        """
        Trace un graphique des prix de clôture d'une action et l'enregistre sous forme de fichier PNG.
        :param data: Les données récupérées (DataFrame de pandas).
        :param title: Le titre du graphique.
        :param output_file: Le nom du fichier de sortie (par défaut: "stock_graph.png").
        """
        if data is not None and not data.empty:
            plt.figure(figsize=(10, 5))
            plt.plot(data['Close'], label='Prix de clôture')
            plt.title(title)
            plt.xlabel("Date")
            plt.ylabel("Prix ($)")
            plt.legend()
            plt.grid()
            plt.savefig(output_file)  # Enregistre le graphique sous forme de fichier PNG
            print(f"Graphique enregistré sous le nom : {output_file}")
        else:
            print("Aucune donnée disponible pour tracer le graphique.")

# Exemple d'utilisation
if __name__ == "__main__":
    # Initialiser les classes
    tesla_stock = StockData("TSLA")
    tesla_stock.fetch_data(start_date="2023-01-01", end_date="2023-12-01")

    # Tracer et sauvegarder le graphique
    StockGraph.plot_stock(tesla_stock.data, title="Évolution de l'action Tesla (TSLA)", output_file="tesla_stock_2023.png")
